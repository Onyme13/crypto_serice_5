from DES_tables import *

test = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
test_c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

#GOOD
#Initial Permutation GOOD
def Initialization(Input):
    output = [2] * len(IP)

    for x in range(len(Input)):        
        output[x] =  Input[IP[x]-1]

    left_half = output[:32]
    right_half = output[32:]

    return left_half,right_half


"""======================================================================================="""

#GOOD
def key_generation(Key):

    keys= []
    output = [2] * len(Key)

    
    for x in range(len(PC_1)):
        output[x] = Key[PC_1[x]-1]
    left_half = output[0:28]
    right_half = output[28:56]



    for rotation in Rotations:
        #key permutation pc_1
        key = [2] * len(PC_2)

        #binary rotation
        left = left_half[rotation:] + left_half[0:rotation]
        right = right_half[rotation:] + right_half[0:rotation]

        full = left + right

        for x in range(len(PC_2)):
            key[x] = full[PC_2[x]-1]  
        keys.append(key)

    return keys

"""======================================================================================="""

#GOOD
def cipher_function(right_half, keys):
    
    R = [2] * len(E)
    output = ""
    

    #1 GOOD
    for x in range(len(E)):
        R[x] =  right_half[E[x]-1]

    #2 GOOD
    for x in range(len(R)):
        output += str(R[x] ^ keys[x])

    #3 GOOD
    A_list = [output[0:6],
    output[6:12],
    output[12:18],
    output[18:24],
    output[24:30],
    output[30:36],
    output[36:42],
    output[42:48]]
    A_replacement = ""


    for x in range(len(A_list)):

        y_value = int(A_list[x][0] + A_list[x][5],2)
        x_value = int(A_list[x][1:5],2)
        int_value_replacement = S_Boxes[x][y_value][x_value]
        bin_value_replacement = bin(int_value_replacement).replace("0b","") 

        while len(bin_value_replacement) < 4:
            bin_value_replacement = '0' + bin_value_replacement

        A_replacement += bin_value_replacement
    
    #4 GOOD
    final = [2] * len(P)

    for x in range(len(P)):
        final[x] = A_replacement[P[x]-1] 
    return final

"""======================================================================================="""


def encryption(Input,Key):
    x = 0
    key = key_generation(Key)                # génération des clés (liste)
    L, R = Initialization(Input) # première séparation  

    while x < 15:
        Lfinal = []

        Rxor = cipher_function(R,key[x])

        for i in range(len(Rxor)):
            Lfinal.append(L[i] ^ int(Rxor[i]))
        
        L = R
        R = Lfinal
        x+=1


    #round 16
    Rxor = cipher_function(R,key[x])
    Lfinal = []


    for i in range(len(Rxor)):
        Lfinal.append(L[i] ^ int(Rxor[i]))

    #Final permutation
    LplusR = Lfinal + R
    output_final = [2] * len(IP_Inverse)

    #GOOD
    for x in range(len(IP_Inverse)):
        output_final[x] = LplusR[IP_Inverse[x]-1]


    print("\n===============================================================================\n")
    print(output_final)
    print("\n===============================================================================\n")
    cipher_lisible = hex(int("".join(str(x) for x in output_final),2))
    print(cipher_lisible)

    return cipher_lisible

encryption(message_test,cle_test)



