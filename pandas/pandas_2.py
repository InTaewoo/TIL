# dataFrame
import pandas as pd
# 중첩된 리스트를 통한 데이터 생성
# 각 행을 리스트로 만들어야 함
data = [['Belgium', 'Brussels', 11190846],
        ['India', 'New Delhi', 1303171035],
        ['Brazil', 'Brasília', 207847528]]

df = pd.DataFrame(data)

df = pd.DataFrame(data, columns=['Country','Capital','Population'])
print(df)

df_2 = pd.DataFrame(data,index=['aa','bb','cc'],columns=['Country','Capital','Population'])
print(df_2)

print(type(df_2))
print(df_2.shape)

data = {'col1': [1, 2, 3, 4],
        'col2': [5, 6, 7, 8],
        'col3': [9, 10, 11, 12]}

df_3 = pd.DataFrame(data,
                    index=['A', 'B', 'C', 'D'])

print(df_3)