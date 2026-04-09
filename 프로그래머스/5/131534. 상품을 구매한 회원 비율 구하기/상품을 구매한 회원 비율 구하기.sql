select 
    YEAR(SALES_DATE) as YEAR, 
    MONTH(SALES_DATE) as MONTH, 
    COUNT(distinct u.USER_ID) as PURCHASED_USERS, 
    round(COUNT(distinct u.USER_ID)/(
        select  count(u.user_id) 
        from USER_INFO u
        where DATE_FORMAT(u.JOINED, "%Y") = "2021" #분모는 2021가입이면 됨
    ),1) as PUCHASED_RATIO
from ONLINE_SALE o
join USER_INFO u on u.USER_ID = o.USER_ID
where DATE_FORMAT(u.JOINED, "%Y") = "2021"
group by DATE_FORMAT(SALES_DATE, "%Y-%m")
order by 1,2
