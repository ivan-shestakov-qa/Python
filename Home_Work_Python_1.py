# 1) Создать переменную типа String
Name = "Ivan"
Surname = " Shestakov"
name = Name + Surname
print(type(name))
print("My name is " + name)

# 2) Создать переменную типа Integer
My_age = 37
Daughter = 17
Son = 20
Wife = 39
we = My_age + Daughter + Son + Wife
print(type(we))
print("Low age = " + str(we))

# 3) Создать переменную типа Float
my_weight = 74.2
daughter_weight = 50.5
son_weight = 80.4
wife_weight = 53.2
we_weight = my_weight + daughter_weight + son_weight + wife_weight
print(type(we_weight))
print("Low weight = " + str(we_weight))

# 4) Создать переменную типа Bytes
my_hd_d = bytes([70])
my_hd_e = bytes([75])
my_hd_f = bytes([80])
my_hd = my_hd_d + my_hd_e + my_hd_f
print(type(my_hd))
print("Low hd = " + str(my_hd))

# 5) Создать переменную типа List
age = list([My_age, Daughter, Son, Wife])
cat_1 = 14
cat_2 = 13
age.extend([cat_1, cat_2])
print(type(age))
print(age)

# 6) Создать переменную типа Tuple
def get_user():
    name = "Ivan"
    age_my = 37
    is_married = True
    return name, age_my, is_married

user = get_user()
print(type(user))
print(user)

# 7) Создать переменную типа Set
family = set(["Ivan", "Elena","Viktor","Dariya"])
family.add("Cat-Niusha")
family.add("Cat-Plathon")
print(type(family))
print(family)

# 8) Создать переменную типа Frozen set
address = frozenset(["56", "Gagarin street", "Mogilev", "Belarus"]) # Выявлено что тип внутренних скобок не важен
print(type(address))
print(str(len(address)) + " objects per line")
print(address)

# 9) Создать переменную типа Dict
names = {"Vanya":37, "Elena":39, "Viktor":20, "Dariya":17}
print(type(names))

print(names)