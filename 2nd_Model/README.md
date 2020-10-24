# NBA FORECAST MODEL: <img src="https://a4.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fmisc_logos%2F500%2Fnba.png" width="300" height="300"/>

Creates and develops from scratch a data-mining pipeline that utilizes the NBA API to deploy a linear regression and decision tree model for NBA game predictions

## Data Mining: <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.promptcloud.com%2Fblog%2Fweb-mining-tools%2F&psig=AOvVaw30S8lzqJZ_FfGX6dCKA7iA&ust=1603660180648000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPDeoe-RzuwCFQAAAAAdAAAAABAD" width="300 height="200/>

Data Mining: data mining is defined as a process used to extract usable data from a larger set of any raw data.
### getData
By utilzing the NBA API, my model retrieves a particular NBA season's data for each team and places it into a pandas dataframe with respective stats for each game played. Attributes include:  

    - SEASON_ID,	TEAM_ID, TEAM_ABBREVIATION,	TEAM_NAME,	GAME_ID,	GAME_DATE,	MATCHUP,	WL,	MIN,	PTS,	FGM, FGA,	FG_PCT,	FG3M,	FG3A,	FG3_PCT,	FTM,	FTA,	FT_PCT,	OREB,	DREB,	REB,	AST,	STL,	BLK,	TOV,	PF,	PLUS_MINUS

For organization purposes, my model exports this as a csv for further reference. 

## Feature Engineering: <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Ftowardsdatascience.com%2Ffeature-engineering-what-powers-machine-learning-93ab191bcc2d&psig=AOvVaw1fru5zEQLywAhZ3n0QA83X&ust=1603660254187000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKjqtpOSzuwCFQAAAAAdAAAAABAD" width="300 height="200/>

Feature engineering: the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.

### findAvgs
This function, essentially, calculates the rolling averages for each feature for each team by filtering out the "noise" from the dataset. As a result, I create a csv file with all features which calcuates the average from the past ten games for a particular team.

### combine_Teams
Combines rows for teams that play against each other and sorts the rows based on game date
This portion utilizes the csv created in findAvgs and joins games based on the primary key of GAME_ID. I, then, delete all duplicates to eliminate redundancy. As a result I create another pandas dataframe with each game played along with their opponent and export it as a csv.

### get_zscores
Calculates zscores for each team + fits data to linear regression and decision tree model
This portion calculates the zscores for each team by subtracting the rolling average for one team from their opponent. As a result, we get a standardized score relative to the two opponents. Then, I use the created dataframe to fit the data to a linear regression and a decision tree model by making use of sklearn's libraries.

## Model: currently have a model that operates better than random and what we want to do in the future
### Data Visualization


