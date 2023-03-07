
# *****************************
# Make your Code



#2
flag = 0 
counter = 0  
iterations = 10
iseven = False

for i in range(iterations):
    usernum = int(input('Enter a number: '))
    if (usernum % 2 == 0 ):
        iseven = True
    else: 
        iseven = False
    if (flag == 1 and iseven == True):
        counter += 1 
    if (iseven == True): 
        flag += 1 
    else:
        flag = 0
print (counter)

    
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
