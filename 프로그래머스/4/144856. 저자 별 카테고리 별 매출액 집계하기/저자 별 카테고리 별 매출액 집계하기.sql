-- 코드를 입력하세요
select j.AUTHOR_ID, j.AUTHOR_NAME,j.CATEGORY, sum(TOTAL_SALES)
from (
    select b.AUTHOR_ID, AUTHOR_NAME,CATEGORY,sales*price as TOTAL_SALES
    from BOOK_SALES s
    left join BOOK b
    on s.BOOK_ID = b.BOOK_ID
    join AUTHOR a
    on a.AUTHOR_ID=b.AUTHOR_ID
    where SALES_DATE like "2022-01%"
    ) as j 

group by b.author_id,category
order by 1 asc ,3 desc