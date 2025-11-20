select p.product_code, sum(sales_amount)*p.PRICE as SALES
# PRODUCT_CODE
from PRODUCT p
join OFFLINE_SALE o on p.PRODUCT_ID = o.PRODUCT_ID
group by product_code
order by 2 desc, 1