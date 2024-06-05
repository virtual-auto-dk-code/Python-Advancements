dict = {'A':'a','B':'b'}
ls = []
ls1 = ['p','q']
ls2 = ['x','y']
ls.append(ls1)
ls.append(ls2)
ls.append(dict)
print(ls)
dict['C'] = ['ccc']
print(ls)
ls3 = dict['C']
print(type(ls3))
print(ls3)


