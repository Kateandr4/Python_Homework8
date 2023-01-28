def enter_example():
    exam = input('Введите пример: ')
    exam = exam.replace(' ', '').replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ')
    if exam.startswith(' - '):
        exam = '-' + exam[3:]
    exam = exam.split()    
    return exam
def print_example(my_list):
        print("ответ =", my_list[0])
 
