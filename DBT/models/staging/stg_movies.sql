{{config(materialized='view')}}


with movies as
(
select
    *,
    row_number() over(partition by movieid, title) as rn
from
    {{ source('staging', 'movies_external_table') }}
where
    title is not null
    and 
    genres is not null
)


select
    cast(movieid as NUMERIC) as movieId,
    --spliting relase year from movie title
    cast(REGEXP_REPLACE(title, '\\s*\\((\\d{4})\\)', '') as STRING) AS title,
    cast(REGEXP_SUBSTR(title, '\\((\\d{4})\\)') as INT) AS movie_release_year,
    cast(genres as STRING) as genres
from
    movies
where  
    rn = 1

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
