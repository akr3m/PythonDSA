def convert_decimal_to_binary(decimal):
    assert decimal >= 0 and int(decimal) == decimal, 'number must be a positive integer'
    if decimal == 0:
        return 0
    elif decimal == 1:
        return 1
    else:
        # 5 ---> 101
        # 5 / 2 --> quotient = 2; remainder = 1
        # 2 / 2 --> quotient = 1; remainder = 0

        # 14 ---> 1101
        # 14 / 2 --> quotient = 7; remainder = 0
        # 7 / 2 --> quotient = 3; remainder = 1
        # 3 / 2 --> quotient = 1; remainder 1

        # 17 ---> 10001
        # 17 / 2 -->    quotient = 8; remainder = 1
        # 8 / 2 -->     quotient = 4; remainder = 0
        # 4 / 2 -->     quotient = 2; remainder = 0
        # 2 / 2 -->     quotient = 1; remainder = 0

        return convert_decimal_to_binary(int(decimal / 2))*10 + (decimal % 2)


arr = [5, 13, 2, 1, 0, 17]
for a in arr:
    print('a = ' + str(a) + '\tconvert_decimal_to_binary(arr) = ' + str(convert_decimal_to_binary(a)))


