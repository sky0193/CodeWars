"""
Simple Encryption #1 - Alternating Split
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""

def decrypt_one_time(encrypted_text):
    index_odd = 0
    index_even = len(encrypted_text) // 2 
    result = ""

    for i in range(0, index_even):
        result += encrypted_text[index_even + i]
        result += encrypted_text[index_odd + i]

    if(len(encrypted_text) % 2 == 1):
        result += encrypted_text[len(encrypted_text) - 1]
    return result

def decrypt(text, n):
    result = text
    for i in range(0, n):
        result = decrypt_one_time(result)
    return result

def encrypt_one_time(text):
    odd_indexes = text[1::2]
    even_indexes = text[0::2]
    return "".join(odd_indexes + even_indexes)

def encrypt(text, n):

    result = text
    for i in range(0, n):
        result = encrypt_one_time(result)
    return result

    
import unittest

class TestEncryption(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(encrypt("This is a test!", 3), " Tah itse sits!")
        self.assertEqual(encrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(encrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

        self.assertEqual(decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(decrypt(" Tah itse sits!", 3), "This is a test!")
        self.assertEqual(decrypt("This is a test!", 4), "This is a test!")
        self.assertEqual(decrypt("This is a test!", -1), "This is a test!")
        self.assertEqual(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

        self.assertEqual(encrypt("", 0), "")
        self.assertEqual(decrypt("", 0), "")
        self.assertEqual(encrypt(None, 0), None)
        self.assertEqual(decrypt(None, 0), None)


def main():
    unittest.main()


if __name__ == '__main__':
    main()