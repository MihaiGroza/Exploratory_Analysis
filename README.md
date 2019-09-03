# Statistical Tests

## Correlation

H0 hypothesis: There is not a relationship between Apple and Sp500

HA hypothesis: There is a relationship between variable Apple and Sp500


![Image of model](https://github.com/MihaiGroza/statistical_tests/blob/master/Graphs/corellation.png)

It seems that there is a linear relationship, however we must check for homogeneity of variance

### Levene's Test of Homogeneity 

(statistic=35.46732173033491, pvalue=4.904150098936615e-09)

The test is significant. Our variances are not homogenous.
We should opt for a correlation test that doesn't assume homogeneity such as a spearman instead of a pearson.


Pearson correlation method (assumes homogeneity of variance)
(correlation=0.7478342928339387, pvalue=5.107535442948088e-46)

Spearman rank correlation method
(correlation=0.7321835035153023, pvalue=2.989768108578345e-43)

Conclusion: There is a high relationship between Apple and the overall market. 

## Chi Square Test

The H0 (Null Hypothesis): Trading outcome is independent of mondays and non-mondays.

The H1 (Alternative Hypothesis): Trading outcome is not independent of mondays and non-mondays.

### Expected matrix

|is_monday    | is_green |is_red|
|-------------| ---------|------|
|False        | 112.608  |91.392|
|True         | 25.392   |20.608| 

### Observed matrix

|is_monday   | is_green  |is_red|
|------------|-----------|------|
|False       |  110.0    |95.0  |
|True        |   28.0    |18.0  |

Results:(statistic=0.8007550294850146, pvalue=0.8492864317723491)

Conclusion: Cannot reject the null hypothesis. Wether a day trades in the red is independent of the day the stock is traded on.  (In this case, we used the stock prices of Apple)


## Linear Regression

Data: https://www.kaggle.com/mirichoi0218/insurance
Goal: Find most impactful predictors of insurance premiums
Overview:


### Exploratory Analysis

(click to enlarge)

  smoker charges|gender charges| region charges
  :------------:|:------------:|:--------------:
  ![](https://github.com/MihaiGroza/statistical_tests/blob/master/Graphs/smoker_charges.png)|![](https://github.com/MihaiGroza/statistical_tests/blob/master/Graphs/sex_charges.png)|![](https://github.com/MihaiGroza/statistical_tests/blob/master/Graphs/region_charges.png)

According to our exploratory anaylsis, we see that gender and region do not impact the premiums. However, smoking is a strong predictor.

### Normality Test

![Image of model](https://github.com/MihaiGroza/statistical_tests/blob/master/Graphs/Probability%20Plot.png)

The residuals of our model is not normally distributed

### Homoscedasticity Test using Bruesch-Pagan

Lagrange multiplier statistic = 121.74360137568986
p-value = 1.446717553918174e-22               

The variance of our data is not homogenous. We will account for this in the model re-run.

### Results

|                |       coef |   std err |         z  |   P>|z|  |  [0.025    |  0.975]   |
|------------------------------------------------------------------------------------
|Intercept       | -1.207e+04 |  1062.898 |   -11.356  |    0.000 |  -1.42e+04 |  -9986.611|
|age             |   256.8564 |    11.961 |    21.474  |    0.000 |    233.412 |    280.300|
|bmi             |   339.1935 |    31.879 |    10.640  |    0.000 |    276.711 |    401.676|
|sex_female      |   131.3144 |   334.971 |     0.392  |    0.695 |   -525.217 |    787.846|
|smoker_yes      |  2.385e+04 |   578.079 |    41.255  |    0.000 |   2.27e+04 |    2.5e+04|
|children        |   475.5005 |   131.009 |     3.630  |    0.000 |    218.727 |    732.274|
|region_northwest|  -352.9639 |   486.616 |    -0.725  |    0.468 |  -1306.714 |    600.786|
|region_southeast| -1035.0220 |   503.426 |    -2.056  |    0.040 |  -2021.718 |    -48.326|
|region_southwest|  -960.0510 |   463.014 |    -2.073  |    0.038 |  -1867.541 |    -52.561|
