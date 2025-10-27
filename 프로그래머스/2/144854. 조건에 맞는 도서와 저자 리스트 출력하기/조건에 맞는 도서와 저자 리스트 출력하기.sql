select b.BOOK_ID, a.AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from book as  b
join author as a on a.AUTHOR_ID = b.AUTHOR_ID
where b.CATEGORY = "경제"
order by PUBLISHED_DATE