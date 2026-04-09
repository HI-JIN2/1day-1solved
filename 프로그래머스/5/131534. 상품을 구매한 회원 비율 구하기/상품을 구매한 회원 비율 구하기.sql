-- 코드를 입력하세요


select 
# online_sale_id, u.user_id,  DATE_FORMAT(sales_date, "%Y-%m"), joined
YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, 
# u.USER_ID,
COUNT(distinct u.USER_ID) as PURCHASED_USERS
, round(COUNT(distinct u.USER_ID)/(
    select  count(u.user_id)
    from USER_INFO u
    where DATE_FORMAT(u.JOINED, "%Y") = "2021"
),1) as PUCHASED_RATIO
# select  count(u.user_id)
from ONLINE_SALE o
join USER_INFO u on u.USER_ID = o.USER_ID
where DATE_FORMAT(u.JOINED, "%Y") = "2021"
group by DATE_FORMAT(SALES_DATE, "%Y-%m")
order by 1,2