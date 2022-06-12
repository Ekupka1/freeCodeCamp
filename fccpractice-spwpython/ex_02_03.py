#)2-03 EX pfe - Calculating Pay

sh = input('enter hours: ')
sr = input('enter rate: ')

try:
    fh = float(sh) #Danger Code
    fr = float(sr) #Danger Code
except:
    print("ERROR, Please enter a # input")
    quit()

# Check 1
# print(fh, fr)

# if fh > 40 :
#     # print("Over-time")
#     reg = fr * fh
#     otp = (fh-40.0) * (fr*0.5)
#     # print(reg, otp)
#     xp = reg + otp
# else:
#     # print('Regular-time')
#     xp = fr * fh

# print("pay: ", xp)

# 04-06 function making 
def computePay(hours, rate):
    print("In compute pay", hours, rate)
    if hours > 40:
        reg = fr * fh
        otp = (fh-40.0) * (fr*0.5)
        pay = reg + otp
    else:
        pay = fr * fh
    # print("returning", pay)
    return pay


xp = computePay(fh, fr) #evokes function
print("Pay: ", xp)
