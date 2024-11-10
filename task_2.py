# TODO Напишите функцию find_common_participants

def find_common_participants(list1, list2, separator=","):
    #if separator == None: separator = ","

    list1 = list1.split(separator)
    list2 = list2.split(separator)
    a = list(set(list1) & set(list2))
    a = sorted(a)
    return a


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

#f = find_common_participants(participants_first_group, participants_second_group,"|")
#print(f)

