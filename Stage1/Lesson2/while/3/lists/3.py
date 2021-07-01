# Подсчитать, сколько имен содержат букву "a"

names = ['Bob', 'Alice', 'Katia', 'Vasya', 'Olya']

count = 0
i = 0
while i < len(names):
    name = names[i]
    if 'a' in name or 'A' in name:
        print(name)
        count += 1
    i += 1

print(count)
