immutable_var = [2, 4, 5, 1, 55], 32323, 'pum-purum'
print(immutable_var)
#immutable_var[0] = 'wtf???'
#print(immutable_var)
# Элементы картежа нельзя менять, потому что картеж это неизменный элемент,
# который как раз и нужен для того, чтобы хранить в нём неизменный тип данных, например данные
# пользователя - его логин и пароль
a = 27
b = 34
mutable_list = [2, 4, 5, 1, 55, 32323, 'pum-purum', a*b]
print(mutable_list)
mutable_list .append('woody')
print(mutable_list)
mutable_list .remove(32323)
print(mutable_list)
mutable_list .remove([55][0])
print(mutable_list)