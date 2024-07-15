--- все накладные за второй квартал 2022 года
select
	*
from
	public.invoice
where
	created_date_time >= '2022-04-01'
	and created_date_time < '2022-07-1';

--- все накладные, у которых есть полисы, созданные за период с 2 по 10 марта
select
	i.*
from
	public.invoice i
join public.distinct_policy dp on
	i.uid = dp.invoice_object_uid
where
	extract(month from dp.policy_created_date_time) = 3
	and extract (day from dp.policy_created_date_time) >= 2
	and extract (day from dp.policy_created_date_time) <= 10;
	
--- обновляющий накладные, у которых город прибытия «Калининград»
update
	public.invoice
set
	  = now()
where
	invoice.arrival_city_name = 'Калининград' returning *;