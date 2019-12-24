# Reverse the given number and sum of given number digits

n = int(input('Enter a number:'))
digit_sum = 0
rev_num = 0
while n > 0:
    div = n % 10
    digit_sum = digit_sum + div
    rev_num = rev_num * 10 + div
    n = n // 10

print('Sum of digits of given number:', digit_sum)
print('Reverse of given number:', rev_num)
