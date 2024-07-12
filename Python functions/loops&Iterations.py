ielts_skills = ['read', 'write', 'speak', 'listen']

for skill in ielts_skills:
    if skill == 'speak':
        print('Found')
        print(skill)

english_level = [1, 2, 3, 4, 5]
for level in english_level:
    if level > 2:
        print('found')
        break
    print(level)

english_level = [1, 2, 3, 4, 5]
for levels in english_level:
    if levels == 3:
        continue
    print(levels)

english_level = [1, 2]
for levels in english_level:
    for letter in 'ABC':
        print(letter, levels)

for level in range(1, 5):
    print(level)

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
