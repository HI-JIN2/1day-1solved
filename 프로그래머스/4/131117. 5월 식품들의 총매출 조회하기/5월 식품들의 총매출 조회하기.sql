-- 코드를 입력하세요
select f.PRODUCT_ID,f.PRODUCT_NAME, PRICE*j.t as TOTAL_SALES
from FOOD_PRODUCT f
inner join (SELECT PRODUCT_ID,sum(AMOUNT) as t
    from FOOD_ORDER
    where PRODUCE_DATE like "2022-05%"
    group by PRODUCT_ID)  as j
on f.PRODUCT_ID=j.PRODUCT_ID
order by 3 desc, 1 asc