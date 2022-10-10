original_password = 'open@123'
original_security_answer = 'black'


password = input("Enter your password:")
if(password == original_password):
    print("Door will open")

else:
    c=1
    while (password != original_password):
        c=c+1
        print("Worng Password and Try again.")
        password = input("Enter your password:")
        if password== original_password:
            print("Door will open")
            break
        if c==3:
            security_answer= input("Enter your original_security_answer: ")
            if security_answer == original_security_answer:
                    original_password = update_password = input("Enter new password: ")
                    print("Your Password has been updated!")
                    print("Enter your new password and open the door!")
            else:
                    print("You can't open the door")
                    break
                
print(original_password)