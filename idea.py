from base64 import b64encode,b64decode
from hashlib import sha256
# dữ liệu khách hàng gửi
data = {"cardId":"618559d321b3860023be57e8","cart":[{"productId":"60102f9b6e989f46b051b3c8","payablePrice":450000,"purchaseQty":1}],"name":"le the thang","phone":562404529,"city":"Tỉnh Quảng Ninh","town":"Thị xã Đông Triều","address":"abc","fee":0,"totalAmount":450000}
#B1.kiểm tra xem data có hợp lệ không ?

#B2.tạo payment
payment = ""
for i in data:
    payment=payment+str(i)+":"+str(data[i])+"&"
payment = payment[:-1]  # xoá dấu & ở cuối thôi
#print(payment)

#B3.tạo Signature
private_sign_key = "nguyenchihao2001"
Signature = sha256((private_sign_key+payment).encode()).hexdigest()
#print(Signature)

#B4.thêm Signature vào cuối payment
payment = payment + "&Signature:" + Signature
#print(payment)

#B5.gửi header payment : base64.encode(payment) cho client
payment = b64encode(payment.encode())
#print(payment)

#B6. client nhận được header payment(có chữ kí)
#đoạn này nếu bình thường thì gửi lại server thôi
# còn khác thường sẽ giữ lại chỉnh sửa payment (hash length extension attack)

#B7. xác thực
# decode base64
payment = b64decode(payment).decode()
print(payment)
if "Signature" not in payment:
    print("không có chữ kí thì không xác thực -> dừng")
#xác định vị  trí của Signature trong payment
Position_of_Signature = payment.find("&Signature:")
Signature = payment[Position_of_Signature+11:]
#xác thực
data = payment[:Position_of_Signature]
if sha256((private_sign_key+data).encode()).hexdigest() != Signature:
    print("cút luôn")
#B8.thanh toán
data_analysis = data.split("&")
data = {}
for s in data_analysis:
    arr = s.split(":")
    key,value = arr[0],arr[1]
    data[key] = value

totalAmount = int(data["totalAmount"])

if money < totalAmount :
    print("có đủ tiền đâu mà mua ? cút ra khỏi cửa hàng")

money = money - totalAmount

