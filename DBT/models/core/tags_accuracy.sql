{{config(materialized='table')}}

with genome_scores as
(
select *
from {{ ref('stg_genome-scores') }}
),

genome_tags as
(
select *
from {{ ref('stg_genome-tags') }}
),

movies as
(
select *
from {{ ref('stg_movies') }}
)

select movies.title, gt.tag, gs.relevance
from genome_scores gs 
inner join genome_tags gt on gs.tagId = gt.tagId
inner join movies on gs.movieId = movies.movieId
