select m.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE m 
join REST_REVIEW r  on r.MEMBER_ID = m.MEMBER_ID
where m.MEMBER_ID = ( select MEMBER_ID
      from REST_REVIEW 
      group by MEMBER_ID
      order by count(REVIEW_ID) desc
      limit 1
)
order by 3, 2
# select MEMBER_ID, count(REVIEW_ID)
#       from REST_REVIEW 
#       group by MEMBER_ID
#       order by count(REVIEW_ID) desc
#       limit 1