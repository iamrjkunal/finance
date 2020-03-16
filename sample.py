import numpy as np
import pandas as pd
ser1 = pd.Series([1,2], index=['usa','china'])
df= pd.DataFrame([[1,2],[3,4],[5,6]],['a','b','c'],['c1','c2'])
#dataframe is actually series arranged column wises
df['c1'] #columns
df.loc['a'] #rows