-- 코드를 작성해주세요
select ITEM_ID,	ITEM_NAME,	RARITY
from ITEM_INFO
where item_id not in 
    (select distinct PARENT_ITEM_ID
    from ITEM_TREE
    where PARENT_ITEM_ID is not null)
order by ITEM_ID desc 

# select distinct PARENT_ITEM_ID
# from ITEM_TREE
# where PARENT_ITEM_ID is not null

# t.PARENT_ITEM_ID is not null and 
# i.item_id not in t.PARENT_ITEM_ID
# 부모가 아닌 것 