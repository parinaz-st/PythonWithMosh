course = 'python for begginers'
print(course.upper()) #returns a new string
print(course)

print("find the index of y : " + str(course.find('y')))
print("find the index of Y : " + str(course.find('Y')))
print("find the index of for : " + str(course.find('for')))
print("find the index of for : " + str(course.find('for')))
print('\n')
print("replace b fot g: " + course.replace('b', 'g'))
print("find if the string has the word python: " + str(course.find('python')) + " (the index of the first character of python)")

print("another way to see if the course have python in it with (in): ")
print('python' in course)