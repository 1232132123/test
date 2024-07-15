import psycopg2
import uuid
import random
from faker import Faker
import datetime

fake = Faker()

city = [
    'Москва',
    'Санкт-Петербург',
    'Новосибирск',
    'Екатеринбург',
    'Калининград',
]

try:
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='password', host='localhost')
except:
    print('Can`t establish connection to database')
    exit()

start_date = datetime.date(year=2021, month=1, day=1)


curs = conn.cursor()

for i in range(1000):
    invoice_uuid = uuid.uuid4()
    invoice_object_date = fake.date_between(start_date=start_date, end_date='+3y')

    q1 = f"""
    insert into public.invoice
    (
        uid,
        amount,
        arrival_city_name,
        arrival_city_uid,
        arrival_date,
        arrival_kladr,
        cargo_kind,
        created_date_time,
        "date",
        departure_city_name,
        departure_city_uid,
        departure_kladr,
        freight_in_kops,
        net_volume,
        net_weight,
        "number",
        updated_date_time,
        insurance_company,
        transport_company,
        channel_name
    ) values (
        '{invoice_uuid}',
        '{random.randint(1, 1000)}',
        '{random.choice(city)}',
        '{uuid.uuid4()}',
        '{fake.date_between(start_date=start_date, end_date='+3y')}',
        '12345-{i}',
        '{i}',
        '{invoice_object_date}',
        '{fake.date_between(start_date=start_date, end_date='+3y')}',
        '{random.choice(city)}',
        '{uuid.uuid4()}',
        '12345-{i}',
        0,
        1000,
        1000,
        '1',
        '{invoice_object_date}',
        '1-{i}',
        '1-{i}',
        '1-{i}'
    )"""

    q2 = f"""
    insert into public.distinct_policy
    (
        invoice_object_uid,
        invoice_type_id,
        invoice_object_number,
        invoice_object_date,
        policy_created_date_time,
        channel_name,
        "key",
        id
    ) values (
        '{invoice_uuid}',
        '{i}',
        '{i}',
        '{invoice_object_date}',
        '{invoice_object_date}',
        '1-{i}',
        '1-{i}',
        '{uuid.uuid4()}'
    )
    """

    curs.execute(q1)
    curs.execute(q2)
    conn.commit()


curs.close() # закрываем курсор
conn.close() # закрываем соединение
