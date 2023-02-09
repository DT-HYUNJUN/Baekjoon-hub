min_burger = 2000
min_drink = 2000
for _ in range(3):
    burger = int(input())
    if min_burger > burger:
        min_burger = burger
for _ in range(2):
    drink = int(input())
    if min_drink > drink:
        min_drink = drink
print(min_burger + min_drink - 50)