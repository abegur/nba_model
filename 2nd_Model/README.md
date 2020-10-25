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

Dataframe: 

    - SEASON_ID	TEAM_ID	TEAM_ABBREVIATION	TEAM_NAME	GAME_ID	GAME_DATE	MATCHUP	WL	MIN	PTS	...	AV_FT_PCT	AV_OREB	AV_DREB	AV_REB	AV_AST	AV_STL	AV_BLK	AV_TOV	AV_PF	AV_PLUS_MINUS
    2619	22017	1610612766	CHA	Charlotte Hornets	21701143	2018-04-01	CHA vs. PHI	L	240	102	...	0.7810	10.6	38.5	49.1	21.0	6.2	3.9	12.0	14.8	2.4

### combine_Teams
This portion utilizes the csv created in findAvgs and joins games based on the primary key of GAME_ID. I, then, delete all duplicates to eliminate redundancy. As a result I create another pandas dataframe with each game played along with their opponent and export it as a csv.

Dataframe: 

    - TEAM_ID_A	TEAM_ABBREVIATION_A	TEAM_NAME_A	GAME_ID	GAME_DATE	MATCHUP_A	WL_A	MIN_A	AV_PTS_A	AV_FGM_A	...	AV_FT_PCT_B	AV_OREB_B	AV_DREB_B	AV_REB_B	AV_AST_B	AV_STL_B	AV_BLK_B	AV_TOV_B	AV_PF_B	AV_PLUS_MINUS_B
    2281	1610612766	CHA	Charlotte Hornets	21900909	2020-03-03	CHA vs. SAS	L	240	97.2	35.7	...	0.8024	8.0	32.0	40.0	24.2	8.0	4.2	10.6	18.7	-8.3

### get_zscores
This portion calculates the zscores for each team by subtracting the rolling average for one team from their opponent. 

```for column in z_data.columns[1:]:
    z_data[column] = data['AV_' + column + '_A'] - data['AV_' + column + '_B']
```

As a result, we get a standardized score relative to the two opponents. Then, I use the created dataframe to fit the data to a linear regression and a decision tree model by making use of sklearn's libraries.

Dataframe: 

    - 	WL	PTS	FGM	FGA	FG_PCT	FG3M	FG3A	FG3_PCT	FTM	FTA	FT_PCT	OREB	DREB	REB	AST	STL	BLK	TOV	PF	PLUS_MINUS
    146	0.0	-15.100000000000000	-1.6000000000000000	-1.7000000000000000	-0.006200000000000090	-4.900000000000000	-12.300000000000000	-0.01420000000000000	-7.0	    -7.300000000000000	-0.04819999999999990	-0.7000000000000010	-1.5	-2.2000000000000000	-0.8000000000000010	1.2000000000000000	-0.5	        -2.700000000000000	0.0	0.8

## Model:
Currently: Have a model that operates better than random 
Logistic Regression: 

    - Coefficient Information:
    PTS: 0.11508870418272563
    FGM: -0.09514096621197392
    FGA: -0.12218154180465549
    FG3_PCT: -1.0604111394379243
    FTA: -0.09085012100683548
    REB: 0.1284208148426271
    AST: -0.006881641759073735
    STL: 0.14569096540116291
    TOV: -0.10956681097691838
    ----------------------------------
    Accuracy: 0.6157575757575757
    Precision: 0.6473779385171791
    Recall: 0.7458333333333333
    ----------------------------------
    Confusion Matrix:
    [[150 195]
    [122 358]]
    
Decision Tree: 

    - 0.5975757575757575
          L    W
    True L  136  211
    True W  121  357

    
Future: Create a function that determines which teams are playing today and give the probability of the home team winning based on the above features. 
### Data Visualization


