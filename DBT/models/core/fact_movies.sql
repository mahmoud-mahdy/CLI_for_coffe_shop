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

-- removing all movies with less than 20 reviews (unreliable data)
rating_transformation as
(SELECT
    movieId,
    count(rating) as review_count
FROM rating

GROUP BY movieId

HAVING COUNT(rating.rating) >= 20
ORDER BY review_count
)

select rating.movieId, rating.userId, rating.rating, movies.title as Movie_title, movies.movie_release_year, movies.genres, Rating.timestamp as rating_time,  
links.imdbid, links.tmdbid

from rating

inner join movies on rating.movieId = movies.movieId
left join links on movies.movieId = links.movieId
inner join rating_transformation on rating_transformation.movieId = rating.movieId

where 
    -- removing all moves doesnt have title or release year (all remaining moves have both title and release year)
    movies.title != ''
    and
    movies.movie_release_year is not null


-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'