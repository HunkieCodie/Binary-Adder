# BINARY DIVISION - CPE401 LAB WORK 4
# NAME: SHITTU PROMISE ADURAGBEMI
# MATRIC NUMBER: CSC/2016/116

dividend = input("Enter dividend in binary: ")
divisor = input("Enter divisor in binary: ")

dividend_to_int = int(dividend, 2)
divisor_to_int = int(divisor, 2)

result_in_int = int(dividend_to_int/divisor_to_int)
remainder_in_int = int(dividend_to_int % divisor_to_int)

result_in_bin = bin(result_in_int)[2:]
remainder_in_bin = bin(remainder_in_int)[2:]

print("--"*20)
print("{}  ({})\tdivided by\t{}  ({})\n\nequals:\n\t\tQUOTIENT: {}"
      "  ({})\n\t\tREMAINDER: {}  ({})\n{}".format(dividend,
                                                   dividend_to_int,
                                                   divisor,
                                                   divisor_to_int,
                                                   result_in_bin,
                                                   result_in_int,
                                                   remainder_in_bin,
                                                   remainder_in_int,
                                                   "--"*20))


