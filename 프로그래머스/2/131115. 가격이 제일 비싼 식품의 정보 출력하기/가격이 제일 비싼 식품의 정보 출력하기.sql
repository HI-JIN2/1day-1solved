-- 코드를 입력하세요
SELECT PRODUCT_ID, PRODUCT_NAME,PRODUCT_CD,CATEGORY,max(PRICE)
from FOOD_PRODUCT
group by (PRODUCT_ID)
order by price desc
limit 1