units=int(input("please enter number of units you consumed"))
if(units<50):
    amount=units*2.60
    surcharge=25
elif(units<=100):
    amount=130+((units-50)*3.25) 
    surcharage=35
elif(units<=200):
    amount=130+162.50+((units-100)*5.26) 
    surcharage=45
else:
    amount=130+162.50+526+((units-200)*8.45)
    surcharage=75
totalamount=amount+surcharage
total=amount + surcharage
print ("\nElectricity Bill=%.2f"%total)              