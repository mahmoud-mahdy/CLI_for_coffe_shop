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

links as
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

select
    gs.movieId,
    gt.tag,
    gs.relevance
from
    genome_scores gs
right join
    genome_tags gt on gs.tagId = gt.tagId

-- dbt build --select <model.sql> --vars '{'is_test_run': 'false'}'