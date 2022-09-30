import random

import qrcode
from django.shortcuts import render
otp = 0
def OpenLoginPage(request):
    return render(request,"login.html")


def validateUser(request):
    name = request.POST.get("t1")
    password = request.POST.get("t2")
    # import random
    # import qrcode

    # x = random.randint(100000,999999)
    # im = qrcode.make("OTP is"+str(x))
    # im.show()
    if name == "python" and password == "django":
        rno = random.randint(100000, 999999)
        global otp
        otp = rno
        im = qrcode.make("OTP:" + str(rno))
        im.save(r"app1/static/qrimages/soumya.jpg")#this qrcode image save in this files
        return render(request, "qrcode_page.html")
    else:
        return render(request,"login.html",{"message":"Invalid User"})

def ValidateOtp(request):
    user_otp = request.POST.get("otp")
    if user_otp == str(user_otp):
        return render(request,"welcome.html")
    else:
        return render(request,"login.html",{"message":"Invalid User"})



