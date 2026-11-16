from csv import reader
import xml.dom.minidom as minidom
import random

def count_title():
    count = 0
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        for row in table:
            title_length = row[2].lower()
            if len(title_length) > 30:
                count += 1

    print(count)

def book_search():
    while True:
        flag = 0

        search = input('Введите запрос: ')
        if search == '0':
            break

        with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
            table = reader(csvfile, delimiter=';')
            next(table)

            for row in table:
                lower_case = row[2].lower()

                try:
                    year = int(row[3])
                except ValueError:
                    continue

                if search.lower() == lower_case and 1991 <= year <= 1994:
                    print(row[1])
                    flag += 1


            if flag == 0:
                print('Ничего не найдено.')
            else:
                print(f'Найдено {flag} результатов.')

def link_generator():
    books = []

    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

        for row in table:
            try:
                year = int(row[3])
            except ValueError:
                continue

            author = row[2].strip()
            title = row[1].strip()

            if author and title:
                citation = f"{author}. {title} - {year}"
                books.append(citation)

    if len(books) < 20:
        print("Not enough books to generate 20 unique citations.")
        return
    else:
        selected_books = random.sample(books, 20)

        with open("bibliography.txt", "w", encoding="utf-8") as file:
            for number, citation in enumerate(selected_books, 1):
                file.write(f"{number}. {citation}\n")

def parse_xml():
    dom = minidom.parse("currency.xml")
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    code_dict = []

    for node in elements:
        char_code_node = node.getElementsByTagName("CharCode")[0]
        nominal_node = node.getElementsByTagName("Nominal")[0]

        nominal = int(nominal_node.firstChild.data)
        char_code = char_code_node.firstChild.data

        if nominal == 10 or nominal == 100:
            code_dict.append(char_code)

    print(code_dict)

def publishers():
    publisher_set = set()

    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        next(table)

        for row in table:
            if len(row) > 4:
                publisher_set.add(row[4].strip())

    for publisher in sorted(publisher_set):
        print(publisher)

    print("Total unique publishers:", len(publisher_set))


def main():
    count_title()
    #book_search()
    #link_generator()
    parse_xml()
    publishers()

if __name__ == '__main__':
    main()