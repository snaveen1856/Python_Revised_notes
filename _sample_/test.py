D = {}
op_hrs = [7, 7, 7, 11, 15, 10, 17]
cl_hrs = [19, 19, 19, 19, 15, 10, 7]
d = ['mon', 'tue', 'wed', 'thr', 'fri', 'sat', 'sun']
for i in range(7):
    if op_hrs[i] < cl_hrs[i]:
        print(d[i], ':', op_hrs[i], '--', cl_hrs[i])
        k = op_hrs[i] - cl_hrs[i]
        D[d[i]] = -k
    elif op_hrs[i] > cl_hrs[i]:
        k = 'closed'
        D[d[i]] = k
        print(d[i], ':', 'Closed')
    else:
        print(d[i], ':', 'Opened 24 hrs')
        k = 'Opened 24 hrs'
        D[d[i]] = k
t = list(set(D.values()))
print(t)
for a in t:
    if a == 12:
        print('Mon-Wed', ':', op_hrs[0], '-', cl_hrs[0])
        break
    elif a == 8:
        print('Thr', ':', op_hrs[3], '-', cl_hrs[3])
    else:
        print()
