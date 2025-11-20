select j.FLAVOR
from FIRST_HALF as f
join JULY as j on f.FLAVOR = j.FLAVOR
group by FLAVOR
having sum(j.TOTAL_ORDER) + sum(f.TOTAL_ORDER)
order by sum(j.TOTAL_ORDER) + sum(f.TOTAL_ORDER) desc
limit 3