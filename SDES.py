from utilities import Utilities

utilities = Utilities()

class SDES:
    def keyGeneration(self, key):

        # Generating key 1
        k1_p10 = utilities.generate_p10_from(key)
        k1_p10 = utilities.shift_left(k1_p10, 1)
        k1_p8 = utilities.generate_p8_from(k1_p10)

        key1 = k1_p8

        # Generating key 2
        k2_shift_l1 = k1_p10
        k2_shift_l2 = utilities.shift_left(k2_shift_l1, 2)
        k2_p8 = utilities.generate_p8_from(k2_shift_l2)
        key2 = k2_p8

        return key1, key2

    def sdes_algorithm(self, plaintext, input_key1, input_key2, mode="encrypt"):
        key1 = input_key1 if mode == "encrypt" else input_key2
        key2 = input_key2 if mode == "encrypt" else input_key1

        ip_result = utilities.generate_ip_from(plaintext, False)
        left = ip_result[:int(len(ip_result) / 2)]
        right = ip_result[int(len(ip_result)/2): ]

        # Step 1 Expand and Permute over right
        expand_and_permute_result = utilities.generate_ep_from(right)

        # Step 2 Exclusive or between K1 and expand_and_permute_result
        exclusive_or_result = utilities.generate_exclusive_or_from(expand_and_permute_result, key1)

        # Step 3 Look up SBOX_SO and SBOX_S1
        sbox_look_up_result = utilities.generate_xbox_look_up_from(exclusive_or_result)

        # Step 4 Use the result from step 3 to generate p4
        p4_result = utilities.generate_p4_from(sbox_look_up_result)

        # Step 5 Exclusive or between Left and p4_result
        step5_result = utilities.generate_exclusive_or_from(p4_result, left)
        step5_result = step5_result + right

        # Step 6 Takes the input from the previous step and exchanges l for R
        left = step5_result[:int(len(step5_result) / 2)]
        right = step5_result[int(len(step5_result)/2):]

        left, right = right, left

        # Step 1 Expand and Permute over right
        expand_and_permute_result = utilities.generate_ep_from(right)

        # Step 2 Exclusive or between K1 and expand_and_permute_result
        exclusive_or_result = utilities.generate_exclusive_or_from(expand_and_permute_result, key2)

        # Step 3 Look up SBOX_SO and SBOX_S1
        sbox_look_up_result = utilities.generate_xbox_look_up_from(exclusive_or_result)

        # Step 4 Use the result from step 3 to generate p4
        p4_result = utilities.generate_p4_from(sbox_look_up_result)

        # Step 5 Exclusive or between Left and p4_result
        step5_result = utilities.generate_exclusive_or_from(p4_result, left)
        step5_result = step5_result + right

        # Generate cyphertext usin ip inverse
        return utilities.generate_ip_from(step5_result, True)




        