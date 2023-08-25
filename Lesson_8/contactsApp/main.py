import sqlite3 as sq

with sq.connect("contacts.db") as con:
    cur = con.cursor()
    def create_table():
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            org TEXT,
            telephone INTEGER
        )""")
        # cur.execute("DROP TABLE contacts")
        con.commit()
    def show():
        cur.execute("SELECT * FROM contacts")
        for row in cur.fetchall():
            print(row)

    def add_into_empty(data_list):
        cur.execute("SELECT * FROM contacts")
        cur.execute("INSERT INTO contacts (name, surname, org, telephone) VALUES(?, ?, ?, ?)", data_list[0])
        con.commit()


while True:
    create_table()
    command = input('Введите команду:\n'
                    '/show - просмотр контактов\n'
                    '/add - добавить контакт\n'                    
                    '/search - поиск\n')
    if command == '/show':
        show()
    if command == '/add':
        input_contact = tuple()
        list_contact = []
        name_contact = input('Введите имя контакта:\n')
        surname_contact = input('Введите фамилию контакта:\n')
        org_contact = input('Введите название организации:\n')
        tel_contact = input('Введите номер телефона:\n')
        input_contact = (name_contact, surname_contact, org_contact, tel_contact)
        list_contact.append(input_contact)
        add_into_empty(list_contact)
