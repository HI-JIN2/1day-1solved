-- 코드를 입력하세요

select CATEGORY, price as 	MAX_PRICE,	PRODUCT_NAME
from FOOD_PRODUCT f
join 
    (SELECT max(price) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치','식용유')
    group by CATEGORY
    ) p
    on f.price = p.MAX_PRICE
where CATEGORY in ('과자', '국', '김치','식용유')
order by 2 desc
