-- 코드를 입력하세요

select f.CATEGORY, price as 	MAX_PRICE,	PRODUCT_NAME
from FOOD_PRODUCT f
join 
    (SELECT CATEGORY, max(price) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치','식용유')
    group by CATEGORY
    ) p
    on f.price = p.MAX_PRICE and f.CATEGORY = p.CATEGORY
order by 2 desc
