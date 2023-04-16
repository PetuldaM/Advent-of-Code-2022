with open('calories2.txt', encoding='utf-8') as file:
    calories = file.read().splitlines()

if calories[-1] != '':
    calories.append('')
supporting_list = []
elfs = []
for item in calories:
    if item != '':
        item = int(item)
        supporting_list.append(item)
    else:
        elfs.append(supporting_list)
        supporting_list = []

calories_total = []

for i in elfs:
    calories_total.append(sum(i))

max_calories= max(calories_total)

print(max_calories)

calories_total = sorted(calories_total)

last_three = sum(calories_total[-3:])

print(last_three)
