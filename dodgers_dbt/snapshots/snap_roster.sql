{% snapshot snap_roster %}

{{
    config(
        target_schema='main',
        unique_key='player_id',
        strategy='check',
        check_cols=['player_position']
    )
}}

select
    player_id,
    player_name,
    player_position
from {{ ref('stg_roster') }}

{% endsnapshot %}