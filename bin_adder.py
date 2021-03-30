# PROGRAMMING A BINARY ADDER - CPE401 LAB WORK
# NAME: SHITTU PROMISE ADURAGBEMI
# MATRIC NUMBER: CSC/2016/116


# Function to format both inputs to the same number of digits
def rjust_length(s1, s2, fill="0"):
    l1, l2 = len(s1), len(s2)
    if l1 > l2:
        s2 = s2.rjust(l1, fill)
    elif l2 > l1:
        s1 = s1.rjust(l2, fill)
    return (s1, s2)


# Function to get inputs
def get_inputs():
    bits_a = input("Input your first binary string:  ")
    bits_b = input("Input your second binary string: ")
    return rjust_length(bits_a, bits_b)


# Defining XOR function.
def xor(bit_a, bit_b):
    A1 = bit_a and (not bit_b)
    A2 = (not bit_a) and bit_b
    return int(A1 or A2)


# Defining a half adder which is a XOR to give you a summed output and an AND # to give you a carry. It will have 2 inputs (bit_a, bit_b) and gives two
# outputs the XOR for sum and the AND for carry.
def half_adder(bit_a, bit_b):
    return xor(bit_a, bit_b), bit_a and bit_b


# Define a full Adder which is two half adders. It will have 3 inputs
# (bit_a, bit_b, carry) and two outputs (sum and carry).
def full_adder(bit_a, bit_b, carry=0):
    sum1, carry1 = half_adder(bit_a, bit_b)
    sum2, carry2 = half_adder(sum1, carry)
    return sum2, carry1 or carry2


# Lastly, we call this full adder, starting at the Least Significant Bit
# (LSB), with 0 as carry, and work our way to the Most Significant Bit (MSB)
# where we carry the carry as input to the next step.
def binary_string_adder(bits_a, bits_b):
    carry = 0
    result = """"""
    for i in range(len(bits_a)-1 , -1, -1):
        sum_, carry = full_adder(int(bits_a[i]), int(bits_b[i]), carry)
        result += str(sum_)
    result += str(carry)
    return result[::-1]


# Main function to run the code.
def main():
    bits_a, bits_b = get_inputs()
    try:
        print("1st string of bits is : {}, ({})".format(bits_a, int(bits_a, 2)))
        print("2nd string of bits is : {}, ({})".format(bits_b, int(bits_b, 2)))
        result = binary_string_adder(bits_a, bits_b)
        print("--" * 20)
        print("Final Adder Result is : {}, ({})".format(result, int(result, 2)))
        print("—-" * 20)
    except ValueError:
        print("Error in input. Input should be in binary - should contain zero and/or ones.")


if __name__ == "__main__":
    main()
