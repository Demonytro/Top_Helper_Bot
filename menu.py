"""Menu"""

from my_calc import main as my_calc_main               #----почему при старте запускается--- как запустить
from sort import main as sort_main                      #------ как передать путь
# from notebook1.notebook_main import main as nb_main     #----- init.py
from note_ex import main as nb_main                      # ---------  образцы команд
from contacts_book_classes import main as ab_main        # ----------- нет основной логики и команд



def main_menu():

    work_loop = True
    while work_loop:
        user_input = input('Menu press button\n1 - AdressBook\n2 - NoteBook\n3 - FileSorter\n4 - Calculator\n0 - Exit\n\nBot waiting ... type command >>> ')
        if user_input == "1":            # 1 - AdressBook
            print('Start AdressBook application')
            ab_main()
            print('Finish AdressBook application')
        elif user_input == "2":    # 2 - NoteBook
            print('Start NoteBook application')
            nb_main()
            print('Finish NoteBook application')
        elif user_input == "3":    # 3 - FileSorter
            print('Start FileSorter application')
# ------------------------------------------------  argv[1] =  file_path = input("input folder path")
            sort_main()
            print('Finish FileSorter application')
            pass
        elif user_input == "4":      # 4 - Calculator
            print('Start Calculator application')
            my_calc_main()
            print('Finish Calculator application')
        elif user_input == 5:
            pass
        elif user_input == 6:
            pass
        elif user_input == '0':
            work_loop = False
        else:
            continue
    
    pass #не забываем оценить работу Помощника     Надеюсь, до новых Встреч





if __name__ == '__main__':
    main_menu()