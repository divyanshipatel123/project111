import pandas as pd
import csv 
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go 
import random
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_SD = statistics.stdev(data)

def randomSetOfMeans(counter):
    dataset = []
    for i in range(0 , counter):
        randIndex = random.randint(0 , len(data) - 1)
        val = data[randIndex]
        dataset.append(val)
    mean = statistics.mean(dataset)
    return mean

meanList = []

for i in range(0,100):
    setOfmeans = randomSetOfMeans(30)
    meanList.append(setOfmeans)

mean_Sample_dist = statistics.mean(meanList)
sd_Sample_dist = statistics.stdev(meanList)
print(mean_Sample_dist , "mean of the sampling distribution")
print(sd_Sample_dist, "standard deviation of the sampling distribution")


fig = ff.create_distplot([meanList] , ["reading time of the articles"] , show_hist= False)


start_sd1 , end_sd1 = mean_Sample_dist - sd_Sample_dist , mean_Sample_dist + sd_Sample_dist
start_sd2 , end_sd2 = mean_Sample_dist - (sd_Sample_dist*2) , mean_Sample_dist + (sd_Sample_dist *2)
start_sd3 , end_sd3 = mean_Sample_dist - (sd_Sample_dist*3) , mean_Sample_dist + (sd_Sample_dist *3)
print(start_sd1 , end_sd1 , " first sd /n" , start_sd2,end_sd2,"second sd/n" , start_sd3 , end_sd3 , "third sd /n")

#Takin the intervention data
df2 = pd.read_csv("sample_2.csv")
data2 = df2["reading_time"].tolist()

mean_new_Sample = statistics.mean(data2)
sd_new_Sample = statistics.stdev(data2)
print("mean of the of the new sample : " , mean_new_Sample)
print("Standard deviation of the of the new sample : " , sd_new_Sample)

#Tracing the 1st 2nd and 3rd standard deviations on the graph
fig.add_trace(go.Scatter(x = [start_sd1 , start_sd1] , y = [0 , 0.6] , mode = 'lines' , name = "First sd"))
fig.add_trace(go.Scatter(x = [end_sd1 , end_sd1] , y = [0 , 0.6] , mode = 'lines' , name = "First +sd"))
fig.add_trace(go.Scatter(x = [start_sd2 , start_sd2] , y = [0 , 0.6] , mode = 'lines' , name = "Second sd"))
fig.add_trace(go.Scatter(x = [end_sd2 , end_sd2] , y = [0 , 0.6] , mode = 'lines' , name = "First +sd"))
fig.add_trace(go.Scatter(x = [start_sd3 , start_sd3] , y = [0 , 0.6] , mode = 'lines' , name = "third sd"))
fig.add_trace(go.Scatter(x = [end_sd3 , end_sd3] , y = [0 , 0.6] , mode = 'lines' , name = "third +sd"))
#tracing the mean of the sampling distribution
fig.add_trace(go.Scatter(x = [mean_Sample_dist , mean_Sample_dist] ,y = [0 , 0.6] , mode = "lines" , name = "mean"))
#tracing the mean of the new sample
fig.add_trace(go.Scatter(x = [mean_new_Sample , mean_new_Sample] , y = [0 , 0.6] , mode = "lines" , name = "mean of new sample"))

#calculate the Z score
Z_Score = (mean_new_Sample - mean_Sample_dist)/ sd_Sample_dist
print("Z score of the data is : " , Z_Score)

fig.show()