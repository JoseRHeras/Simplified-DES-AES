class Utilities:
    W2_CONSTANT = [1, 0, 0, 0, 0, 0, 0, 0]
    W4_CONSTANT = [0, 0, 1, 1, 0, 0, 0, 0]
    
    BINARY_CONVERSION = {
         "0000": 0, "0001" : 1, "0010": 2, "0011": 3,
         "0100": 4, "0101": 5, "0110" : 6, "0111": 7,
         "1000": 8, "1001": 9, "1010": 10, "1011": 11,
         "1100": 12, "1101": 13, "1110": 14, "1111": 15
     }

    KEY_GEN_AND_ENCRYPTIION_SBOX = {
        "0000": "1001", "0001" : "0100", "0010": "1010", "0011": "1011",
        "0100": "1101", "0101": "0001", "0110" : "1000", "0111": "0101",
        "1000": "0110", "1001": "0010", "1010": "0000", "1011": "0011",
        "1100": "1100", "1101": "1110", "1110": "1111", "1111": "0111"
    }

    DENCRYPTIION_SBOX = {
        "0000": "1010", "0001" : "0101", "0010": "1001", "0011": "1011",
        "0100": "0001", "0101": "0111", "0110" : "1000", "0111": "1111",
        "1000": "0110", "1001": "0000", "1010": "0010", "1011": "0011",
        "1100": "1100", "1101": "0100", "1110": "1101", "1111": "1110"
    }

    MULTIPLICATION_TABLE = {
        "21": 2, "22": 4, "23": 6, "24": 8, "25": 10, "26": 12, "27": 14, "28": 3, "29": 1, "210": 7, "211" : 5, "212": 11, "213": 9, "214": 15, "215": 13,
        "41": 4, "42": 8, "43": 12, "44": 3, "45": 7, "46": 11, "47": 15, "48": 6, "49": 2, "410": 14, "411": 10, "412": 5, "413":1, "414": 13, "415": 9,
        "91": 9, "92": 1, "93": 8, "94": 2, "95":11, "96": 3, "97": 10, "98": 4, "99": 13, "910": 5, "911": 12, "912": 6, "913": 15, "914": 7, "915": 14,
        "1": 1, "0": 0
    }

    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    p4 = [2, 4, 3, 1]
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inverse = [4, 1, 3, 5, 7, 2, 8, 6]

    sbox_s0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]

    sbox_s1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]

    # Generators
    def generate_p10_from(self, key):
        result = []
        for e in self.p10:
            result.append(key[e - 1])
        
        return result

    def generate_p8_from(self, key):
        result = []
        for e in self.p8:
            result.append(key[e - 1])
        return result

    def generate_ip_from(self, input, is_inverse):
        key = self.ip_inverse if is_inverse else self.ip
        result = []
        for e in key:
            result.append(input[e - 1])

        return result

    def generate_ep_from(self, input):
        result = []

        for e in self.ep:
            result.append(input[e - 1])
        return result

    def generate_exclusive_or_from(self, input1, input2):
        result = []
        for i in range(len(input1)):
            if input1[i] == input2[i]:
                result.append(0)
            else:
                result.append(1)

        return result

    def generate_p4_from(self, input):
        p4_result = []

        for e in self.p4:
            p4_result.append(input[e - 1])

        return p4_result

    def generate_xbox_look_up_from(self, input):
        def get_str_bin_value(string):
            if string == "00":
                return 0
            elif string == "01":
                return  1
            elif string == "10":
                return  2
            else:
                return  3

        def get_array_val(input):
            if input == 0:
                return [0, 0]
            elif input == 1:
                return [0, 1]
            elif input == 2:
                return [1, 0]
            else:
                return [1, 1]

        left = input[:int(len(input) / 2)]
        right = input[int(len(input)/2):]

        result = []

        for i in range(2):
            table = self.sbox_s0 if i == 0 else self.sbox_s1
            arr = left if i == 0 else right
            
            col = str(arr[1]) + str(arr[2])
            col = get_str_bin_value(col)

            row = str(arr[0]) + str(arr[3])
            row = get_str_bin_value(row)

            val = table[row][col]
            
            result += get_array_val(val)
        
        return result

    def shift_left(self, key, number_of_shifts):
        left = []
        right = []

        for index, e in enumerate(key):
            if index < len(key) / 2:
                left.append(e)
            else:
                right.append(e)


        for i in range(number_of_shifts):
            left_element = left.pop(0)
            right_element = right.pop(0)

            
            left.append(left_element)
            right.append(right_element)

        return left + right

    def rotate_value(self, input):
        left = input[:int(len(input) / 2)]
        right = input[int(len(input) / 2) :]

        return right + left

    def generate_substitution_from(self, input, mode="e"):
        table = self.KEY_GEN_AND_ENCRYPTIION_SBOX if mode == "e" else self.DENCRYPTIION_SBOX

        left_row, left_col = str(input[0]) + str(input[1]), str(input[2]) + str(input[3])
        right_row, right_col = str(input[4]) + str(input[5]), str(input[6]) + str(input[7])

        sbox_val_1 = table[left_row + left_col]
        sbox_val_2 = table[right_row + right_col]
        
        return [int(x) for x in sbox_val_1] + [int(x) for x in sbox_val_2]

    def get_XOR_from(self, input1, input2, operation_type=""):
        def get_XOR(a, b):
            tem_result = []
            for i in range(len(a)):
                if a[i] == b[i]:
                    tem_result.append(0)
                else:
                    tem_result.append(1)
            return tem_result
        
        side_one = input1
        if operation_type == "w2":
            side_one = get_XOR(self.W2_CONSTANT, input1)
        elif operation_type == "w4":
            side_one = get_XOR(self.W4_CONSTANT, input1)
        
        return get_XOR(side_one, input2)

    def shift_rows(self, input):
        return input[:4] + input[12:] + input[8:12] + input[4:8]
               
    def generate_mix_columns_from(self, input, mode="e"):
        
        def get_value(left, right):
            key = str(left) + str(right)
            if key in self.MULTIPLICATION_TABLE:
                return self.MULTIPLICATION_TABLE[key]
            
            key = str(right) + str(left)
            if key in self.MULTIPLICATION_TABLE:
                return self.MULTIPLICATION_TABLE[key]

            
            return left * right

        def convert_to_binary(input):
            num = str(bin(input))[2:]
            if len(num) < 4:
                num = ("0" * (4 - len(num))) + num

            return num


        a = self.BINARY_CONVERSION["".join([str(x) for x in input[:4]])]
        b = self.BINARY_CONVERSION["".join([str(x) for x in input[4:8]])]
        c = self.BINARY_CONVERSION["".join([str(x) for x in input[8:12]])]
        d = self.BINARY_CONVERSION["".join([str(x) for x in input[12:]])]
        
        result = []
        ls = 1 if mode == "e" else 9
        ls1 = 4 if mode == "e" else 2
        # section one
        left_side = convert_to_binary(get_value(a, ls))
        right_side = convert_to_binary(get_value(ls1, b))
        result += self.get_XOR_from(left_side, right_side)

        
        # Section two
        ls = 4 if mode == "e" else 2
        ls1 = 1 if mode == "e" else 9
        left_side = convert_to_binary(get_value(a, ls))
        right_side = convert_to_binary(get_value(b, ls1))
        result += self.get_XOR_from(left_side, right_side)

        # Section three
        ls = 1 if mode == "e" else 9
        ls1 = 4 if mode == "e" else 2
        left_side = convert_to_binary(get_value(c, ls))
        right_side = convert_to_binary(get_value(ls1, d))
        result += self.get_XOR_from(left_side, right_side)

        # Section four
        ls = 4 if mode == "e" else 2
        ls1 = 1 if mode == "e" else 9
        left_side = convert_to_binary(get_value(c, ls))
        right_side = convert_to_binary(get_value(d, ls1))

        result += self.get_XOR_from(left_side, right_side)
        
        return result