# -*- coding: utf-8 -*-
data = (('香蕉', 34, 2), ('芭樂', 28, 3), ('水梨', 50, 2))
total = [] # 小計

print('品  名\t數  量\t單  價\t小  計')

for t1 in data:
    name,s1,s2 =t1 # (品名,數量,單價)
    total.append(s1 * s2)
    print(f'{name:>4}{s1:8}{s2:8}{total[-1]:8}')
    #print(f'{name:>4}{s1:8}{s2:8}{s1*s2:8}')


print(f'總  計:{sum(total):23}')  