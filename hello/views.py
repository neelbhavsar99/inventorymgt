from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Greeting, TrainingModel, StoreData
from .forms import GreetingForm, StoreDataForm
from django.http import HttpResponse, HttpResponseRedirect
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from django.db import connection
from django.db.models.query import QuerySet


# Create your views here.
def index(request):
    monthinput = 1
    form = StoreDataForm()
    if request.method == 'POST':
        form = StoreDataForm(request.POST)
        #print("hi", request.POST)
        #monthVal = request.POST
        if form.is_valid():
            ###form.get()
            #form.save()
            #messages.info(request, 'Successfully verified!')
            print(form.cleaned_data['month'])
            monthinput = form.cleaned_data['month']
            print(monthinput)
        else:
            form = StoreDataForm()

    # ------------------ #
    #if __name__ == '__main__':
    # sales, label, cost, MSRP, month, mon, tues, wed, thurs, fri, sat, sun
    #data = pd.read_csv("DataSets\ForUse2.csv", sep=',')
    #data = TrainingModel.objects.all()

    query = str(TrainingModel.objects.all().query)
    data = pd.read_sql_query(query, connection)
    data = data[[
        'sales', 'label', 'cost', 'msrp', 'month', 'mon', 'tues', 'wed',
        'thurs', 'fri', 'sat', 'sun'
    ]]
    predict = 'label'

    #Training the model
    x = np.array(data.drop([predict], 1))
    y = np.array(data[[predict]])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        x, y, test_size=0.1)
    linear = linear_model.LinearRegression()

    #Training the model every time you refresh
    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)
    percentage = (acc)
    percentage = percentage * 100

    # Will get predictions from the parameters from DB.
    #predictions = linear.predict(x_test)
    #myResult = [len(predictions)]
    # myResult = [] * len(predictions)
    #countx = 0
    # for x in range(len(predictions)):
    #     print((int)(predictions[x]), x_test[x], y_test[x])
    #     #myResult[x] = predictions[x]

    #new table for holding real data

    # ------------------- #

    # #----

    query2 = str(StoreData.objects.all().query)
    print("query", query2)
    #condition = Greeting.objects.filter()
    #query = str(StoreData.objects.filter(condition)

    data = pd.read_sql_query(query2, connection)
    #data = data[data.month == monthinput]
    #data = StoreData.objects.filter(month=monthinput)
    print("test", data)
    print("data", data)
    data = data[[
        'sales',
        'cost',
        'msrp',
        'month',
        'mon',
        'tues',
        'wed',
        'thurs',
        'fri',
        'sat',
        'sun',
        'SKU',
    ]]
    x = np.array(data.drop(['SKU'], 1))
    print(x)
    SKU = np.array(data['SKU'])
    print(x.shape)
    predictions2 = linear.predict(x)
    print("real prediction result", predictions2)
    newpredict = predictions2.flatten()
    newpredict = newpredict.tolist()
    newSKU = SKU.flatten()
    newSKU = newSKU.tolist()
    third = zip(newSKU, newpredict)

    #prediction is list of integers
    # #----

    context = {
        "form": form,
        "percentage": percentage * 100,
        "third": third,
    }

    return render(request, "index.html", context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    print(greetings)
    return render(request, "db.html", {"greetings": greetings})


def create(request):
    form = GreetingForm()
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        print("hi", request.POST)
        monthVal = request.POST
        if form.is_valid():
            form.save()
            #messages.info(request, 'Successfully verified!')

        else:
            form = GreetingForm()

    context = {'form': form}
    return render(request, "create.html", context)
