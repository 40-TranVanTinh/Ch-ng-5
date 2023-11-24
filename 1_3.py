n=int(input("Nhập mặt hàng:"))
if( n==1):
    print("Tên hàng: Sữa hộp Vinamilk") 
if(n==2):
    print("Tên hàng:Sữa hộp Milo")
else:
    print("Tên hàng:Sữa hộp Ovantine")        
m=int(input("Nhập số lượng:"))
if(m*n==m):
    print("Số lượng:",m)
    print("Đơn giá:25000")
    print("Tiền phải trả:",m*25000)
if(m*n>m and m*n<m*3):
    print("Số lượng:",m)
    print("Đơn giá :30000")
    print("Tiền phải trả:",m*30000)
else:
    print("Số lượng:",m)
    print("Đơn giá: 32000")
    print("Tiền phải trả:",m*32000)        