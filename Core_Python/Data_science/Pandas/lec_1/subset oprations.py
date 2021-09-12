import pandas as pd
titanic = pd.read_csv('../lec 2/titanic.csv')
print("::: pd.read_excel() example::: \n")
#How do I select specific columns from a DataFrame
ages = titanic["Age"]
print(ages)
#Each column in a DataFrame is a Series. As a single column is selected,
# the returned object is a pandas DataFrame. We can verify this by checking the type of the output:
print(type(titanic["Age"]))
#And have a look at the shape of the output:

print(ages.shape)
#DataFrame.shape is an attribute (remember tutorial on reading and writing,
# do not use parantheses for attributes) of a pandas Series and DataFrame containing
# the number of rows and columns: (nrows, ncolumns). A pandas Series is 1-dimensional and only the
# number of rows is returned.

#The inner square brackets define a Python list with column names, whereas the outer brackets are used
# to select the data from a pandas DataFrame as seen in the previous example.
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())

#will return number of rows and colums
print(titanic[["Age", "Sex"]].shape)

#To select rows based on a conditional expression, use a condition inside the selection brackets [].
above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())
print(above_35.shape)
#The output of the conditional expression (>, but also ==, !=, <, <=,… would work)
# is actually a pandas Series of boolean values (either True or False) with the same number of
# rows as the original DataFrame. Such a Series of boolean values can be used to filter the
# DataFrame by putting it in between the selection brackets []. Only rows for which the value is
# True will be selected.


