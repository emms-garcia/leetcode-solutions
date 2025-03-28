WITH scores AS (
    SELECT
        player_id,
        SUM(score) AS score
    FROM
        matches
    UNPIVOT (
        (player_id, score) FOR column IN (
            (first_player, first_score),
            (second_player, second_score)
        )  
    )
    GROUP BY player_id
),    
tournament_ranks AS (
    SELECT
        group_id,
        player_id,
        RANK() OVER (PARTITION BY group_id ORDER BY score DESC, player_id ASC) AS rank
    FROM
        scores
    JOIN
        players USING (player_id)
)
            
SELECT
    group_id,
    player_id
FROM
    tournament_ranks
WHERE
    rank = 1