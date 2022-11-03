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


"""======================================================================================="""

def key_generation(Key):

    keys= []

    for rotation in Rotations:
        #key permutation pc_1
        output = Key
        #key = [2] * 48
        key = []


        for x in range(len(PC_1)):
            output[PC_1[x]-1] = Key[x]

        left_half = output[0:28]
        right_half = output[28:56]



        #binary rotation
        left = left_half[rotation:] + left_half[0:rotation]
        right = right_half[rotation:] + right_half[0:rotation]
        
        for i in range(len(right_half)):
            right = right_half
            right[i-rotation] = right_half[i]

        full = left + right

        for x in range(len(PC_2)):
            key.insert(PC_2[x]-1,full[x])

        keys.append(key)
    return keys


"""======================================================================================="""
"""!!!!!!!!!!!!! conversion to INT !!!!!!!!!!!!!!!!!!!"""

def cipher_function(keys, right_half):
    
    R = [0] * len(E)
    output = ""
    
    #1
    for x in range(len(E)):
        R[E[x]-1] = right_half[x % (len(right_half))]
    #print(len(R))
    #print(len(keys))
    #print(len(output))

    #2    
    for x in range(len(R)):
        output += str(R[x] ^ keys[x])

    #3   
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
        #print(y_value)
        #print(x_value)


        int_value_replacement = S_Boxes[x][y_value][x_value]
        bin_value_replacement = bin(int_value_replacement).replace("0b","") 

        if len(bin_value_replacement) < 4:
            bin_value_replacement = '0' + bin_value_replacement

        A_replacement += bin_value_replacement
    #4
    final = []
    
    print(len(A_replacement))
    for x in range(len(P)):
        final.insert(P[x]-1, A_replacement[x])

    return final

"""======================================================================================="""
"""TypeError: unsupported operand type(s) for ^: 'list' and 'list'"""

"""def round(Left,Right,Key):
    #effectue le round
    
    Rtemp = Right

    R_xor_int = []
    R_xor = cipher_function(Key,Rtemp)

    #cipher function
    for x in range(len(R_xor)):
        R_xor_int.append(int(R_xor[x]))       

    Lfinal = []
    
    #XOR
    for x in range(len(R_xor_int)):
        Lfinal.append(Left[x] ^ R_xor_int[x])    
        
    #croisement
    Rfinal = Lfinal
    Lfinal = Right

    return Lfinal, Rfinal
"""



def encryption(Input,Key):
    x = 0
    key = key_generation(Key)                # génération des clés 

    first_L, first_R = Initialization(Input) # première séparation  

    #premier round


    """
    for x in range (len(key)):

         for x in range(len(first_R)): 

             R_croise = cipher_function(key[0],first_R)
             R_croise_int = [] 

             for x in range(len(R_croise)):
                 R_croise_int.append(int(R_croise[x]))       
             L = first_L^R_croise_int    
             R = first_L


             R_croise = cipher_function(key[x+1],R)
             L = L^R_croise    
             R = L
        """
    #Final permutation
    LplusR = L + R
    output_final = []   

    for x in range(len(LplusR)):
        output_final.insert([IP_Inverse[x]-1], LplusR[x])

    print("\n===============================================================================\n")
    print(output_final)

    return output_final

encryption(message_test,cle_test)



