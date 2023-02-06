word = input("Введите слово: ")
word.upper()
letter = [str(i) for i in str(word.upper())]
points = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
score = 0
for i in letter:
  for k, v in points.items():
    if i in v:
      score = score + k
print(score)