# To calculate the Area and Perimeter of a rectangle
length=float(input("enter length of the rectangle"))
breadth=float(input("enter breadth of the rectangle"))
print("area is", length*breadth)
print("perimeter is", 2*(length+breadth))
# To calculate the Area of a triangle with Base and Height
base=float(input("enter base of the triangle"))
height=float(input("enter height of the triangle"))
print("area is", 0.5 *base*height)

# To calculate average marks of 3 subjects
num1=float(input("enter marks for first subject"))
num2=float(input("enter marks for Second subject"))
num3=float(input("enter marks for third subject"))

average=(num1+num2+num3)/3
print("average is", average)
# To calculate discounted amount with discount %
price=float(input("enter price for item"))
discount=float(input("enter discount in percentage"))
print("discounted amount is",price-(discount/100)*price)
# To calculate the Surface Area and Volume of a Cuboid
#Total Surface Area = 6(side)**2
#Volume of cube = (Side)**3
side=float(input("side of cuboid"))
print("Area is" , 6*side**2)
print("Volumeis", side**3)
