units = {
        0: 0,
        1: 3, #one
        2: 3, #two
        3: 5, #three
        4: 4, #four
        5: 4, #five
        6: 3, #six
        7: 5, #seven
        8: 5, #eight
        9: 4, #nine
        }
hundreds = units

dozens = {
        10: 3, #ten
        11: 6, #eleven
        12: 6, #twelve
        13: 8, #thirteen
        14: 8, #fourteen
        15: 7, #fifteen
        16: 7, #sixteen
        17: 9, #seventeen
        18: 8, #eighteen
        19: 8, #nineteen
        }

tens = {
        0: 0,
        20: 6, #twenty
        30: 6, #thirty
        40: 5, #forty
        50: 5, #fifty
        60: 5, #sixty
        70: 7, #seventy
        80: 6, #eighty
        90: 6, #ninety
        }

end = 3
hundred = 7

def construct(i1, i2, i3):
    result = hundreds[i1]
    if result > 0:
        if i2 + i3 > 0:
            result += end
        result += hundred

    if 9 < (i2 * 10 + i3) < 20:
        return result + dozens[i2 * 10 + i3]
    else:
        return result + tens[i2 * 10] + units[i3] 

res = 0
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            res += construct(i1, i2, i3)
            
print(construct(3, 4, 2))
print(construct(1, 1, 5))
one_thousand = 3 + 8
print(res + one_thousand)
