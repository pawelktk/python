import math


def odleglosc(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)


def obwod_trojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Punkty są współliniowe – nie tworzą trójkąta.")
        return 0
    d1 = odleglosc(P1, P2)
    d2 = odleglosc(P2, P3)
    d3 = odleglosc(P3, P1)
    return d1 + d2 + d3

def czy_wspolliniowe(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    return (x2 - x1)*(y3 - y1) == (y2 - y1)*(x3 - x1)


print("Odległość między punktami [0, 0] i [3, 4]:", odleglosc([0, 0], [3, 4]))

P1 = [0, 0]
P2 = [0, 3]
P3 = [4, 0]
print("Obwód trójkąta:", obwod_trojkata(P1, P2, P3))

P4 = [0, 0]
P5 = [1, 1]
P6 = [2, 2]
print("Czy punkty są współliniowe?", czy_wspolliniowe(P4, P5, P6))
print("Obwód trójkąta współliniowego:", obwod_trojkata(P4, P5, P6))
