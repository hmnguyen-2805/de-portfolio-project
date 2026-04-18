with roster as (
    select * from {{ ref('stg_roster') }}
),

pitching as (
    select * from {{ ref('stg_pitching_stats') }}
),

joined as (
    select 
        r.player_id,
        r.player_name,
        r.player_position,
        p.era,
        p.strikeouts,
        p.innings_pitched,
        {{ classify_workload('p.innings_pitched') }} as pitcher_role
    from roster r
    inner join pitching p
        on r.player_id = p.player_id
)

select * from joined