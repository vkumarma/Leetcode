#!/usr/bin/env python3
def numberToWords(num) -> str:

    hash = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

    l = list(hash.keys())
    words = []
    i = len(l) - 1

    if num == 0: return "Zero"

    def recurse(n, l, words, i):
        if n >= 1 and n <= 20:
            words.append(hash[n])
            return

        if l[i] > n:
            recurse(n, l, words, i-1)

        else:
            q = n // l[i]
            r = n % l[i]
            if q in hash and q < 100:
                if n >= 100:
                    words.append(hash[q])
            else:
                recurse(q, l, words, i-1)
            words.append(hash[l[i]])

            if r != 0:
                recurse(r, l, words, i-1)

    recurse(num, l, words, i)
    sentence = " ".join(words)
    return sentence


entry = input("Enter a number or q for exit: ")
while True:
    if entry == "Q" or entry == "q": break
    print(numberToWords(int(entry)))
    print("\n")
    entry = input("Enter a number or q for exit: ")
    
    
