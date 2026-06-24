m=[50, 65, 80, 70, 90]
print(m)
print(m[2:])
print(m[1:4])
print(m[:3])
for item in m:
    print(item, end=" ")

print()
# WAPP find the lowest element form the list using loop
for i in range(0,5):
    print(m[i], end=" ")
print()

print(min(m))
print(max(m))
print(len(m))
m.append(95)
print(m)
m.pop()
print(m)
m.sort()
print(m)
m.sort(reverse=True)
print(m)