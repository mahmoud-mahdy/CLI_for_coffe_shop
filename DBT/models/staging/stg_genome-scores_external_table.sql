with 

source as (

    select * from {{ source('staging', 'genome-scores_external_table') }}

),

renamed as (

    select
        movieid,
        tagid,
        relevance

    from source

)

select * from renamed
