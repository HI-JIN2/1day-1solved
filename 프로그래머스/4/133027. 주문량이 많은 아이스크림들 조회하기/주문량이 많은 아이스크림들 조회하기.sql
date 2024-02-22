# -- 코드를 입력하세요
SELECT f.FLAVOR
# , (f.TOTAL_ORDER + j.TOTAL_ORDER) as total
from FIRST_HALF f
left join (select FLAVOR,sum(total_order) as july_t
    from JULY
    group by FLAVOR) as a
on f.FLAVOR= a.FLAVOR
order by (f.TOTAL_ORDER + a.july_T) desc
limit 3

# select FLAVOR,sum(total_order)
# from JULY
# group by FLAVOR
