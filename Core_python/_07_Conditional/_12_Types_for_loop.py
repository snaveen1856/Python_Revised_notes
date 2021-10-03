# different loops with enumerate and zip

names = ['Peter parker', 'Steve Rogers', 'Tony Stark', 'Bruce Wyans', 'Vin Diesel']
heros = ['Spider-man', 'Captain America', 'Iron man', 'Bat-man', 'Fast and Furious']
studios = ['Sony', 'Marvel', 'Marvel', 'DC comics', 'Paramount']
count = 0
print('--------------Normal For loop------------')
for name in names:
    hero = heros[count]
    print(f" '{name}' is actually '{hero}' ")
    count += 1
print()
print('----------For loop using Enumerate-------------')
for index, name in enumerate(names):
    hero = heros[index]
    print(f" '{name}' is actually '{hero}' ")

print()
print('------------For loop using Zip-------------')
for name, hero in zip(names, heros):
    print(f" '{name}' is actually '{hero}' ")
print('---------------------------------------------------')
for name, hero, owned in zip(names, heros, studios):
    print(f" '{name}' is actually '{hero}' from '{owned}' ")
print()
print('------------Unpacking of tuple-------------')
for value in zip(names, heros, studios):
    print(value)
print(type(value))
