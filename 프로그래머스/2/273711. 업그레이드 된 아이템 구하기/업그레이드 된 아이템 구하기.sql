-- 코드를 작성해주세요

# select i.ITEM_ID,	ITEM_NAME,	RARITY
# from ITEM_INFO i 
# join ITEM_TREE t
# on i.ITEM_ID = t.ITEM_ID
# where t.PARENT_ITEM_ID is not null and 
# i.RARITY = "RARE"
# order by i.ITEM_ID desc



# where t.PARENT_ITEM_ID in 
select i.ITEM_ID,i.ITEM_NAME,i.RARITY
from ITEM_INFO i
join ITEM_TREE t
on i.ITEM_ID = t.ITEM_ID
where t.PARENT_ITEM_ID in (select ITEM_ID from ITEM_INFO where RARITY="RARE")
order by ITEM_ID desc


# # (
# select distinct PARENT_ITEM_ID
# from ITEM_TREE 
# where PARENT_ITEM_ID is not null 
# RARITY = "RARE")

# select distinct PARENT_ITEM_ID
# from ITEM_TREE 
# where PARENT_ITEM_ID is not null