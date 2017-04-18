total = 0
#variables with price and name
a = str("apple ")
a2 = 3
b = str("potato ")
b2 = 2
#function to produce name and price baised on code
def read ( codes ):
#global variables to be used outside of function
    global total
    global h
    global a
    global b
    h = input()
    if h == "111":
        print(a + "£" + str(a2))
        total = total + int(a2)
    elif h == "222":
        print(b + "£" + str(b2))
        total = total + int(b2)
#total price then resets total and creates a recept-like system
    elif h == "0":
        print ("Total = £" + str(total))
        total = int(0)
        print("---------------------------")
    else:
        print("Code is invalid")
    read("codes")
#introduction to program
print("This is a Barcode Reader")
print("Enter Barcode")
read("codes")


f = open("pyfi.txt","w+")
f.w("hello")
f.close
