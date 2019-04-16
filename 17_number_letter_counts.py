
def number_words_count(n):
    dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
            14: 'forteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninty'}
    return len(dict[n])

if __name__ == "__main__":
    result = 0
    for i in range(1,1001):
        if i == 1000:
            result += len('onethousand')
            continue

        if i // 100 > 0:
            result += number_words_count(i//100) + 7

        if i % 100 > 0:
            result += 3
            x = i % 100
            if x <= 20:
                result += number_words_count(x)
            else:
                result += number_words_count((x//10)*10)
                if x % 10 > 0:
                    result += number_words_count(x%10)

    print(result)