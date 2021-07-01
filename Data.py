# importing important modules
import statistics as st
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go


# finding the mean of population data
# plotting the population data on a graph
df = pd.read_csv("medium_data.csv")
time = df["reading_time"].tolist()
mean = st.mean(time)
print(mean)
fig_population = ff.create_distplot(
    [time],["reading time"], show_hist= False
)
fig_population.show()

# taking samples of random values
# finding the mean of the sample
def random_set_of_mean(counter):
    sample = []
    for i in range(1,counter):
        random_index = random.randint(0,len(time)-1)
        value = time[random_index]
        sample.append(value)

    mean_sample = st.mean(sample)
    return mean_sample

# plotting the sample on a graph
def show_fig(mean_list):
    df_sample = mean_list
    fig_sample = ff.create_distplot(
        [df_sample], ["mean of the sample"], show_hist= False
    )
    fig_sample.show()
    mean_sample = st.mean(mean_list)
    print(mean_sample)

# calling all the functions
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()
