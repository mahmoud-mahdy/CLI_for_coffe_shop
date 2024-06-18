{{
    config(
        materialized='view'
    )
}}

with ratings as
(
select 
    *,
    row_number() over (partition by userid, movieid) as rn
from
    {{ source('staging', 'ratings_external_table') }}
where 
    rating is not null
)

select
    cast(userid as NUMERIC) as userId,
    cast(movieid as NUMERIC) as movieId,
    cast(rating as NUMERIC) as rating,
    timestamp_seconds(timestamp) AS timestamp

from 
    ratings
where
    rn = 1



-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}''
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}