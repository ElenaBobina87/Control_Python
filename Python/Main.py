from Note import *


class Main:
    while True:
        print('Введите цифру, соответствующую выбраному действию:')
        print('1 - добавить заметку')
        print('2 - удалить заметку')
        print('3 - редактировать заметку')
        print('4 - найти заметку по ID')
        print('5 - найти заметки по дате')
        print('6 - вывести все заметки')
        print('7 - выйти из программы')
        command = input()
        if command == '1':
            Note.create_note()
            
        elif command == '2':
            id = int(input('Введите id заметки, которую хотите удалить: '))
            Note.del_note(id)
            
        elif command == '3':
            id = int(input('Введите id заметки, которую хотите редактировать: '))
            Note.edit_note(id)
            
        elif command == '4':
            id = int(input('Введите id заметки, которую хотите найти: '))
            Note.find_id(id)
           
        elif command == '5':
            date = input('Введите дату: ')
            list_for_date = Note.find_date(date)
            for note in list_for_date:
                Note.note_print(note)
            
        elif command == '6':
            notes = Note.find_all_notes()
            for note in notes:
                
                Note.note_print(note)
            
        elif command == '7':
            break
        else:
            print('Такой команды нет')
            


