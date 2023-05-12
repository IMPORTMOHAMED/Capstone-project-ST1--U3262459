import pandas as pd
import sklearn.model_selection
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from dataclasses import dataclass

# Data file import
df = pd.read_csv("Copy of cancer patient data sets.csv")

# Attribute to be predicted
predict = "released"

# pre-processing
# encode object columns to integers
for col in df:
    if df[col].dtype == 'object':
        df[col] = OrdinalEncoder().fit_transform(df[col].values.reshape(-1, 1))

# Dataset to be Predicted, X is all attributes and y is the features
# pre-processing
le = preprocessing.LabelEncoder()
Age = le.fit_transform(list(df["Age"]))
Gender = le.fit_transform(list(df["Gender"]))
AirPollution = le.fit_transform(list(df["Air Pollution"]))
Alcohol_use = le.fit_transform(list(df["Alcohol use"]))
DustAllergy = le.fit_transform(list(df["Dust Allergy"]))
OccuPationalHazards = le.fit_transform(list(df["OccuPational Hazards"]))
GeneticRisk = le.fit_transform(list(df["Genetic Risk"]))
ChronicLungDisease = le.fit_transform(list(df["chronic Lung Disease"]))
BalancedDiet = le.fit_transform(list(df["Balanced Diet"]))
Obesity = le.fit_transform(list(df["Obesity"]))
Smoking = le.fit_transform(list(df["Smoking"]))
PassiveSmoker = le.fit_transform(list(df["Passive Smoker"]))
ChestPain = le.fit_transform(list(df["Chest Pain"]))
CoughingBlood = le.fit_transform(list(df["Coughing of Blood"]))
Fatigue = le.fit_transform(list(df["Fatigue"]))
WeightLoss = le.fit_transform(list(df["Weight Loss"]))
ShortnessBreath = le.fit_transform(list(df["Shortness of Breath"]))
Wheezing = le.fit_transform(list(df["Wheezing"]))
SwallowingDifficulty = le.fit_transform(list(df["Swal0ing Difficulty"]))
ClubbingFingerNails = le.fit_transform(list(df["Clubbing of Finger Nails"]))
FrequentCold = le.fit_transform(list(df["Frequent Cold"]))
DryCough = le.fit_transform(list(df["Dry Cough"]))
Snoring = le.fit_transform(list(df["Snoring"]))
Level = le.fit_transform(list(df["Level"]))  # 0 low, 1 = medium, 2 = high risk

# Declare x and y values
x = list(zip(Age, Gender, AirPollution, Alcohol_use, DustAllergy, OccuPationalHazards, GeneticRisk, ChronicLungDisease,
             BalancedDiet, Obesity, Smoking, PassiveSmoker, ChestPain, CoughingBlood, Fatigue, WeightLoss,
             ShortnessBreath, Wheezing, SwallowingDifficulty, ClubbingFingerNails, FrequentCold, DryCough, Snoring))
y = list(Level)

# Test options and evaluation metric
num_folds = 5
seed = 7
scoring = 'accuracy'

# Splitting what we are trying to predict into 4 different arrays -
# X train is a section of the x array(attributes) and vise versa for Y(features)
# The test data will test the accuracy of the model created
# 0.2 means 80% training 20% testing, with higher data it already has seen that information and knows
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.20, random_state=seed)


# Prediction function
@dataclass(eq=True, frozen=True, order=True)
class lung_cancer_model_prediction:
    best_model = RandomForestClassifier()
    best_model.fit(x_train, y_train)
    y_pred = best_model.predict(x_test)
    model_accuracy = accuracy_score(y_test, y_pred)
