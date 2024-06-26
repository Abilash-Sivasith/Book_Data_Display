"""
Reads books data and gives graphs with usefull infomation

Created By:
Abilash Sivasith
"""

import pandas as pd
import matplotlib.pyplot as plt
import math
import pip

pip.main(['install', 'openpyxl'])
import random

EXCEL_FILENAME = "books_I_want_to_read.xlsx"


def open_excel():
    """opens the excell file"""
    excel_file = pd.read_excel(EXCEL_FILENAME)
    return excel_file


def workable_file():
    """turns the provided excell file into a workable format"""
    excel_file_to_read = open_excel()
    book_info_list = []
    i = 0
    for index, row in excel_file_to_read.iterrows():
        book_name = row['Title']
        book_authors = (row['Author 1'], row['Author 2'])
        book_genre = (row['Genre 1'], row['Genre 2'])
        book_read = row['Read']
        book_owned = row['Owned']
        book_year_read = row['Year Read']
        tuple_of_book_info = (book_name, book_authors, book_genre, book_read, book_owned, book_year_read)
        book_info_list.append(tuple_of_book_info)
    return book_info_list


def graph_per_genre():
    """graph books based on main genre"""
    book_data_list = workable_file()
    dict_of_genre = {}
    for data in book_data_list:
        genre = data[2][0]
        if genre not in dict_of_genre:
            dict_of_genre[genre] = 1
        else:
            dict_of_genre[genre] += 1

    genre_as_list = []
    for genre in dict_of_genre.keys():
        genre_as_list.append((str(genre)))
    #genre_as_list = [str(genre) for genre in dict_of_genre.keys()]
    num_book_in_genre = list(dict_of_genre.values())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(genre_as_list, num_book_in_genre, color='blue', width=0.4)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Genres")
    plt.ylabel("# Books in Genre")
    plt.title("Books Per Genre")
    plt.show()


def graph_per_genre_read():
    """graph read books based on main genre"""
    book_data_list = workable_file()
    dict_of_genre = dict()
    dict_fiction_non_fiction = {"Fiction": 0, "Non-Fiction": 0}
    for data in book_data_list:
        genre = data[2][0]
        read_status = data[5]
        if isinstance(read_status, (int, float)) and not math.isnan(read_status):

            if genre not in dict_of_genre:
                dict_of_genre[genre] = 1
            else:
                dict_of_genre[genre] += 1

            if genre == "fiction":
                dict_fiction_non_fiction['Fiction'] += 1
            else:
                dict_fiction_non_fiction['Non-Fiction'] += 1

    # Graphing Read Books Per Genre
    genre_as_list = list(dict_of_genre.keys())
    num_book_in_genre = list(dict_of_genre.values())
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.bar(genre_as_list, num_book_in_genre, color='blue', width=0.4)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Genres")
    plt.ylabel("# Books in Genre")
    plt.title("Read Books Per Genre")
    plt.show()
    fiction_vs_non_fiction = list(dict_fiction_non_fiction.keys())
    num_books_in_fiction_vs_non_fiction = list(dict_fiction_non_fiction.values())
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.bar(fiction_vs_non_fiction, num_books_in_fiction_vs_non_fiction, color='blue', width=0.4)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("# Books in Genre")
    plt.title("Read Books Split By Fiction and Non-Fiction")
    plt.show()


def books_per_year():
    """graphs the books read based on the year"""
    book_data_list = workable_file()
    dict_of_read_book_per_year = dict()
    for data in book_data_list:
        year_read = data[5]
        if isinstance(year_read, (int, float)) and not math.isnan(year_read):
            year_read = int(year_read)
            if year_read not in dict_of_read_book_per_year:
                dict_of_read_book_per_year[year_read] = 1
            else:
                dict_of_read_book_per_year[year_read] += 1

    years = list(dict_of_read_book_per_year.keys())
    num_books_in_year = list(dict_of_read_book_per_year.values())
    plt.figure(figsize=(10, 7))
    plt.plot(years, num_books_in_year, marker='o', linestyle='-')
    plt.xlabel("Year")
    plt.ylabel("# Books Read")
    plt.title("Books Read per Year")
    plt.grid(True)
    plt.ylim(0, max(num_books_in_year) + 2)
    plt.yticks(range(0, max(num_books_in_year) + 5, 1))
    plt.xticks(range(min(years), max(years) + 1, 1))
    plt.show()


def random_book_generator():
    """returns a random book from books thats are unread"""
    book_data_filtered_by_read = read_book_filter()
    random_int = random.randint(0, len(book_data_filtered_by_read))
    tittle, authors_tuple, genres, _ = book_data_filtered_by_read[random_int]
    if str(authors_tuple[1]) in ["nan", "NaN"]:
        string_to_print = f"I think you should read {tittle} by {authors_tuple[0]}"
    else:
        string_to_print = f"I think you should read {tittle} by {authors_tuple[0]} and {authors_tuple[1]}"

    print(string_to_print)


def read_book_filter():
    """returns a list of tuples with the (books, (authors1, author2), genre, owned) info """
    book_data_list = workable_file()
    books_data_after_read_books_filtered_out = []
    for data in book_data_list:
        tittle, authors, genres, have_read, owned, _ = data
        if have_read == 'NO':
            books_data_after_read_books_filtered_out.append((tittle, authors, genres, owned))

    return books_data_after_read_books_filtered_out


def main():
    """main loop with what data you want to display"""
    #graph_per_genre()
    #graph_per_genre_read()
    random_book_generator()


main()
