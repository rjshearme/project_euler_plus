lexical_numbers = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
}

power_numbers = {
    100: "Hundred",
    1_000: "Thousand",
    1_000_000: "Million",
    1_000_000_000: "Billion",
}

def build_number_string(number):
    if number in lexical_numbers:
        return lexical_numbers[number]
    if number // 100:
        max_power = max(pow for pow in power_numbers if number - pow >= 0)
        multi, remainder = divmod(number, max_power)
        return build_number_string(multi) + " " + power_numbers[max_power] + " " + build_number_string(remainder)

    max_number = max(lex_num for lex_num in lexical_numbers if (number - lex_num) > 0)
    return lexical_numbers[max_number] + " " + build_number_string(number - max_number)
