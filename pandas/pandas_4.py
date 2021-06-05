import pandas as pd
import numpy as np
s5 = pd.Series({'국어':100, '영어':95, '수학':90})
print(s5)

print(pd.date_range(start='2019/01/01',end='2019.01.07'))

a = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(a)
b = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(b)
print(pd.DataFrame(b))
