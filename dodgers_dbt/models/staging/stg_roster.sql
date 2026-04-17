with source as (
    select * from {{ source('main', 'roster')}}
),

renamed as (
    select
        player_id,
        name        as player_name,
        position    as player_position
    from source
)

select * from renamed