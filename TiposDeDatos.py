n1 = 8
n2 = 10.5
palabra = "ejercicio"

print(n1)
print(n2)
print(palabra)
mi_set = {n1, n2, palabra}
print(mi_set)
mi_set.add(False)
print(mi_set)
print(len(mi_set))

a={12,34,5,6,78,90}
b={12,2,4,6,8,97}
print(a)
print(b)
ab= a|b
print(ab)
print(len(ab))
ab1=a&b
print(ab1)
ab2=a-b
print(ab2)
a.isdisjoint(b)