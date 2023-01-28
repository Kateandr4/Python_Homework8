#my_list = []

def calcul(my_list: list):
#    global my_list
    #res = 0
    i = 0
    while len(my_list) > 1:
        while '*' in my_list or '/' in my_list:
            while i < len(my_list):
                if my_list[i] == '*' :
                    my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
                    del my_list[i]
                    del my_list[i]
                elif my_list[i] == '/' :
                    my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
                    del my_list[i]
                    del my_list[i]
                i+=1
        while '+' in my_list or '-' in my_list:
            i = 0
            while i <  len(my_list):
                if my_list[i] == '+':
                    my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
                    del my_list[i]
                    del my_list[i]
                elif my_list[i] == '-':
                    my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
                    del my_list[i]
                    del my_list[i]
                i+=1
    return my_list