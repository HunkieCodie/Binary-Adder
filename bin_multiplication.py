# BINARY MULTIPLICATION - CPE401 LAB WORK 3
# NAME: SHITTU PROMISE ADURAGBEMI
# MATRIC NUMBER: CSC/2016/116

def binary_addition(a, b):
    """
        Binary addition.
        :param a: the first operand - a tuple of bits
        :param b: the second operand - a tuple of bits
        :type a: tuple
        :type b: tuple
        :return: the sum, as a tuple of bits
        :rtype: tuple
    """
    # first, ensure that the 2 arrays have the same number of bits,
    # by filling in with 0s on the left of the shortest operand
    diff = len(a) - len(b)

    if diff > 0:
        # concatenating a tuple of size <diff> with tuple b (all elements are 0s)
        b = ((0,) * diff) + b
    elif diff < 0:
        # concatenating a tuple of size <-diff> with tuple a (all elements are 0s)
        a = ((0,) * (-diff)) + a

    c = 0
    s = [0] * (len(a) + 1)
    for j in reversed(range(0, len(a))):
        d = (a[j] + b[j] + c) // 2
        s[j + 1] = (a[j] + b[j] + c) - 2 * d
        c = d
    s[0] = c

    # removing unneeded 0s on the left
    if s[0] == 0:
        s.remove(0)

    return tuple(s)


def shift_left(a, n):
    """
        Shift an array of bits to the L, by adding n 0s on the right.
        #. construct a tuple of n elements, all 0s
        #. concatenate it to the tuple that has been passed in
        #. return the concatenation

        :param a: a tuple of bits
        :param n: the number of positions over which to shift
        :type a: tuple
        :return: if n > 0, the L-shifted array; otherwise, the original array;
        *if the first parameter (`a` )
         is not of the `tuple` type, the function should handle it nicely and
         return an empty tuple. A test in the
         test suite below checks that this requirement has been met.*
        :rtype: tuple
    """
    if not isinstance(a, tuple): return ()
    return a + (0,) * n


def binary_multiplication(a, b):
    """
        Multiply arrays of bits.

        #. Initialize the cumulative sum of product (a tuple with 0 as its only
        element)

        #. Go over the bits in `b` (the second multiplicand), in *reverse order*:
         if current bit is 1, add to the cumulative sum the operand `a`,
         L-shifted by 0 for rightmost bit, by 1 for bit k-1, by 2 for bit k-2, ...

        #. return the cumulative sum

        :param a: first multiplicand - an array of bits
        :param b: second multiplicand - an array of bits
        :type a: tuple
        :type b: tuple
        :return: an array of bits
        :rtype: tuple
    """
    # initialize a null tuple of same size as a for the final sum
    s = (0,) * len(a)
    # take a copy of a for the intermediary products
    m = a[:]
    for i in reversed(range(len(b))):
        if b[i] != 0:  # when digit is one, add the intermediary product
            s = binary_addition(s, m)
        m = shift_left(m, 1)  # shift one per digit in b
    return s


def main():
    multiplicant = input("Enter first number: ")
    multiplier = input("Enter second number: ")
    print("Multiplicant = {}    [{} decimal]".format(multiplicant, int(multiplicant, 2)))
    print("Multiplier = {}    [{} decimal]".format(multiplier, int(multiplier, 2)))
    multiplicant_tuple = tuple([int(bit) for bit in multiplicant])
    multiplier_tuple = tuple([int(bit) for bit in multiplier])
    product = binary_multiplication(multiplicant_tuple, multiplier_tuple)
    product_ = ''.join([str(i) for i in product])
    print("--"*25)
    print("Result :\n\t{} X {} = {}    [{} decimal]".format(multiplicant, multiplier,
                                                            product_, int(product_, 2)))
    print("--"*25)


if __name__ == '__main__':
    main()
