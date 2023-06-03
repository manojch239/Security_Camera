import time
import pyotp
import qrcode

key = "THISISMYSUPERDUPERLUPERSECRETKEY" # only service provider should have this
"""t_otp = pyotp.TOTP(key)
print(t_otp.now())

time.sleep(30)
 
print(t_otp.now())

input_code = input("Enter 2FA Code: ")
print(t_otp.verify(input_code))"""

"""counter = 0
hotp = pyotp.HOTP(key)
print(hotp.at(0))

for _ in range(5):
    print(hotp.verify(input("Enter a Code : "),counter))
    counter+=1"""

#uri = pyotp.totp.TOTP(key).provisioning_uri(name="ManojM",issuer_name="MnM369")
#print(uri)
#qrcode.make(uri).save("totp.png")

URL = "https://www.linkedin.com/in/manoj-chowdary-m-7161031b4/"
code = qrcode.make(URL)
code.save('LinkedIn.png')
code.show()


