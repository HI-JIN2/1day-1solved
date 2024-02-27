-- 코드를 입력하세요
SELECT category, sum(sales) as TOTAL_SALES
from BOOK_SALES s
join BOOK b
on s.BOOK_ID = b.BOOK_ID
where SALES_DATE like "2022-01%"
group by category
order by 1