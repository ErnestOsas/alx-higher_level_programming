#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    neu_liste = []
    for i in range(list_length):
        try:
            divi = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divi = 0
        except ZeroDivisionError:
            print("division by 0")
            divi = 0
        except IndexError:
            print("out of range")
            divi = 0
        finally:
            neu_liste.append(divi)
    return neu_liste
