# mimimum denominations required

amount = 11
denomination_count = 0

if 500 <= amount:
    denomination_count += amount // 500
    amount %= 500
if 200 <= amount < 500:
    denomination_count += amount // 200
    amount %= 200
if 100 <= amount < 200:
    denomination_count += amount // 100
    amount %= 100
if 50 <= amount < 100:
    denomination_count += amount // 50
    amount %= 50
if 20 <= amount < 50:
    denomination_count += amount // 20
    amount %= 20
if 10 <= amount < 20:
    denomination_count += amount // 10
    amount %= 10
if 5 <= amount < 10:
    denomination_count += amount // 5
    amount %= 5
if 2 <= amount < 5:
    denomination_count += amount // 2
    amount %= 2
if 1 <= amount < 2:
    denomination_count += amount // 1
    amount %= 1
print('The minimum denomination count is ', denomination_count)
