
major_password = "origin"
master_pasword = input("what is your manster password?  :")

if master_pasword == major_password:
    print("master password id correct")
else:
    print("master passowrd is invalid")



def view():
    with open("passowrd.txt","r") as f :
        for line in f.readline:
            print(line)
    


def add():
    name = input("Account name  :")
    pwd = input("Enter the password  :")
    with open("password.txt", "a") as f :
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("would you like to add a new or view exixting ones? .or you want to quit press q   : ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break

    else:
        print("invalid mode"  )
#gain modified         continue
