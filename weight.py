Weight = int(input("Weight : ")) 
unit = input("(K)g or (L)bs : ") 
if unit.upper() == "K":
    A = Weight / 0.45
    print("weight in Lbs : " + str(A))
else:
    A = Weight * 0.45
    print("weight in Kgs : " + str(A))
