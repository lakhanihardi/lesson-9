medical_cause=input("did you have a medical cause y or n:")
atten=int(input("enter the attendance of the student:"))
if medical_cause=='y':
    print("you are allowed")
else:
    if atten >=75:
        print("allowed") 
    else:
        print("not allowed")       