from statistics import mean

l0 = [1, 5, 6.3, 6, None, 2.0, -4, None]
n = mean(list(filter(lambda x: x != None, l0)))
l1 = [x if x != None else n for x in l0]

print(l1)
