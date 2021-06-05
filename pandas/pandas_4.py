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

c = pd.DataFrame(np.random.rand(5,5),
             columns=['A','B','C','D','E'],
            index=[1,2,3,4,5])
print(c)

male_tuple={'서울특별시':4732275,
             '부산광역시':1668618,
             '인천광역시':1376813,
             '대구광역시':1198815,
             '대전광역시':734441,
             '광주광역시':720060}
male = pd.Series(male_tuple)
print(male)


female_tuple = {'서울특별시':4988557,
             '부산광역시':1735805,
             '인천광역시':1470404,
             '대구광역시':1229140,
             '대전광역시':734423,
             '광주광역시':739404}
female = pd.Series(female_tuple)
print(female)

pop_tuple = {'서울특별시':9720846,
             '부산광역시':3404423,
             '인천광역시':2947217,
             '대구광역시':2427954,
             '대전광역시':1471040,
             '광주광역시':1455048}
population = pd.Series(pop_tuple)

korea_df = pd.DataFrame({'인구수':population,
                      '남자인구':male,
                     '여자인구':female})
print(korea_df)
print(korea_df.index)
print(korea_df.values)

s=pd.Series(['a','b','c','d','e'],index=[1,3,5,7,9])
print(s)

print(s.iloc[3])
print(s.iloc[2:4])
print(korea_df.남자인구)
korea_df['남여비율']=korea_df.남자인구*100/korea_df.여자인구
print(korea_df)

print(korea_df[1:])

idx_tuples = [('서울특별시', 2010),('서울특별시',2020),
              ('부산광역시', 2010),('부산광역시',2020),
              ('인천광역시', 2010),('인천광역시',2020),
              ('대구광역시', 2010),('대구광역시',2020),
              ('대전광역시', 2010),('대전광역시',2020),
              ('광주광역시', 2010),('광주광역시',2020)]
print(idx_tuples)

pop_tuples = [10312545, 9720846,
              2567910, 3404423,
              2758296, 2947217,
              2511676, 2427854,
              1502664, 1471040,
              1454636, 1455048]
population = pd.DataFrame(pop_tuples, index=idx_tuples)
print(population)