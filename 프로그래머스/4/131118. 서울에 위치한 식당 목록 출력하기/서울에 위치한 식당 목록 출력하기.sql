-- 코드를 입력하세요
# SELECT * 
# from REST_INFO i
# join REST_REVIEW r
# on 

select i.REST_ID,i.REST_NAME,i.FOOD_TYPE,i.FAVORITES,i.ADDRESS,j.SCORE
from REST_INFO i
join (select REST_ID,round(avg(REVIEW_SCORE),2) as SCORE
from REST_REVIEW r
group by REST_ID
) as j 
on i.REST_ID = j.REST_ID
where ADDRESS like "서울%"
order by j.score desc, i.FAVORITES desc
