select id, ni.FISH_NAME, LENGTH
from FISH_NAME_INFO ni
join(
    select id, i.FISH_TYPE, f.LENGTH
    from FISH_INFO i
    right join (
        select FISH_TYPE, max(LENGTH) as LENGTH
        from FISH_INFO
        group by FISH_TYPE) 
    f on i.FISH_TYPE =f.FISH_TYPE and i.LENGTH  =f.LENGTH) 
    p on ni.FISH_TYPE = p.FISH_TYPE
