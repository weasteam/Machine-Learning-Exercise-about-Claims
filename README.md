# Machine Learning Exercise

We are interested in an analytic and/or predictive model to predict claims that would be denied with the following Denial.Reason.Code: F13, J8G, JO5, JB8, JE1, JC9, JF1, JF9, JG1, JPA and JES.


### [Basic Work Flow](https://www.mathworks.com/help/stats/supervised-learning-machine-learning-workflow-and-algorithms.html?s_tid=gn_loc_drop)

```{mermaid}
graph TB
    P[Prepare Data]-->C[Choose an Algorithm]
    C-->F[Fit a Model]
    F-->M[Choose a Validation Method]
    M-->E[Examine Fit and Update Until Satisfied]
    E-->FP[Use Fitted Model for Predictions]
```

### Understand Your Data
* [How To Load Machine Learning Data in Python](http://machinelearningmastery.com/load-machine-learning-data-python/)
* [Understand Your Data With Descriptive Statistics](https://s3.amazonaws.com/MLMastery/machine_learning_mastery_with_python_sample.pdf)
* [Understand Your Machine Learning Data With Descriptive Statistics in Python](http://machinelearningmastery.com/understand-machine-learning-data-descriptive-statistics-python/)
* [Visualize Machine Learning Data in Python With Pandas](http://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/)

### Preprocessing data
* Categorical Varible to digital
* Object to float
* [Simple Methods to deal with Categorical Variables in Predictive Modeling](https://www.analyticsvidhya.com/blog/2015/11/easy-methods-deal-categorical-variables-predictive-modeling/)

### Understand Your Data on the processed data
* Correlations, find the columns need to be reduced
* Skew, Histograms, Box, find the columns need to be normalized
* Scater plat, find the category columns that does not help much

### Transform Data
* [Preprocessing data](http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
* [How to Prepare Data For Machine Learning](http://machinelearningmastery.com/how-to-prepare-data-for-machine-learning/)
* [How To Prepare Your Data For Machine Learning in Python with Scikit-Learn](http://machinelearningmastery.com/prepare-data-machine-learning-python-scikit-learn/)

### Feature Selection
* [An Introduction to Feature Selection](http://machinelearningmastery.com/an-introduction-to-feature-selection/)
* [Feature Selection in Python with Scikit-Learn](http://machinelearningmastery.com/feature-selection-in-python-with-scikit-learn/)
* [machine_learning_mastery_with_python_sample](https://s3.amazonaws.com/MLMastery/machine_learning_mastery_with_python_sample.pdf)
* [Data Dimensionality Reduction](http://www.kdnuggets.com/2015/05/7-methods-data-dimensionality-reduction.html)

Examples of dimensionality reduction methods include Principal Component Analysis, Singular Value Decomposition and Sammon’s Mapping.
