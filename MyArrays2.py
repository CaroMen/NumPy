import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

print(grades.mean(axis=0))
print(grades.mean(axis=1))

numbers = np.array([1, 4, 9, 16, 25, 36])

print(np.sqrt(numbers))

print(grades[0, 1])
print(grades[1])
print(grades[0:2])
print(grades[[1, 3]])

print()
print()

print(grades[1, 2])
print(grades[[1, 3]])
print(grades[:, 0])

# shallow copies
numbers = np.arange(1, 6)
number2 = numbers.view()

print(number2)

numbers[1] *= 10

print(number2)

number2[1] /= 10

print(numbers)

numbers2 = numbers[0:3]

numbers[1] *= 20

print(numbers2)


# deep copies

numbers2 = numbers.copy()

grades = np.array([[87, 96, 70], [100, 87, 90]])

print(grades.reshape(1, 6))

print(grades)

flattened = grades.flatten()
print(flattened)

raveled = grades.ravel()
print(raveled)

raveled[6] = 99
print(grades)

grades2 = grades.T

print(grades2)
print(grades)

grades = np.array([[87, 96, 70], [100, 87, 90]])

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades, grades2))

print(h_grades)

v_grades = np.vstack((grades, grades2))

print(v_grades)
