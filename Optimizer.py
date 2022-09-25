#!/usr/bin/env python
# coding: utf-8

# # Sportscience

# In[5]:


from scipy.optimize import linprog
import pandas as pd
data = pd.read_csv("Sportscience.csv", sep=';')
pd.DataFrame.from_records(data)
data.head()


# In[25]:


from scipy.optimize import linprog
import pandas as pd
data = pd.read_csv("SportscienceDots.csv", sep=';')
pd.DataFrame.from_records(data)

obj = data['price_tmp'].tolist() # Целевая функция

def negative(number):
    return number * -1

proteins = data['proteins'].tolist()             # Белки
proteins1 = list(map(negative, proteins))
fats = data['fats'].tolist()                     # Жиры
fats1 = list(map(negative, fats))
carbohydrates = data['carbohydrates'].tolist()   # Углеводы
carbohydrates1 = list(map(negative, carbohydrates))
calories = data['calories'].tolist()                 # Калории
calories1 = list(map(negative, calories))


lhs_ineq = [proteins1,        # Белки
            fats1,            # Жиры
            carbohydrates1,   # Углеводы
            calories1]        # Калории

rhs_ineq = [ -1000,  # Белки
             -1000,  # Жиры
             -1000,  # Углеводы
             -2500]  # Калории

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")

opt

