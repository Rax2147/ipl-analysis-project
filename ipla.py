import numpy as numpy
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt



ndf = pd.read_csv("C:\\Users\\raks2\\Downloads\\data.csv")
print(ndf)



# Matches won by each team
win_count_df = pd.DataFrame(ndf["winner"].value_counts())
win_count_df.reset_index(inplace=True)
print(win_count_df)
fig_01 = px.bar(data_frame=win_count_df, x="winner", y="count", title="No. of Matches Won by each Franchise", labels={"count":"Matches Won", "winner":"Team"}, color="count")
fig_01.update_layout(xaxis_title = "Franchise", yaxis_title = "Matches Won")
fig_01.show()


# Matches won by chasing or defending
won_chasing = len(ndf.loc[(ndf["win_by_wickets"]!= 0)].index)
won_defending = len(ndf.loc[(ndf["win_by_runs"]!= 0)].index)
won_method_df = pd.DataFrame({"Matches Won": [won_chasing, won_defending], "Won by":["Won by Chasing", "Won by Defending"]})
print(won_method_df)
fig_02 = px.pie(data_frame=won_method_df, values="Matches Won", names="Won by", color_discrete_sequence=px.colors.sequential.Electric_r, title="Matches won by chasing and defending")
fig_02.show()




#no. of man of match
mom_win_df = pd.DataFrame(ndf["player_of_match"].value_counts())
mom_win_df.reset_index(inplace = True, names = ["Player Name", "momwon"])
print(mom_win_df)
fig_03 = px.scatter(data_frame=mom_win_df, x = "Player Name", y = "count", title="Most Man of the Match Awards", size="count", color="Player Name", labels={"count":"Man of the Match Awards Won"})
fig_03.update_layout(xaxis_title = "Player Name", yaxis_title = "Mom won")
fig_03.show()



# no of times teams won at home 
team_names = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Rajasthan Royals", "Kolkata Knight Riders", "Kings XI Punjab","Delhi Daredevils", "Sunrisers Hyderabad" ]
mat_won_at_home = [ len(ndf.loc[(ndf["city"]=="Mumbai") & (ndf["winner"] == "Mumbai Indians")].index),len(ndf.loc[(ndf["city"]=="Chennai") & (ndf["winner"] == "Chennai Super Kings")].index),len(ndf.loc[(ndf["city"]=="Bangalore") & (ndf["winner"] == "Royal Challengers Bangalore")].index), len(ndf.loc[(ndf["city"]=="Jaipur") & (ndf["winner"] == "Rajasthan Royals")].index), 
len(ndf.loc[(ndf["city"]=="Kolkata") & (ndf["winner"] == "Kolkata Knight Riders")].index),len(ndf.loc[(ndf["city"]=="Chandigarh") & (ndf["winner"] == "Kings XI Punjab")].index), 
len(ndf.loc[(ndf["city"]=="Delhi") & (ndf["winner"] == "Delhi Daredevils")].index),len(ndf.loc[(ndf["city"]=="Hyderabad") & (ndf["winner"] == "Sunrisers Hyderabad")].index)]
print(team_names)
print(mat_won_at_home)
won_at_home_df = pd.DataFrame({"Team" : team_names, "Matches Won" : mat_won_at_home})
print(won_at_home_df)
fig_04 = px.bar(data_frame=won_at_home_df, x = "Team", y="Matches Won", title = "Matches won by teams at home", color_discrete_sequence=px.colors.sequential.Burgyl)
fig_04.update_layout(xaxis_title = "Team", yaxis_title = "Matches Won")
fig_04.show()














