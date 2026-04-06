select hour(f.DATETIME) as HOUR, COUNT(*) as COUNT
from ANIMAL_OUTS f
where hour(f.DATETIME) between 9 and 19
group by hour(f.DATETIME)
order by  1