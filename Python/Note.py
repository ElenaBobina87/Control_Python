import json
from datetime import datetime
import os


class Note:

    
    
   
    def create_note():
        title = input("Введите заголовок заметки: ")
        body = input("Введите содержимое заметки: ")
        notes = Note.find_all_notes()  
        data = {}
        data['id'] = len(notes) + 1
        data['Title'] = title
        data['Text'] = body
        data['Date'] = datetime.now().date().isoformat()
        data['Time'] = datetime.now().time().isoformat()
        
        notes.append(data)   
        
        with open("my_note.json", "w") as file:
            
            json.dump(notes, file, indent=4)
        
        
        print("Заметка сохранена")
    

    def note_print(note):
        print("ID = ", note['id'])
        print("Заголовок: ", note['Title'])
        print("Содержимое: ", note['Text'])
        print("Создана ", note['Time'], note['Date'])

    def find_all_notes():
        if os.path.exists("my_note.json"):
            with open("my_note.json", "r") as file:
                notes = json.load(file)
                
                return notes
        else:
            return []
        


    def write_note():
        if os.path.exists("my_note.json"):
            notes = Note.find_all_notes()
            return notes
        else:
            return []

    def find_date(date):
        notes = Note.find_all_notes()
        notes_for_date = []
        for note in notes:
            if note['Date'] == date:
                notes_for_date.append(note)
        return notes_for_date 

    def find_id(id):
        notes = Note.find_all_notes()
        
        for note in notes:
            if note['id'] == id:
                Note.note_print(note)
                return note
        print('Заметка не найдена')

    def del_note(id):
        notes = Note.find_all_notes()
        new_notes = []
        for note in notes:
            if note['id'] != id:
                new_notes.append(note)
        with open('my_note.json', 'w') as file:
            json.dump(new_notes, file, indent=4)
        print("Заметка удалена")
        return new_notes

    def edit_note(id):
        notes = Note.find_all_notes()
        for note in notes:
            if note['id'] == id:
                title = input('Введите новый заголовок: ')
                if title != "":
                    note['Title'] = title
                body = input('Введите новое содержание заметки: ')
                if body != "":
                    note['Text'] = body
                note['Date'] = datetime.now().time().isoformat()
                note['Time'] = datetime.now().date().isoformat()
        with open('my_note.json', 'w') as file:
            json.dump(notes, file, indent=4)
        print('Заметка отредактирована')
        
           
           
        

