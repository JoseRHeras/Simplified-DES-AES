import unittest
from SAES import SAES
from SDES import SDES


class TestSimplifiedAlgorithms(unittest.TestCase):

    def setUp(self):
        self.saes = SAES()
        self.sdes = SDES()

    # SAES Testting Section
    def test_saes_key_generation(self):
        key = "1010010111110011"
        expected = [[1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]]
        actual0, actual1, actual2 = self.saes.keyGeneration([int(x) for x in key])

        self.assertListEqual(expected[0], actual0)
        self.assertListEqual(expected[1], actual1)
        self.assertListEqual(expected[2], actual2)

        key = [int(x) for x in "1010010111110011"]
        key0, key1, key2 = [int(x) for x in "1010010111110011"], [int(x) for x in "1001001001100001"], [int(x) for x in "1110101010001011"]
        actual0, actual1, actual2 = self.saes.keyGeneration(key)
        self.assertListEqual(key0, actual0)
        self.assertListEqual(key1, actual1)
        self.assertListEqual(key2, actual2)


    def test_saes_encryption(self):
        plaintext, cyphertext = [int(x) for x in "1000010000100001"], [int(x) for x in "0000110010110011"]
        keys = [[1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]]
        actual = self.saes.get_saes_encryption(keys[0], keys[1], keys[2], plaintext)

        self.assertListEqual(actual, cyphertext)

        plaintext, cyphertext = [int(x) for x in "0000111100001111"], [int(x) for x in "0010010111000100"]
        key0, key1, key2 = [int(x) for x in "1010010111110011"], [int(x) for x in "1001001001100001"], [int(x) for x in "1110101010001011"]
        actual = self.saes.get_saes_encryption(key0, key1, key2, plaintext)

        self.assertListEqual(cyphertext, actual)

    def test_saes_decryption(self):
        keys = [[1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]]
        plaintext, cyphertext = [int(x) for x in "1000010000100001"], [int(x) for x in "0000110010110011"]
        actual = self.saes.get_saes_decryption(keys[0], keys[1], keys[2], cyphertext)

        self.assertListEqual(plaintext, actual)


        plaintext, cyphertext = [int(x) for x in "0000111100001111"], [int(x) for x in "0010010111000100"]
        key0, key1, key2 = [int(x) for x in "1010010111110011"], [int(x) for x in "1001001001100001"], [int(x) for x in "1110101010001011"]
        actual = self.saes.get_saes_decryption(key0, key1, key2, cyphertext)

        self.assertListEqual(plaintext, actual)


    def test_sdes_key_generation(self):
        main_key = [int(x) for x in "0000011111"]
        key0, key1 = [int(x) for x in "01101011"], [int(x) for x in "10101010"]

        actual0, actual1 = self.sdes.keyGeneration(main_key)

        self.assertListEqual(key0, actual0)
        self.assertListEqual(key1, actual1)


    def test_sdes_encryption(self):
        key0, key1 = [int(x) for x in "01101011"], [int(x) for x in "10101010"]
        plaintext = [int(x) for x in "11101110"]
        cyphertext = [int(x) for x in "01011101"]
        actual = self.sdes.sdes_algorithm(plaintext, key0, key1)

        self.assertListEqual(cyphertext, actual)

    def test_sdes_decryption(self):
        key0, key1 = [int(x) for x in "01101011"], [int(x) for x in "10101010"]
        plaintext = [int(x) for x in "11101110"]
        cyphertext = [int(x) for x in "01011101"]
        actual = self.sdes.sdes_algorithm(cyphertext, key0, key1, mode="decryption")

        self.assertListEqual(plaintext, actual)

if __name__ == "__main__":
    unittest.main()