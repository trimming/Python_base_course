import sqlite3 as sq
import json

with sq.connect("contacts.db") as con:
    cur = con.cursor()
    def create_table():
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            org TEXT,
            tel TEXT
        )""")
        con.commit()
        # cur.execute("DROP TABLE contacts")
    def show(show_command):
        cur.execute(show_command)
        for row in cur.fetchall():
            print(f"{row[0]}. {row[1]} {row[2]} {row[3]} {row[4]}")

    def add_into_empty(data_list):
        cur.execute("SELECT * FROM contacts")
        cur.execute("INSERT INTO contacts (name, surname, org, tel) VALUES(?, ?, ?, ?)", data_list)
        print("Контакт сохранен.")
        con.commit()
    def do_contact_edit(command_edit):
        cur.execute(command_edit)

    def import_contacts():
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        with open("my_contacts.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(rows, ensure_ascii=False))
            print("Контакты успешно импортированы в my_contacts.json")

while True:
    create_table()
    command = input('Введите команду:\n'
                    '/show - просмотр контактов\n'
                    '/add - добавить контакт\n'                    
                    '/search - поиск\n'
                    '/import - импортировать контакты\n'
                    '/end - выйти\n')
    if command == '/show':
        show("SELECT * FROM contacts")
    elif command == '/add':
        name_contact = input('Введите имя контакта:\n')
        surname_contact = input('Введите фамилию контакта:\n')
        org_contact = input('Введите название организации:\n')
        tel_contact = input('Введите номер телефона:\n')
        temp = (name_contact, surname_contact, org_contact, tel_contact)
        add_into_empty(temp)
    elif command == '/search':
        param = input("Введите параметр поиска:\n"
                      "name - Имя\n"
                      "surname - Фамилия\n"
                      "org - Организация\n"
                      "tel - Телефон\n")
        search_name = input(f"Введите {param}:\n")
        show(f"SELECT * FROM contacts WHERE {param} LIKE '{search_name}%'")
        options = input("Желаете удалить или изменить контакт?\n"
                        "1 - Удалить\n"
                        "2 - Изменить\n"
                        "3 - Назад\n")
        if options == '1':
            do_contact_edit(f"DELETE FROM contacts WHERE {param} LIKE '{search_name}%'")
            print(f"Контакт с именем {search_name} удален.")
        if options == '2':
            edit = []
            edit.append(input("Какую информацию вы хотите изменить?\n"
                              "name - Имя\n"
                              "surname - Фамилию\n"
                              "org - Организацию\n"
                              "tel - Телефон\n"))
            edit.append(input("Введите новое значение:\n"))
            do_contact_edit(f"UPDATE contacts SET {edit[0]}='{edit[1]}' WHERE {param} LIKE '{search_name}%'")
            print("Контакт изменен.")
        else:
            continue
    elif command == '/import':
        import_contacts()
    elif command == '/end':
        break
    else:
        print('Неопознанная команда, попробуйте еще раз.')
