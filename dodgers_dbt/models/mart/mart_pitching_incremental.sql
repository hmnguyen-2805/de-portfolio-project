{{ config(materialized='incremental', unique_key='player_id') }}

with source as (
    select 
        player_id,
        player_name,
        era,
        strikeouts,
        innings_pitched,
        {{ is_elite_pitcher('era') }} as elite_status
    from {{ ref('stg_pitching_stats') }}

    {% if is_incremental() -%}
        where player_id not in (select player_id from {{ this }})
    {%- endif %}
)

select * from source