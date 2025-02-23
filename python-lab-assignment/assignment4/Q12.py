import math

def areaTriangle(side1, side2, side3):
    assert side1+side2 > side3
    assert side2+side3 > side1
    assert side3+side1 > side2
    # if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    s = (side1 + side2 + side3) / 2  #semi-perimeter
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print(area)
        # return area
    # else:
    #     return "The sides do not form a valid triangle."

def main():
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    result = areaTriangle(side1, side2, side3)
    
    print(result)

main()
