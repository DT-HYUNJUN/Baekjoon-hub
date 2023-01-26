triangle = [int(input()) for _ in range(3)]
if triangle.count(60) == 3:
    print('Equilateral')
elif sum(triangle) == 180 and len(set(triangle)) == 2:
    print('Isosceles')
elif sum(triangle) == 180 and len(set(triangle)) == 3:
    print('Scalene')
elif sum(triangle) != 180:
    print('Error')