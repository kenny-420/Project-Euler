_1_to_9 = sum(len(i) for i in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

_10_to_19 = sum(len(i) for i in ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",  "sixteen", "seventeen", "eighteen", "nineteen"])

_20_to_99 = 0
for i in ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]:
    _20_to_99 += len(i)*10 + _1_to_9

_1_to_99 = _1_to_9 + _10_to_19 + _20_to_99

_100_to_999 = 0
for i in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
    _100_to_999 += len(i) + len("hundred") + \
            (len(i) + len("hundredand")) * 99 + \
            _1_to_99

_1_to_1000 = _1_to_99 + _100_to_999 + len("onethousand")
print(_1_to_1000)
