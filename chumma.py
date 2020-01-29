# import re
#
# s=input("Enter mail Id")
# m=re.fullmatch("[a-zA-Z0-9_.]*@gmail.com",s)
# if m!=None:
#     print("Valid Mail Id")
# else:
#     print("invalid email Id")



#
# import re
#
# s=input("Enter email Id")
# m=re.fullmatch("[a-zA-z0-9_.]*@gmail.com",s)
# if m!=None:
#     print("Valid email Id")
# else:
#     print("invalid emial Id")
#


import re

s=print("Enter the mobile Number")
m=re.fullmatch("91-([0-9]){10}*",s)
if m!=None:
    print("Valid mobile number")
else:
    print("invalid mobile number")






