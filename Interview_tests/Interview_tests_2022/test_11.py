rates = [11, 2, 10, 15, 20, 13, 2]
times = [10, 11, 12, 13, 14, 15, 16]
dict_ = {}
for i in range(len(times)):
    key = times[i]
    value = rates[i]
    dict_[key] = value
# print(dict_)
selling_rate = {}
buying_rates = {}
max_ = max(dict_.values())
min_ = min(dict_.values())
for item in dict_:
    if max_ == dict_[item]:
        selling_rate[item] = max_
    elif min_ == dict_[item]:
        buying_rates[item] = min_
    else:
        pass
print(selling_rate, buying_rates)
print()
min_rate = min(rates)
max_rate = max(rates)
time_to_buy = times[rates.index(min_rate)]
time_to_sell = times[rates.index(max_rate)]
print(f"sell at : {time_to_sell} buy at : {time_to_buy}")

"""table1:

id, name, subject, location, marks
select * from student where location in ('India','USA') and subject = 'maths' and marks > 90;

"""