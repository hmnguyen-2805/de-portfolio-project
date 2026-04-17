with pitching as (
    select * from {{ ref('stg_pitching_stats') }}
),

eligible_pitching as (
    select * from pitching
    where innings_pitched >= 10
)

select 
    player_name,
    era,
    strikeouts,
    innings_pitched
from eligible_pitching
order by era asc