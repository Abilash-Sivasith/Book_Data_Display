"""
Reads books data and gives graphs with usefull infomation

Created By:
Abilash Sivasith
"""

import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

EXCEL_FILENAME = "books_I_want_to_read.xlsx"

def open_excel():
    """opens the excell file"""
    excel_file = pd.read_excel(EXCEL_FILENAME)
    return excel_file


def workable_file():
    """turns the provided excell file into a worksable format"""
    excel_file_to_read = open_excel()
    book_info_list = []
    i = 0 
    for index, row in excel_file_to_read.iterrows():
        book_name = row['Tittle']
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
        title = data[0]
        genre = data[2][0]
        if genre not in dict_of_genre:
            dict_of_genre[genre] = 1
        else:
            dict_of_genre[genre] += 1
        genre_as_list = list(dict_of_genre.keys())
    num_book_in_genre = list(dict_of_genre.values())
    fig, ax = plt.subplots(figsize= (10,5))
    ax.bar(genre_as_list, num_book_in_genre, color = 'blue', width= 0.4)
    plt.xticks(rotation=45, ha="right") 
    plt.xlabel("Genres")
    plt.ylabel("# Books in Genre")
    plt.title("Books Per Genre")
    
    plt.show()
    
    return dict_of_genre

            

def graph_per_genre_read():
    """graph read books based on main genre"""
    pass


def books_per_year():
    """graphs books read per year"""
    pass


def main():
    """main loop with what data you want to display"""
    pass


