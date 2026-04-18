{% macro classify_workload(innings_pitched, threshold=50.0) -%}
    case
        when {{ innings_pitched }} < {{ threshold }} then 'Reliever'
        else 'Starter'
    end
{%- endmacro %}