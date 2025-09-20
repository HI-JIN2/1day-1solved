-- 코드를 작성해주세요
select count(id) as COUNT
from ecoli_data
where genotype & 2 =0 
and (genotype & 4 >=1 
or genotype & 1 >=1)