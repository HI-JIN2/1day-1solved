-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF f
inner join ICECREAM_INFO i
on f.FLAVOR = i.FLAVOR
group by INGREDIENT_TYPE
order by INGREDIENT_TYPE desc


# ELECT INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
# from FIRST_HALF f
#  inner join icecream_info i
#  on f.flavor = i.flavor
#  group by i.ingredient_type
#  order by TOTAL_ORDER