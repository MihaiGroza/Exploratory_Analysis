# Statistical Tests

## Correlation

H0 hypothesis: There is not a relationship between Apple and Sp500

HA hypothesis: There is a relationship between variable Apple and Sp500


![Image of model](https://github.com/MihaiGroza/statistical_tests/blob/master/corellation.png)

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

              is_green  is_red
is_monday                  
False         112.608  91.392
True          25.392   20.608 

### Observed matrix

             is_green  is_red
is_monday                  
False         110.0    95.0
True           28.0    18.0

Results:(statistic=0.8007550294850146, pvalue=0.8492864317723491)

Conclusion: Cannot reject the null hypothesis


## Linear Regression


