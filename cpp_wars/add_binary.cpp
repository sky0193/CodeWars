#include <bitset>
#include <iostream>
#include <string>
#include <assert.h>  

/**
 * @brief Implement a function that adds two numbers together and returns their sum in binary.
 * The conversion can be done before, or after the addition.
 *
 * The binary number returned should be a string.
 *
 * Examples:(Input1, Input2 --> Output (explanation)))
 *
 * @param a  Input1
 * @param b  Input2
 * @return binaryAsString  Output
 */

std::string add_binary(uint64_t a, uint64_t b)
{
    auto sum = a + b;

    if (sum == 0)
    {
        return "0";
    }

    auto binaryAsString = std::bitset<64>(sum).to_string();
    binaryAsString.erase(0, binaryAsString.find_first_not_of('0'));
    return binaryAsString;
}

/**
 * @brief Implement a function that adds two numbers together and returns their sum in binary.
 * The conversion can be done before, or after the addition.
 *
 * The binary number returned should be a string.
 *
 * Examples:(Input1, Input2 --> Output (explanation)))
 *
 * @param a  Input1
 * @param b  Input2
 * @return output  Output
 */

std::string add_binary_2(uint64_t a, uint64_t b)
{
    a += b;
    std::string output;

    do
    {
        output = std::to_string(a % 2) + output;
        a /= 2;
    } while (a > 0);

    return output;
}

int main()
{
    uint64_t numberA = 89;
    uint64_t numberB = 1;

    assert (add_binary(numberA, numberB) == "1011010");
    
    return 0;
}