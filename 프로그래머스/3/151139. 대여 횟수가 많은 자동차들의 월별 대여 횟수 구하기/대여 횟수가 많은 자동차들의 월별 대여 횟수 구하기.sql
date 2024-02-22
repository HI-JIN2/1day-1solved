# select month(START_DATE) as month, CAR_ID, count(HISTORY_ID) as record
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where (DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10')
# group by car_id
# having count(HISTORY_ID)>=5
# order by 1, 2 desc
select month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE between '2022-08-01' and '2022-10-31'
and CAR_ID in (select CAR_ID
               from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where START_DATE between '2022-08-01' and '2022-10-31'
               group by CAR_ID
               having count(CAR_ID) >= 5
              )
group by 1, 2
having RECORDS > 0
order by 1, 2 desc
