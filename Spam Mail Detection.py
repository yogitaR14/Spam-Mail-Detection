#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[2]:


# loading the data from csv file to a pandas Dataframe
raw_mail_data = pd.read_csv('mail_data.csv')


# In[ ]:


print(raw_mail_data)


# In[ ]:


# replace the null values with a null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')


# In[ ]:


# printing the first 5 rows of the dataframe
mail_data.head()


# In[ ]:


# checking the number of rows and columns in the dataframe
mail_data.shape


# In[ ]:


# label spam mail as 0;  ham mail as 1;

mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1


# In[ ]:


# separating the data as texts and label

X = mail_data['Message']

Y = mail_data['Category']


# In[ ]:


print(X)


# In[ ]:


print(Y)


# In[ ]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)


# In[ ]:


print(X.shape)
print(X_train.shape)
print(X_test.shape)


# In[ ]:


# transform the text data to feature vectors that can be used as input to the Logistic regression

feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english')

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)

# convert Y_train and Y_test values as integers

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')


# In[ ]:


print(X_train)


# In[ ]:


print(X_train_features)


# In[ ]:


model = LogisticRegression()


# In[ ]:


# training the Logistic Regression model with the training data
model.fit(X_train_features, Y_train)


# In[ ]:


# prediction on training data

prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)


# In[ ]:


print('Accuracy on training data : ', accuracy_on_training_data)


# In[ ]:


# prediction on test data

prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)


# In[ ]:


print('Accuracy on test data : ', accuracy_on_test_data)


# In[ ]:


input_mail = ["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times"]

# convert text to feature vectors
input_data_features = feature_extraction.transform(input_mail)

# making prediction

prediction = model.predict(input_data_features)
print(prediction)


if (prediction[0]==1):
  print('Ham mail')

else:
  print('Spam mail')


# In[ ]:




