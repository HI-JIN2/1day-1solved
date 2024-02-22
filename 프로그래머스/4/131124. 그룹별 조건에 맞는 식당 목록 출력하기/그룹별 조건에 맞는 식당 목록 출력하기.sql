select m.MEMBER_NAME,r.REVIEW_TEXT, date_format(r.REVIEW_DATE,"%Y-%m-%d")as REVIEW_DATE
from MEMBER_PROFILE m,REST_REVIEW r 
where m.member_id = r.member_id
    and  m.member_id = (select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(*) desc
    limit 1)
order by r.REVIEW_DATE, r.REVIEW_DATE

# (select MEMBER_ID, count(*)
#     from REST_REVIEW
#     group by MEMBER_ID
#     order by count(*) desc
#     limit 1)

# SELECT p.member_name 멤버명, r.review_text 리뷰, DATE_FORMAT(r.review_date, '%Y-%m-%d') 리뷰작성일
# FROM member_profile p, rest_review r
# WHERE p.member_id = r.member_id
#       AND p.member_id = (SELECT r.member_id
#                         FROM rest_review r
#                         GROUP BY r.member_id
#                         ORDER BY COUNT(*) DESC
#                         LIMIT 1)
# ORDER BY 리뷰작성일, 리뷰;