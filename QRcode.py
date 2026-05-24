# Step 1: take a user_id of a user
# Step 2: every payment defined  with the URL
# Step 3: every QR code generate with the URL and user_id
# Step 4: we can generate every QR code in image form
# Step 5: every generated QR code we can view with the help of pillow library
import qrcode

#taking UPI ID as a input
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=Mitali_Sharma&am=AMOUNT&cu=CURRENCY&tn=Message
#pa: those upi id which we want to pay
#pn: name of the person to whom we want to pay(Recipient Name)
#am: amount which we want to pay
#tn: message which we want to send with the payment

#Defining the payment URL based on the UPI ID and the payments app
#You can modify the URL based on the payment app you are using (e.g., Google Pay, PhonePe, Paytm)

phonepe_url = f'upi://pay?pa={upi_id}&pn=vashishtmitali0204@ibl%20Mitali_Sharma&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=8920579403@pytes%20Mitali_Sharma&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=vashishtmitali1999@oksbi%20Mitali_Sharma&mc=1234'

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QR code to image file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#Display the QR codes (you may need to install PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
