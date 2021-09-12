from pandas import DataFrame

numbers = {'set_of_numbers': [1,2,3,4,5,6,7,8,9,10]}
df = DataFrame(numbers,columns=['set_of_numbers'])

df.loc[df['set_of_numbers'] in range(0,5), 'equal_or_lower_than_4?'] = 'True'
df.loc[df['set_of_numbers'] > 4, 'equal_or_lower_than_4?'] = 'False'

print (df)