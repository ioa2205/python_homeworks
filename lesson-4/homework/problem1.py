# Problem 1
l1 = [1, 2, 3, 4, 5,6,23]
l2 = [6, 7, 8, 9, 10]
uncommon_elements = list(set(l1).symmetric_difference((l2)))
l = [i for i in l1 if i not in l2] + [j for j in l2 if j not in l1]

print(uncommon_elements)
print(l)