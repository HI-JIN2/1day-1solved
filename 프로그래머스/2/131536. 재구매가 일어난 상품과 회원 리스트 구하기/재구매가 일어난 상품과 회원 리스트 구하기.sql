-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
from online_sale

 GROUP
    BY  USER_ID
        , PRODUCT_ID
HAVING  COUNT(*) > 1
 ORDER
    BY  USER_ID ASC
        , PRODUCT_ID DESC