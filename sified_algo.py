import sys
from SAES import SAES
from SDES import SDES

def simplified_des(input):
    sdes = SDES()
    
    if len(input) == 5 and "d" in input:
        cyphertext = [int(x) for x in input[2]]
        k1 = [int(x) for x in input[3]]
        k2 = [int(x) for x in input[4]]
        print(sdes.sdes_algorithm(cyphertext, k1, k2, mode="decrypt"))

    elif len(input) == 5 and "e" in input:
        plaintext = [int(x) for x in input[2]]
        k1 = [int(x) for x in input[3]]
        k2 = [int(x) for x in input[4]]

        print(sdes.sdes_algorithm(plaintext, k1, k2, mode="encrypt"))
    elif len(input) == 3 and "kg" in input: 
        key = [int(x) for x in input[2]]
        print(sdes.keyGeneration(key))

def simplified_aes(input):
    saes = SAES()
    output = []

    if len(input) == 6 and input[1] == "d":
        k0 = [int(x) for x in input[2]]
        k1 = [int(x) for x in input[3]]
        k2 = [int(x) for x in input[4]]
        cyphertext = [int(x) for x in input[5]]
        output = saes.get_saes_decryption(k0, k1, k2, cyphertext)
    elif len(input) == 6 and input[1] == "e":
        k0 = [int(x) for x in input[2]]
        k1 = [int(x) for x in input[3]]
        k2 = [int(x) for x in input[4]]
        plaintext = [int(x) for x in input[5]]
        output = saes.get_saes_encryption(k0, k1, k2, plaintext)
    elif len(input) == 3 and input[1] == "kg":
        key = [int(x) for x in input[2]]
        output = saes.keyGeneration(key)

    print(output)
    
def main_function(input):
    
    if len(input) == 1:
        with open("F:\Projects\PythonProjects\Cryptography\instructions.txt", 'r') as f:
            print(f.read())
    elif len(input) >= 4:
        
        if input[1] == "sdes":
            simplified_des(input[1:])
        elif input[1] == "saes":
            simplified_aes(input[1:])

if __name__ == "__main__":
    main_function(sys.argv)
