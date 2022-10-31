from DES_tables import IP


#Initial Permutation
def Initialization(Input):
    output = [0] * len(IP)

    for x in range(len(Input)):
        output[IP[x]-1] = Input[x]

    half = len(Input)/2
    left_half = output[0:half]
    right_half = output[half:len(IP)+1]

    return left_half,right_half




