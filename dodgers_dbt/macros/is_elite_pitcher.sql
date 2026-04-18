{% macro is_elite_pitcher(era_column, threshold=3.0) %}
    case
        when {{ era_column }} < {{ threshold }} then 'Elite'
        else 'Not Elite'
    end
{% endmacro %}