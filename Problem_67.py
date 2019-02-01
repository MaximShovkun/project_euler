file = open("Problem_67_triangle.txt", "r")
triangle = file.read()

triangle = triangle.split('\n')

for i, j in zip(triangle, range(len(triangle))):
    triangle[j] = map(int, i.split(' '))

for i in range(1, len(triangle)):

    triangle[i][0] += triangle[i - 1][0]
    triangle[i][len(triangle[i]) - 1] += triangle[i - 1][len(triangle[i - 1]) - 1]

    for j in range(1, len(triangle[i]) - 1):
        if triangle[i - 1][j - 1] > triangle[i - 1][j]:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += triangle[i - 1][j]

print(max(triangle[len(triangle) - 1]))