# NBA FORECAST MODEL: <img src="https://a4.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fmisc_logos%2F500%2Fnba.png" width="300" height="300"/>

Creates and develops from scratch a data-mining pipeline that utilizes the NBA API to deploy a linear regression and decision tree model for NBA game predictions

## Data Mining: 

Data Mining: data mining is defined as a process used to extract usable data from a larger set of any raw data.
### getData
By utilzing the NBA API, my model retrieves a particular NBA season's data for each team and places it into a pandas dataframe with respective stats for each game played. Attributes include:  

    - SEASON_ID,	TEAM_ID, TEAM_ABBREVIATION,	TEAM_NAME,	GAME_ID,	GAME_DATE,	MATCHUP,	WL,	MIN,	PTS,	FGM, FGA,	FG_PCT,	FG3M,	FG3A,	FG3_PCT,	FTM,	FTA,	FT_PCT,	OREB,	DREB,	REB,	AST,	STL,	BLK,	TOV,	PF,	PLUS_MINUS

For organization purposes, my model exports this as a csv for further reference. 

## Feature Engineering: 

Feature engineering: the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.

### findAvgs
This function, essentially, calculates the rolling averages for each feature for each team by filtering out the "noise" from the dataset. As a result, I create a csv file with all features which calcuates the average from the past ten games for a particular team.

### combine_Teams
Combines rows for teams that play against each other and sorts the rows based on game date
This portion utilizes the csv created in findAvgs and joins games based on the primary key of GAME_ID. I, then, delete all duplicates to eliminate redundancy. As a result I create another pandas dataframe with each game played along with their opponent and export it as a csv.

TEAM_ID_A	TEAM_ABBREVIATION_A	TEAM_NAME_A	GAME_ID	GAME_DATE	MATCHUP_A	WL_A	MIN_A	AV_PTS_A	AV_FGM_A	...	AV_FT_PCT_B	AV_OREB_B	AV_DREB_B	AV_REB_B	AV_AST_B	AV_STL_B	AV_BLK_B	AV_TOV_B	AV_PF_B	AV_PLUS_MINUS_B
2281	1610612766	CHA	Charlotte Hornets	21900909	2020-03-03	CHA vs. SAS	L	240	97.2	35.7	...	0.8024	8.0	32.0	40.0	24.2	8.0	4.2	10.6	18.7	-8.3

### get_zscores
Calculates zscores for each team + fits data to linear regression and decision tree model
This portion calculates the zscores for each team by subtracting the rolling average for one team from their opponent. As a result, we get a standardized score relative to the two opponents. Then, I use the created dataframe to fit the data to a linear regression and a decision tree model by making use of sklearn's libraries.

## Model: currently have a model that operates better than random and what we want to do in the future
### Data Visualization


