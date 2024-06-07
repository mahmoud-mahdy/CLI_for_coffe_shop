with genome_score as

(
    select *,
    row_number() over(partition by movieid, tagid ) as rn
    from {{ source('staging', 'genome-scores_external_table') }}
    where movieid is not null
)

select 

    cast(movieid as numeric),
    cast(tagid as numeric),
    cast(relevance as float)
from genome_score
where rn = 1

-- {% if var('is_test_run', default=true) %}

--   limit 100

-- {% endif %}