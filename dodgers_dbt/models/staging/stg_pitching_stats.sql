with source as (
    select * from {{ source('main', 'pitching_stats') }}
),

renamed as (
    select
        player_id       as player_id,
        name            as player_name,
        innings_pitched as innings_pitched,
        strikeouts      as strikeouts,
        era             as era
    from source
)

select * from renamed