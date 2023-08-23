exp-9


import numpy as np import
collections
npArray= np.array([60, 70, 70, 70, 80,90,60])
c=collections.Counter(npArray) # Generate a dictionary {"value":"nbOfOccurrences"}
arraySize=npArray.size
nbOtOccurrences=c[60] #assuming you want the proba to get 10
proba=(nbOfOccurrences/arraySize)* 100
print(proba) #print 60.0

#1/usr/bin/env python3 import
Sys
Marksprob = {}
for line in sys.stdin: line =
line strip()
ClassA, Marks = line.split("\t', 1)
def event _probability(cvent outcomes, sample space):
probability = (event outcomes / sample_space) * 100 return
round(probability, 1)
ClassA = 30
Marks = 15
grade probability = event_probability(Marks, ClassA) print(str(grade probability) + '%")



exp-10 -- impl of block world problemm


class Strips(object):
definit(selt, name, preconds, effects, cost=1):
self.name = name
self.preconds =
precondsself.effects =
effects self.cost =
cost
defrepr(self):
return
self.name
class STRIPS domain(object):
definit(self, feats vals, actions):
self feats vals =
feats valsself.actions =
actions
class Planning_problem(object):
definit(self, prob_domain, initial state, goal):
self.prob_domain =
prob_domainself.initialstate =
initial state self.goal = goal
boolean = {True,
False} ### blocks
world
def move(x,y,z):
"string for the 'move' action
return
"move +x+' from ty+' to +z
def on(x):
"string for the 'on'
feature""" return x+'_is_on'
def clear(x):
min
string for the 'clear’
feature""" return ‘clear +x
def create blocks world(blocks = {'a','b",'¢','d"}):
blocksand table = blocks | {'table'}
stmap = {Strips(move(x.y,z), {on(x):y, clear(x): True, clear(z): True},
fon(x):z, clear(y): True,
clear(z):False})} for x in blocks:
fory in
blocks_and table: for z in blocks:
if x!=y and y!=z and z!=x:
stmap.update( { Strips(move(x,y,'table’), {on(x):y,clear(x): True}, {on(x): table’
clear(y):True})}) for x in blocks: for y in blocks:
for. ip blocks:
I=y:
feats_vals = {on(x):blocksand _table-{x} for x in blocks}
feats _vals.update({clear(x):boolean for x in
blocks and_table})
return STRIPS _domain(feats_vals, stmap)
blocks dom =
create_blocks world({'a".'b'",'c'}) blocks! =
Planning_problem(blocksdom,
{on('a"):'table’, clear('a"): True,
on('b"):'e’, clear('b"): True,
on('c"):'table', clear('c'): False}, # initial state
fon('a"):'b', on('c"):'a'}) #goal
blocks2dom = create_blocks_world({'a','b','c','d"})
towerd = {clear('a"): True, on('a'):'b’,
clear('b"):False, on('b"):'c’,
clear('c'):False, on('c'):'d',
clear('d"):False, on('d"):'table'}
blocks2 =
Planning_problem(blocks2dom, towerd, #
initial state
fon('d'):'c,on('c):'bon("b'):"a"}) #eoal
blocks3 =
Planning _problem(blocks2dom, tower4, #
initial state
yon('d'):'a’, on('a’):'b’, on('b'):'c'}) #goal



exp-11 impl of learing algo 


X=[0,6. 11, 14,22]
Y=[1,7, 12,1521]
# solve fora and b
def best fit(X, Y):
xbar = sum(X)/len(X)
ybar = sum(Y)/len(Y)
n= len(X) # or len(Y)
numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar
* ybardenum = sum([x1**2 for x1 in X]) - n * xbar**2
b = numer /
denum a = ybar-b
* xbar
print('best fit line:\ny= {:.2f} + {:.2f}x".format(a, b))
return a, b
# solution
a, b= best fit(X,Y)
#best fit linc:
tty = 0.80 + 0.92x
# plot points and fit line
import matplotlib.pyplot as
pltplt.scatter(X, Y)
yfit = [a + b * xi for xi in
X] plt.plot(X, yfit)
plt.show()
best fit line:
y= 1.48 +0.92x

knn
Importing Libraries
from sklearn.ncighbors import KNeighborsClassifier
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of
test dataset
# Create KNcighbors classifier object model
KNeighborsClassifier(n_neighbors=6) # default value for n_neighborsis 5
# Train the model using the training sets and check score
model. fit(X, y)
#Predict Output
predicted= model.predict(x_test)
df.columns = ['X1', 'X2', 'X3", 'X4','Y"]
df= df.drop(['X4', "X3'],
1) df.head()
sns.set_context('notebook’, font scale=1.1)
sns.set_style('ticks')
sns.Implot("X1',"X2", scatter=True, fit_rcg=Falsc, data=df, huc='Y")
plt.ylabel('X2")
plt.xlabel("X1")
from sklearn.cross validation import
train_test split neighbors =
KNeighborsClassifier(n_neighbors=5) X =
df.values[:, 0:2]
Y = df.values[:, 2]
trainX, testX, trainY, testY = train_test_split( X,Y, test size = 0.3)
neighbors.fit(trainX, trainY’)
print(' Accuracy: \n', neighbors.score(testX,
testY)) pred = neighbors.predict(testX)


exp 12   development of ensamble model 


# importing utility modules
import pandas as pd
from sklearn.model selection import train_test_split
from sklearn.metrics import mean_squared_crror
# importing machine learning models for prediction
from sklearn.ensemble import
RandomForestRegressor import xgboost as xgb
from sklearn.lincar_model import LincarRegression
# loading train data sct in dataframe from train_data.csv file
df =pd.rcad csv("train_data.csv")
# getting target data from the
dataframe target = df "target"]
# getting train data from the dataframe
train = df.drop("target")
# Splitting between train data into training and validation dataset
X train, X test, y train, y test = train test split(
train, target, test _size=0.20)
# initializing all the model objects with default
parameters model 1 = LinearRegression()
model 2 = xgh.XGBRegressor()
model 3 =
RandomForestRegressor()
# training all the model on the training dataset
model 1.fit(X train, y_ target)
model 2.fit(X train, y target)
model 3.fit(X train, y target)
# predicting the output on the validation
dataset pred I = model 1.predict(X_test)
pred 2 = model 2.predict(X test)
pred 3 =model 3.predict(X test)
# final prediction after averaging on the prediction of all 3 models
pred _final = (pred _1+pred 2+pred 3)/3.0
# printing the root mean squared error between real value and predicted value
print(mean_squared_error(y_test, pred_final))


exp-13 nlp solution


 Import data and tagger
from nltk.corpus import
twitter samples from nltk.tag import
pos_tag_sents
# Load tokenized tweets
tweets_tokens = twitter _samples.tokenized('positive _tweets.json')
# Tag tagged tweets
tweets tagged = pos tag sents(tweets_tokens)
# Set
accumulators
JJ count=0
NN_count=0
# Loop through list of
tweets for tweet in
tweets tagged:
for pair in
tweet: tag =
pair[1] if tag
=="JJ"
JJ count +=
1 elif tag ==
NN"
NN_count += |
print('Total number of adjectives =", JJ count)
print("Total number of nouns =", NN_count)


exp - 14 deep learing projects in python 

Aim —Deep learning Project in Python
Code=
The steps to cover in this are as follows:
Load Data.
Define Keras Model.
1
2
3. Compile Keras Model.
4. Fit Keras Model.
5 Evaluate Keras Model.
6. Tic It All Together.
7. Make Predictions
Load Data.
a. Dataset used —
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
b. Code-
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = datasct[:,8]
Define Keras Model.
a. Code-
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8§,
activation="relu')) model.add(Dense(8,
activation="relu')) model.add(Dense( 1,
activation='sigmoid"))

Compile Keras Model.
a. Code —
# compile the keras model
model.compile(loss='binary_crossentropy’, optimizer="adam’, metrics=['accuracy'])
Fit Keras Model.
a. Code —
# fit the keras model on the dataset
model. fit(X, y, epochs=150, batch _size=10,verbosc=0)
Evaluate Keras Model.
a. Code —
# evaluate the keras model
_, accuracy = model.cvaluate(X, y, verbose=0
print("Accuracy: %.21" % (accuracy*100))

Tie It All Together.
a. Code-
# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter="")
# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset([:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8,
activation="relu')) model.add(Dense(8,
activation=Trclu")) model.add(Dense(1,
activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer="adam’, metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch _size=10,verbose=0)
# evaluate the keras model
accuracy = model.evaluate(X, vy, verbose=0)
print(' Accuracy: %.2{" % (accuracy*100))


ake Predictions
a. Code-—
# first neural network with keras make predictions
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
# load the dataset, Co. . . . .
dataset — Sad pima-indians-diabetes.csv', delimiter=",") # split into input (X) and output (y)
variables
X = dataset[:,0:8]
y = dataset|:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input dim==8,
activation="relu')) model.add(Dense(8,
activation="relu")) model.add(Dense( 1,
activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer="adam’,
metrics=["accuracy']) # fit the keras model on the dataset
model fit(X, y, epochs=150, batch_size=10, verbose=0)
# make class predictionswith the model
predictions = model.predict classes(X)
# summarize the first 5 cases
for i in range(5):
print("%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

Keras Project Summary —
In this project, we discovered how to create our first neural network model using the
powerful Keras Python library for deep learning.
Specifically, we learnt the six key steps in using Keras to create a neural network or deep
learning model, step-by-step including:
How to load data.
How to define a neural network in Keras.
How to compile a Keras model using the efficient numerical
backend. How to train a model on data.
How to evaluate a model on data.
How to make predictions with the model.
Result —The program executed successfully. 