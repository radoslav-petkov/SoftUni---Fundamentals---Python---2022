from math import sqrt


def closer(x1,y1,x2,y2):
    dist_1 = sqrt((x1 ** 2) + (y1 ** 2))
    dist_2 = sqrt((x2 ** 2) + (y2 ** 2))
    if dist_1 < dist_2:
        output = (int(x1 // 1),int(y1 // 1))
    elif dist_2 < dist_1:
        output = (int(x2 // 1),int(y2 // 1))
    else:
        output = (int(x1 // 1),int(y1 // 1))

    return output


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

output = closer(x1,y1,x2,y2)
print(output)