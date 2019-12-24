# Finding BMI of persons using function assignment
def bmi(w, h):
    x = h.split('.')
    a = int(x[0])
    b = int(x[1])
    h1 = (a * 0.304) + (b * 0.0304)
    b = round(w / (h1 ** 2))
    return b


L = {}
data = []
a = []
b = []
c = []
for i in range(6):
    name = input('Enter a name:')
    if not name:
        break
    h = str(input('Enter the height in feets:'))
    h1 = float(h)
    w = int(input('Enter the weight in kgs:'))
    data.append(h1)
    data.append(w)
    k = bmi(w, h)
    data.append(k)
    L[name] = data.copy()
    data.clear()
print(L)
for s in L.keys():
    n = L[s][2]
    if n < 18:
        a.append(s)
    elif 18.5 < n < 25:
        b.append(s)
    else:
        c.append(s)
print('Under Weight: ', a)
print('Normal Weight:', b)
print('Over weight:  ', c)
