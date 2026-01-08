import pandas as pd

df = pd.read_csv('./data/raw/results.csv')

df['date'] = pd.to_datetime(df['date'])
df = df[df['date'] >= '2010-01-01']

df['home_win'] = (df['home_score'] > df['away_score']).astype(int)

df = df.dropna(subset=["home_score", "away_score", "home_team", "away_team"])

home = df[['date', 'home_team', 'away_team', 'home_score', 'away_score', 'home_win', "neutral"]].copy()
home.columns = ['date', 'team', 'opponent', 'team_score', 'opponent_score', 'win', "neutral"]

away = df[[
    "date", "away_team", "home_team",
    "away_score", "home_score", "home_win", "neutral"
]].copy()
away.columns = ["date", "team", "opponent", "team_score", "opponent_score", "win", "neutral"]
away["win"] = (away["team_score"] > away["opponent_score"]).astype(int)

matches_long = pd.concat([home, away], ignore_index=True)
matches_long = matches_long.sort_values(by=['date', 'team'])
matches_long.dropna(inplace=True)
matches_long.to_csv('./data/processed/processed.csv', index=False)