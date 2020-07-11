# First we will import our packages
import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from nba_api.stats import endpoints
from matplotlib import pyplot as plt

data = endpoints.leagueleaders.LeagueLeaders()
df = data.league_leaders.get_data_frame()
# print(df.head()) 
# print(df.head())

# x variable is player's field goal attempts/ games played
# y varialbe is total points /games played
x, y = df.FGA/df.GP, df.PTS/df.GP

x = np.array(x).reshape(-1,1)     
y = np.array(y).reshape(-1,1)  

model = linear_model.LinearRegression()
model.fit(x,y)

r2 = round(model.score(x,y), 2)            
predicted_y = model.predict(x)  


plt.scatter(x, y, s=15, alpha=.5)                            # Scatterplot:  Specfiy size(s) and transparency(alpha) of dots
plt.plot(x, predicted_y, color = 'black')                    # line: Add line for regression line w/ predicted values
plt.title('NBA - Relationship Between FGA and PPG')          # Give it a title
plt.xlabel('FGA per Game')                                   # Label x-axis
plt.ylabel('Points Per Game')                                # Label y-axis
plt.text(10,25, f'R2={r2}')                                  # 10, 25 are the coordinates for our text. Adjust accordingly


plt.annotate(df.PLAYER[1],                       # This the name of the top scoring player. Refer to the .head() from earlier
             (x[0], y[0]),                       # This is the point we want to annotate.  
             (x[0]-7,y[0]-2),                    # These are coords for the text
             arrowprops=dict(arrowstyle='-'))    # Here we use a flat line for the arrow '-'


# Finally, let's save an image called 'graph.png'. 
# We'll set the dpi (dots per inch) to 300, so we have a nice looking picture.
plt.savefig('graph.png', dpi=300)

plt.show()
