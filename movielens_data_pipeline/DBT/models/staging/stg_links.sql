{{config(materialized='view')}}

with links as
(
select
    *,
    row_number() over(partition by movieid, imdbid) as rn
from 
    {{ source('staging', 'links_external_table') }}
where
    imdbid is not null
    and
    tmdbid is not null
)

select
    cast(movieid as NUMERIC) as movieId,
    cast(imdbid as NUMERIC) as imdbid,
    cast(tmdbid as NUMERIC) as tmdbid
from 
    links
where
    rn=1


-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}''
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}