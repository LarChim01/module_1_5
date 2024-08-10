# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
print ("immutable_var переменная типа tuple" )
immutable_var =  50 , ["Это","список"], True, 5*5
print (immutable_var)
# immutable_var [0] = 10
# закоментировано, чтобы выполнить оставшуюся часть задания, при выполнении ошибка
# так как В переменных типа "tuple " можно менять только элементы типа "list"
# Traceback (most recent call last):
#   File "E:\pyton\pythonProject\module_1_5.py", line 5, in <module>
#     immutable_var [0] = 10
#     ~~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
##


immutable_var[1][1] = " можно  изменить"
print (immutable_var)
# Создание изменяемых структур данных:
print ("immutable_list переменная типа tuple состоящая из двух списков")
mutable_list= ["Это","список"], ["Тоже " ," список"]
print(mutable_list)
mutable_list[1][0] = "Да"
mutable_list[0][0:1]="Новый"
mutable_list[0].append(" добавили")
mutable_list[0][2]= "Изменили"

print(mutable_list)