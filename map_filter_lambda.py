#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
#----------------------------Пример 1------------------------------------------
def sq(x):
    return x**2  #дарачаи 2-ва мебардорад

a = [5, 4, 8, 4]

b = list(map(sq, a)) # мап худди for i in range боин хар як элементи списоки а-я мебенад
print(b)
#------------------------------------------------------------------------------------

#-------------------------------------Пример 2---------------------------------------#


a = ["how", "id", "name", "Hello"]
print(list(map(str.upper, a))) # map хар як элементи списока регистраша калон кард



"""filter"""
age = [22, 4, 55, 77, 14, 50, 21]
def is_adalt(age):
    return age >= 18
f = list(filter(is_adalt, age))
print(f)

is_adalt = lambda age: age >= 18
f = list(filter(is_adalt, age))
print(f)