import pandas as pd
s = pd.Series([3,-5,7,4])
print(s)

s = pd.Series([3,-5,7,4],index=['a','b','c','d'])
print(s)

type(s)
print(s.index)
print(s.values)
print(s[0:1])

# pop_dict는 파이썬 딕셔너리
pop_dict = {'Germany': 81.3,
            'Belgium': 11.3,
            'France': 64.3,
            'United Kingdom': 64.9,
            'Netherlands': 16.9}
print(pop_dict)

# pop_dict로 Series 생성
population = pd.Series(pop_dict)
print(population)

print(pop_dict['France'])
print(pop_dict['Germany'])
print(population*1000)







