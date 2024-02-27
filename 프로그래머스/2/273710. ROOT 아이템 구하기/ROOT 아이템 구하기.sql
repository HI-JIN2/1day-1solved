# -- 코드를 작성해주세요
# select i.ITEM_ID, i.ITEM_NAME
# from item_info i
# inner join ITEM_TREE t
# on i.item_id = t.item_id

select i.ITEM_ID, i.ITEM_NAME
from ITEM_INFO i 
join ITEM_TREE t
on i.ITEM_ID = t.ITEM_ID
where t.PARENT_ITEM_ID is null