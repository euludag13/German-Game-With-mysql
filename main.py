import mysql.connector
import random


def query_data():
    mysql_con = db_connection()
    mysql_cursor = mysql_con.cursor()
    mysql_cursor.execute("SELECT * FROM words")
    data = mysql_cursor.fetchall()

    return data, mysql_con


def db_connection():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testdatabase"
    )

    return con


def main_game():
    data = query_data()[0]

    point = 0
    false_answers = 0

    while false_answers != 3:
        random_question = random.randint(0, len(data) - 1)
        print((data[random_question][1]).capitalize())
        answer = input("Enter Your Answer: ")
        if answer.lower() == data[random_question][2]:
            point += 1
        else:
            point -= 2
            false_answers += 1

    print()
    print("Your Point", point)


def add_data():
    connection = query_data()[1]
    cursor = connection.cursor()
    sql = "INSERT INTO words (german_word, turkish_word) VALUES (%s, %s)    "
    german = input("Enter German Word: ")
    turkish = input("Enter Turkish Word: ")
    val = (german.lower(), turkish.lower())
    cursor.execute(sql, val)

    connection.commit()


def main():
    choice_input = int(input("Select Your Choice 1 Add Words/ 2 Game:"))
    if choice_input == 1:
        add_data()
    else:
        main_game()


if __name__ == '__main__':
    main()
