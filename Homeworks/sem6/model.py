import sqlite3


def connect_to_bd():
    con = sqlite3.connect('pb.db')
    cur = con.cursor()
    return [con, cur]


lst1 = connect_to_bd()
conn = lst1[0]
cursor = lst1[1]


def search_in_bd(line):
    data = [row for row in cursor.execute('SELECT * FROM phone_book ORDER BY id')]
    b = ''
    for i in range(len(data)):
        if (line.lower() in data[i][1].lower()) or (line in data[i][2]):
            b = b + str(data[i][0]) + '. ' + data[i][1] + ': ' + data[i][2] + '\n'
    if len(b) == 0:
        return 'Nothing found'
    else:
        return b


def find_position(column, pos):
    return cursor.execute(f"SELECT {column} FROM phone_book where id = {pos}").fetchall()[0][0]


def update_bd(fio, numb, pos):
    cursor.execute(
        f"UPDATE phone_book SET FIO = '{fio}',number = '{numb}' WHERE id = {pos}")
    conn.commit()


def add_contact_to_bd(fio, numb):
    cursor.execute(
        f"INSERT INTO phone_book (FIO, number) VALUES ('{fio}', '{numb}')")
    conn.commit()


def delete_from_bd(pos):
    conn.execute(f"DELETE FROM phone_book WHERE id = {pos}")
    conn.commit()


def show_bd():
    data = [row for row in cursor.execute(
        'SELECT * FROM phone_book ORDER BY id')]
    b = ''
    for i in range(len(data)):
        b = b + str(data[i][0]) + '. ' + data[i][1] + ': ' + data[i][2] + '\n'
    return b
