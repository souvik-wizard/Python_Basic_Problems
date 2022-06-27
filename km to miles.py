# 1
user_input=float(input("Enter the number :"))

asking=int(input("Press 1 to convert Km to miles OR Press 2 to convert Miles to km :"))

if asking==1:

   print  ("{:.2f}".format(user_input*0.621371),"Mile")

elif asking==2:
   print  ("{:.2f}".format(user_input*1.609344),"km")
else:
    print("You have chosen wrong option, Try again")


#  2------------------------


def dist_converter(inp,checking):
    if checking==1:
        return inp*0.621371
    elif checking==2:
      
        return inp*1.609344
    else:
        return "You have chosen wrong option, Try again"

inp=int(input("Enter the value:"))
checking=int(input("Press 1 to convert Km to miles OR Press 2 to convert Miles to km :"))
print("The output is:",dist_converter(inp,checking))