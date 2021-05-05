# Programe centeren on SAES
from utilities import Utilities
utilities = Utilities()

class SAES:
    def keyGeneration(self,input):
        # Step 1 w0 and w1
        w0 = input[:int(len(input) / 2)]
        w1 = input[int(len(input) / 2):]

        # Step 2 Calculating w2
        # w0 xor 1000 0000 xor Sub(Rot(w1))
        w1_rotated = utilities.rotate_value(w1)
        w1_sub = utilities.generate_substitution_from(w1_rotated)
        w2 = utilities.get_XOR_from(w0, w1_sub, "w2")
        
        # Step 3 Calculating w3
        # w3 = w2 XOR w1
        w3 = utilities.get_XOR_from(w2, w1, "w3")
        
        # Step 4
        # w2 XOR 0011 0000 XOR Sub(Rot(w3))
        w3_rot = utilities.rotate_value(w3)
        w3_sub = utilities.generate_substitution_from(w3_rot)
        w4 = utilities.get_XOR_from(w2, w3_sub, "w4")
        
        # Step 5
        # w5 = w4 XOR w3
        w5 = utilities.get_XOR_from(w4, w3)

        # Step 6
        k0 = w0 + w1
        k1 = w2 + w3
        k2 = w4 + w5

        return k0, k1, k2


    def get_saes_encryption(self, key0, key1, key2, plaintext):
        # Step 1 Add Round Key Block
        # Plaintext XOR k0
        step1_result = utilities.get_XOR_from(plaintext, key0)

        # Step 2: SubBytes Block
        block1 = utilities.generate_substitution_from(step1_result[:int(len(step1_result) / 2)])
        block2 = utilities.generate_substitution_from(step1_result[int(len(step1_result) / 2):])
        step2_result = block1 + block2
        
        # Step 3: Shitf Rows
        # Shifts blocks 2 and 4 from the previous result
        step3_result = utilities.shift_rows(step2_result)
        
        # Step 4: Mix Columns Bloc
        step4_result = utilities.generate_mix_columns_from(step3_result)
        
        # Step 5: Add Round Keys Block
        step5_result = utilities.get_XOR_from(step4_result, key1)
        
        # Step 6: Sub Bytes Block
        block1 = utilities.generate_substitution_from(step5_result[:int(len(step5_result) / 2)])
        block2 = utilities.generate_substitution_from(step5_result[int(len(step5_result) / 2):])
        step6_result = block1 + block2
        
        # Step 7: Shift Rows Block
        step7_result = utilities.shift_rows(step6_result)
        
        # Step 8: Add Round Key 2 block
        return utilities.get_XOR_from(step7_result, key2)


    def get_saes_decryption(self,key0, key1, key2, cyphertext):
        # Step 8: Add round key
        # step8_result = utilities.get_XOR_from(cyphertext, key2)
        step8_result = utilities.get_XOR_from(cyphertext, key2 )
        # Step 7: Shift Rows
        step7_result = utilities.shift_rows(step8_result)
        
        # Step 6: SubBytes
        block1 = utilities.generate_substitution_from(step7_result[:int(len(step7_result) / 2)], "d")
        block2 = utilities.generate_substitution_from(step7_result[int(len(step7_result) / 2):], "d")
        step6_result = block1 + block2

        # Step 5: Add round key1
        step5_result = utilities.get_XOR_from(step6_result, key1)

        # Step 4: Mix Columns
        step4_result = utilities.generate_mix_columns_from(step5_result, "d")
        
        # Step 3: Shift Row
        step3_result = utilities.shift_rows(step4_result)

        # Step 2: Sub Bytes
        block1 = utilities.generate_substitution_from(step3_result[:int(len(step3_result) / 2)], "d")
        block2 = utilities.generate_substitution_from(step3_result[int(len(step3_result) / 2):], "d")
        step2_result = block1 + block2

        # Step 1: Add Round Key1
        return utilities.get_XOR_from(step2_result, key0)

# s = Utilities()

# key0 = [int(x) for x in '1010010111110011']
# key1 = [int(x) for x in '1001001011000001']
# key2 = [int(x) for x in '1110101010001011']

# plaintext = [int(x) for x in '0000000000000111']

# cyphertext = [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]

# print(s.get_XOR_from(cyphertext, key2))
# print(s.get_XOR_from(step7_result, key2))