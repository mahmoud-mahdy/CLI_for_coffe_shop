{{
    config(
        materialized='view'
    )
}}

with genome_tags as 
(
select 
    *,
    row_number() over(partition by tagid, tag) as rn
from 
    {{ source('staging', 'genome-tags_external_table') }}
where 
    tag is not null 
)

select
    cast(tagid as NUMERIC) as tagid,
    cast(tag as STRING) as tag,

from
    genome_tags
where
    rn = 1

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}