#Prompt the user for a mass as an integer(in kilograms) and then outputs the equaivlent number of Joules as an ineger, assuming the user will input and integer.
Mass = input("M: ")
mc = int(Mass) * pow(300000000, 2)
print("E: " + str(mc))
