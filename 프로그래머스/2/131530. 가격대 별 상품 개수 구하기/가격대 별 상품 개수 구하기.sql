-- 코드를 입력하세요
select i.j*10000 as PRICE_GROUP, count(j) as PRODUCTS

from (SELECT PRODUCT_ID,	PRODUCT_CODE,	PRICE, case when price<10000 then 0
    when price>=10000 then floor(price/10000) 
    end as j
# count()
from PRODUCT) as i 
group by i.j
order by 1