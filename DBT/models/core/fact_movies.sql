{{config(materialized='table')}}


with links as
(
select *
from {{ ref('stg_links') }}
),

movies as
(
select *
from {{ ref('stg_movies') }}
),

rating as 
(
select *
from {{ ref('stg_ratings') }}
),

tags as
(
select *
from {{ ref('stg_tags') }}
)

select rating.userId, rating.rating, movies.title, movies.genres, rating.timestamp, tags.user_tag, links.imdbid, links.tmdbid
from rating
inner join movies on rating.movieId = movies.movieId
inner join links on movies.movieId = links.movieId
inner join tags on rating.userId = tags.userId


-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'