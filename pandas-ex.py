import pandas as pd
import numpy as np

# to create and display a DataFrame from a specified dictionary data which has the index labels

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

exam_df= pd.DataFrame(exam_data,index=['a','b','c','d','e','f','g','h','i','j'])
print(exam_df)

#select the rows where number of attempts in the examination is less than 2 and score greater than 15

print(exam_df.loc[(exam_df['attempts']< 2) & (exam_df['score'] > 15.0)])

# Change the value in row 'd' to 11.5

# new_df=exam_df.fillna({('score','d'):11.5})
# print(new_df)

exam_df.loc['d','score']=11.5
print(exam_df)

# to calculate the sum of the examination attempts by the students



# Drop a list of rows from a specified DataFrame

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
d_df = pd.DataFrame(d)
print(d_df)
d_df.drop([2,4],inplace=True)
print(d_df)


# Check whether a given column is present in a DataFrame or not

e = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
e_df = pd.DataFrame(e)
print(e_df)
name = 'col1'
if name in e_df.columns:
    print('{} is present'.format(name))
else:
    print('{} is not present'.format(name))


# Get column index from column name of a given DataFrame

f = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
f_df = pd.DataFrame(f)
c_name = 'col2'
c_index = f_df.columns.get_loc(c_name)
print('Index value of {} is {}'.format(c_name,c_index))

# remove last n rows of a given DataFrame


