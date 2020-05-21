import random
f = open('tetx.txt')
nlist= f.read().split()
print(f'В списке ',len(nlist),' имён')
int_num=int(input('Какое число случайных имён Вы хотите получить:'))
1
def randname(int_num,nlist):
    rand_nlist = []
    for i in range(int_num):
        num_name=nlist[random.randint(0,len(nlist)-1)]
        rand_nlist.append(num_name)
    return rand_nlist

def how_often(list_in):

    max_of=0
    min_of = len(list_in)
    often=[]
    rare=[]
    temp_set=set(list_in)
    for i in temp_set:
        name_count=list_in.count(i)
        if max_of < name_count:
            max_of = name_count
            often.clear()
            often.append(i)
        elif max_of == name_count:
            often.append(i)
        elif min_of==name_count:
            rare.append(i)
        elif min_of > name_count:
            min_of = name_count
            rare.clear()
            rare.append(i)
        else:
            continue
    return often,rare

def rare_letter(list_in):
    temp_list=list(map(lambda list_in: list_in[0],list_in))
    letter=how_often(temp_list)[1]
    return letter

rand_nlist=randname(int_num,nlist)
print(rand_nlist)
print(f'частые в полученном списке',how_often(rand_nlist)[0])
print(f'редкие буквы с которых начинаются имена в полученном списке',rare_letter(rand_nlist))