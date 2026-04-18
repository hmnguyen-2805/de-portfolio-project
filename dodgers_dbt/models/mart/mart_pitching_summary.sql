with pitching as (
    select * from {{ ref('stg_pitching_stats') }}
),

eligible_pitching as (
    select * from pitching
    where innings_pitched >= {{ var('min_innings_pitched') }}
)

select
    player_name,
    era,
    strikeouts,
    innings_pitched,
    {{ is_elite_pitcher('era') }} as elite_status
from eligible_pitching
order by era asc