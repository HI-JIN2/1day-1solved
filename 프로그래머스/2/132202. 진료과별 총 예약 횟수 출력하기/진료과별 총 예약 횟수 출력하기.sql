-- 코드를 입력하세요
SELECT MCDP_CD as "진료과코드", count(*) as "5월예약건수"
from APPOINTMENT
where year(APNT_YMD)= 2022 and month(APNT_YMD) =5
group by 1
order by 2,1

# SELECT MCDP_CD "진료과 코드",
# COUNT(*) "5월예약건수"
# FROM APPOINTMENT
# WHERE YEAR(APNT_YMD) = 2022 and MONTH(APNT_YMD) = 5
# GROUP BY 1
# ORDER BY 2, 1