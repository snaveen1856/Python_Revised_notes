# select fullname,gender, subject, score from student
# where gender = 'Male' and score > 90 and subject = 'maths':

# The cost of a stock every hour in a day is given in an array, find the maximum profit that you can make by buying
# and later selling in that day. For example, if the price of stock varies every hour in a day as
# [19, 21, 12, 13, 20, 6, 4, 8, 1], the maximum profit can be earned by buying on 3rd hour(12) and selling on 5th
# hour(20) Output : 20 - 12 = 8


rate = [19, 21, 12, 13, 20, 6, 4, 8, 1]
max_profit = 0
for i in range(len(rate)-1):
    other_val = max(rate[i+1:]) - rate[i]
    if max_profit < other_val:
        max_profit = other_val
print(max_profit)

