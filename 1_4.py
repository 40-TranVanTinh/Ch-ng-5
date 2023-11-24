import math
a=int(input("Nhập cạnh 1:"))
b=int(input("Nhập cạnh 2:"))
c=int(input("Nhập cạnh 3:"))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là:",s)