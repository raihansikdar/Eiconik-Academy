original_password = 'open@123'
original_security_answer = 'black'

password = input("Enter your password 1st time:")
if password == original_password:
    print("Door will open")
else:   
    print('XXX-- Worng password and try again.--XXX')
    print()
    password = input("Enter your password 2nd time:")
    if password == original_password:
        print("Door will open")
    else:
        print('XXXX-- Worng password and try again.--XXXX')
        print()
        password = input("Enter your password 3rd time:")
        if password == original_password:
            print("Door will open")
        else:
            print('XXXX-- Worng password --XXXX')
            print()
            security_answer= input("Enter your original_security_answer: ")
            if security_answer == original_security_answer:
                original_password = update_password = input("Enter new password: ")
                print("Your Password has been updated!")
            else:
                print("You can't open the door")
              
print(original_password)