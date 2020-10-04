import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model

def ProcessData():
    # sold, available, COGS, retail price of inv, cost, MSRP
    #ToBeProcessed1 = np.loadtxt('ToBeProcessed1.csv', delimiter=',')
    ToBeProcessed2 = np.loadtxt('DataSets/ToBeProcessed2.csv', delimiter=',', skiprows=1)
    Processed2 = []
    for data in ToBeProcessed2:
        if (data[4] < data[5]):
            Processed2.append(data)

    np.savetxt('DataSets/Processed2.csv', Processed2, delimiter=',')



if __name__ == '__main__':
    #ProcessData()
    # sales, label, cost, MSRP, month, mon, tues, wed, thurs, fri, sat, sun
    data = pd.read_csv("DataSets\ForUse2.csv",sep = ',')
    #print(data)
    data = data[['sales','label','cost','msrp','month','mon','tues','wed','thurs','fri','sat','sun']]
    predict = 'label'

    x = np.array(data.drop([predict],1))
    y = np.array(data[[predict]])

    x_train, x_test, y_train, y_test= sklearn.model_selection.train_test_split(x,y,test_size = 0.1)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test,y_test)
    print(acc)

    predictions = linear.predict(x_test)

    for x in range(len(predictions)):
        print((int) (predictions[x]),x_test[x],y_test[x])







