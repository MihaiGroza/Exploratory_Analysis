import pandas as pd
import researchpy as rp

import statsmodels.formula.api as smf
import statsmodels.stats.api as sms

from scipy import stats
from statsmodels.compat import lzip

import seaborn as sns
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings('ignore')

#loading data
data = pd.read_csv('insurance.csv')

sns.set(style="white", color_codes=True)

#exploratory analysis
gen_charg = sns.stripplot(x='sex', y='charges', data=data, jitter=True, edgecolor='none', alpha=.40)
region_charg = sns.stripplot(x='region', y='charges', data=data, jitter=True, edgecolor='none', alpha=.40)
smoker_charg = sns.stripplot(x='smoker', y='charges', data=data, jitter=True, edgecolor='none', alpha=.40)
age_charg = sns.jointplot(x='age', y='charges', data=data, kind='hex')
bmi_charg = sns.jointplot(x='bmi', y='charges', data=data, kind='hex')

#overview of data
rp.summary_cont(data[['charges','age', 'children']])

rp.summary_cat(data[['sex', 'smoker', 'region']])

#creating dummy columns
data = pd.get_dummies(data)

#generating model
model = smf.ols("charges ~ age + bmi + sex_female + smoker_yes + children + region_northwest + region_southeast + region_southwest", data= data).fit()

#checking for normality
qqplot = stats.probplot(model.resid, plot= plt)

#checking for heteroscedasticity
name = ['Lagrange multiplier statistic', 'p-value', 
        'f-value', 'f p-value']
test = sms.het_breuschpagan(model.resid, model.model.exog)
lzip(name, test)

# generating model and accounting for heteroscedasticity
model3 = smf.ols("charges ~ age + bmi + sex_female + smoker_yes + children + region_northwest + region_southeast + region_southwest", data= data).fit(cov_type='HC3')
    
model3.summary()
