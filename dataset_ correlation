import pandas as pd
from random import uniform

load = pd.read_csv("zoo_data-1.csv.xls")
data_value = [row[1:] for row in load.values]
def classify(row, weights):
    
    sum=weights[-1]
    for i in range(len(row)-1):
        sum += row[i]*weights[i]
    
    if(sum>=0):
        return 1
    else:
        return 0
 
def train(train_data, n_epoch, l_rate):
    num = 0 
    correct = 0
    weight = [uniform(-1, 1)]
    
    for i in range(len(train_data[0])-1):
        weight.append(uniform(-1,1))
    
    for j in range(n_epoch):
        for k in range(len(train_data)):
            
            num = classify(train_data[k],weight)
            
            if num!=train_data[k][-1]:
                for l in range(len(weight)-1):
                    
                    weight[l] = weight[l]+l_rate*(train_data[k][-1]-num) * train_data[k][l]
                weight[-1] = weight[-1]+(train_data[k][-1]-num)
                
            else:
                correct +=1
        if (j == n_epoch-1):
            return int(correct/len(train_data)*100)
        
        correct = 0
correlation = train(data_value, 100, 1)
if (correlation > 50):
    if(correlation > 70):
        print("Strong Correlation", correlation,"%")
    else:
        print("Week Correlation", correlation,"%")
else:
    print("No Correlation", correlation, "%")
    
for r in data_value:
    print(r)
