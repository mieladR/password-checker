
    
def passwordReset():
    newPassword = input("Enter your new password: ")
    confirmPassword = input("Confirm your new password: ")
    if newPassword == "" or confirmPassword == "":
        print("Password reset failed. Password cannot be empty.")
        return None
    
    elif newPassword == confirmPassword:
        print("Password reset successful. Please try logging in again.")
        return newPassword

    else:
        print("Passwords do not match. Password reset failed. Access permanently denied.")
        return None
access=False
failed_attempts = 0
currentPassword = "rubberDucky123"

while access == False:
    password = input("Enter your password: ")

    if str(password) == currentPassword:
        print('Welcome to the system.')
        access = True
    else: 
        print("Incorrect password. Access denied.")
        failed_attempts += 1
        if failed_attempts >= 3:
            print("Too many failed attempts. Access permanently denied.")
            break
            
        elif failed_attempts == 1 or failed_attempts == 2:
            print(f"Warning: {3 - failed_attempts} attempts remaining.")
            passwordResetCheck = input("Would you like to reset your password? (yes/no): ")
            if passwordResetCheck.lower() == "yes":
                updated_password = passwordReset()
                if updated_password is not None:
                    currentPassword = updated_password
            else:
                access = False