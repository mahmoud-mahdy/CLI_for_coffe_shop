{{
    config(
        materialized='view'
    )
}}


with tags as

(
select
    *,
    row_number() over(partition by userid, movieid ) as rn
from
    {{ source('staging', 'tags_external_table') }}
where
    tag is not null
)


select
    cast(userid as numeric) as userId,
    cast(movieid as numeric) as movieId,
    cast(tag as STRING) as user_tag,
    timestamp_seconds(timestamp) as timestamp
from
    tags
where
    rn = 1

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}''
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}