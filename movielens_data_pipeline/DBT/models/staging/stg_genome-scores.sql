{{config(materialized='view')}}

with genome_score as
(
select 
    *,
    row_number() over(partition by movieId, tagId) as rn
from 
    {{ source("staging", "genome-scores_external_table")}}
where 
    relevance is not null 
)

select
    cast(movieId as NUMERIC) as movieId,
    cast(tagId as NUMERIC) as tagId,
    cast(relevance as NUMERIC) as relevance
from
    genome_score
where 
    rn = 1



-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}