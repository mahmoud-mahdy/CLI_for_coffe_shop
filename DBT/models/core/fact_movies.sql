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

select rating.userId, rating.rating, movies.title as Movie_title, movie_release_year, movies.genres, Rating.timestamp as rating_time, tags.user_tag, 
links.imdbid, links.tmdbid


from rating
left join movies on rating.movieId = movies.movieId
left join links on movies.movieId = links.movieId
left join tags on rating.userId = tags.userId

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'