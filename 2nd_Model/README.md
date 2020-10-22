# NBA FORECAST MODEL:  ![Alt Text](https://a4.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fmisc_logos%2F500%2Fnba.png)![drawing](drawing.jpg)

Creates and develops from scratch a data-mining pipeline that utilizes the NBA API to deploy a linear regression and decision tree model for NBA game predictions

## Data Mining:
Data Mining: data mining is defined as a process used to extract usable data from a larger set of any raw data.
### getData
By utilzing the NBA API, my model retrieves a particular NBA season's data for each team and places it into a pandas dataframe with respective stats for each game played. Attributes include:  
    - SEASON_ID,	TEAM_ID, TEAM_ABBREVIATION,	TEAM_NAME,	GAME_ID,	GAME_DATE,	MATCHUP,	WL,	MIN,	PTS,	FGM, FGA,	FG_PCT,	FG3M,	FG3A,	FG3_PCT,	FTM,	FTA,	FT_PCT,	OREB,	DREB,	REB,	AST,	STL,	BLK,	TOV,	PF,	PLUS_MINUS

For organization purposes, my model exports this as a csv for further reference. 

## Feature Engineering:
definition of feature engineering and how it applies

Feature engineering: the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.


### findAvgs
Finds the ten day rolling average for each team for each game in each attribute

### combine_Teams
Combines rows for teams that play against each other and sorts the rows based on game date

### get_zscores
Calculates zscores for each team + fits data to linear regression and decision tree model

## Model: currently have a model that operates better than random and what we want to do in the future
### Data Visualization


