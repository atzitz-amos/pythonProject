

power_converter = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}


def convert_number_to_power(number):
    s = str(number)
    if s == "1":
        return ""
    power = ""
    for char in s:
        power += power_converter[char]
    return power
