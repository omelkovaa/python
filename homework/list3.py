marks = input().split()
count = len(marks)
fives = marks.count('5')
print(str(fives / count * 100)+ '%')
