l1 = [1, 2.2, "3", 1] 

print(f"List l1: {l1}")
l1.append(5)
print(f"List l1: {l1}")
l1.remove(1)
print(f"List l1: {l1}")
l1.insert(len(l1),9)
print(f"List l1: {l1}")

l2 = [1, 2, 3, 4]
print(f"union of s1 and s2: {l1 | l2}")
print(f"intersect of s1 and s2: {l1 & l2}")
