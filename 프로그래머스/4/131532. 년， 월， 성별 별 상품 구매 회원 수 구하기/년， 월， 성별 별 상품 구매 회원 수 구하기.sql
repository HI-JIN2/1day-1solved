-- 코드를 입력하세요
SELECT year(SALES_DATE),month(SALES_DATE), GENDER, count(distinct o.user_id) as users
from ONLINE_SALE o
left join USER_INFO u 
on o.USER_ID =u.USER_ID
where gender is not null
group by date_format(SALES_DATE,"%Y-%m"), GENDER
order by 1,2,3


# select *
# from (SELECT *
#     from ONLINE_SALE o
#     left join USER_INFO u 
#     on o.USER_ID =u.USER_ID) as j 
# group by date_format(SALES_DATE,"%Y-%m"), GENDER