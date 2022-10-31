from ssl import AlertDescription
from traceback import print_tb
from DES_tables import *


#Initial Permutation
def Initialization(Input):
    output = [0] * len(IP)

    for x in range(len(Input)):
        output[IP[x]-1] = Input[x]

    half = int(len(Input)/2)
    left_half = output[0:half]
    right_half = output[half:len(IP)+1]

    return left_half,right_half

Initialization([40,8,48,16,56,24,64,32,
              39,7,47,15,55,23,63,31,
              38,6,46,14,54,22,62,30,
              37,5,45,13,53,21,61,29,
              36,4,44,12,52,20,60,28,
              35,3,43,11,51,19,59,27,
              34,2,42,10,50,18,58,26,
              33,1,41,9,49,17,57,25])


"""======================================================================================="""

def key_generation(Key):

    keys= []

    for rotation in Rotations:
        #key permutation pc_1
        output = [0] * len(Key)

        for x in range(len(PC_1)):
            output[PC_1[x]-1] = Key[x]

        left_half = output[0:29]
        right_half = output[28:]

        #binary rotation
        for i in range(len(left_half)):
            left = [0] * len(left_half)
            left[i-rotation] = left_half[i]

        for i in range(len(right_half)):
            right = [0] * len(right_half)
            right[i-rotation] = right_half[i]

        full = left + right

        #permutation pc_2
        for x in range(len(PC_2)):
            output[PC_2[x]-1] = Key[x]

        keys.append(output)
    
    print("Liste des cles:\n")
    print(keys)
    return keys


"""======================================================================================="""

def cipher_function(keys, right_half):
    
    R = [0] * len(E)
    output = [] * len(R)

    #1
    for x in range(len(PC_1)):
        R[E[x]-1] = right_half[x]
    
    #2    
    for x in range(len(keys)):
        output[x] = R[x] ^ keys[x]

    #3   
    A_list = [output[0:7],
    output[6:13],
    output[12:19],
    output[18:25],
    output[24:31],
    output[30:37],
    output[36:43],
    output[42:49]]

    A_replacement = ""

    for x in range(len(A_list)):
        y_value = int(A_list[x][0] + A_list[x][5],2)
        x_value = int(A_list[x][0:5],2)

        int_value_replacement = S_Boxes[x][x_value][y_value]
        A_replacement += (bin(int_value_replacement).replace("0b",""))
    
    #4
    final = [] * len(A_replacement)
    
    for x in range(len(P)):
        final[P[x]-1] = A_replacement[x]

    return final