﻿"""
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
Examples

2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"

"""

import unittest


class TestSnailSort(unittest.TestCase):
    def test_pick_peaks(self):
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")
        self.assertEqual(int32_to_ip(0), "0.0.0.0")


def DecimalToBinary(num):
    result = ""
    while (num > 0):
        rest = num % 2
        result = str(rest) + result
        num = num // 2
    return result


def int32_to_ip(int32):
    binary_repr = DecimalToBinary(int32)
    bin32 = "0" * (32 - len(binary_repr)) + binary_repr
    int(bin32[:8], 2)
    result = str(int(bin32[:8], 2)) + "." + str(int(bin32[8:16], 2)) + "." \
                                    + str(int(bin32[16:24], 2)) + "." + str(int(bin32[24:32], 2))
    return result


def main():
    unittest.main()
    pass


if __name__ == "__main__":
    main()
