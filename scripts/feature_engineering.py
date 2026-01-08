import pandas as pd

matches_long = pd.read_csv("data/processed/processed.csv")
matches_long['date'] = pd.to_datetime(matches_long['date'])

matches_long["avg_goals_last_5"] = (
    matches_long.groupby("team")["team_score"]
    .transform(lambda x: x.rolling(window=5, min_periods=1).mean().shift(1))
)
matches_long["win_rate_last_5"] = (
    matches_long.groupby("team")["win"]
    .transform(lambda x: x.rolling(window=5, min_periods=1).mean().shift(1))
)
matches_long["avg_goals_conceded_last_5"] = (
    matches_long.groupby("team")["opponent_score"]
    .transform(lambda x: x.rolling(window=5, min_periods=1).mean().shift(1))
)
matches_long["goal_diff"] = (
    matches_long["team_score"] - matches_long["opponent_score"]
)
matches_long["avg_goal_diff_last_5"] = (
    matches_long.groupby("team")["goal_diff"]
    .transform(lambda x: x.rolling(window=5, min_periods=1).mean().shift(1))
)

matches_long = matches_long.sort_values(by=['date', 'team'])
matches_long.to_csv('./data/features/team_features.csv', index=False)