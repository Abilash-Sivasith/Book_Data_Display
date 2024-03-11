"""
Reads books data and gives graphs with usefull infomation

Created By:
Abilash Sivasith
"""

import pandas as pd
from pprint import pprint

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
    pprint(book_info_list)
        

            
            
    
    
    '''book_title = excel_file_to_read['Tittle']
    # Sets the author as a tuple
    author_1 = excel_file_to_read['Author 1']
    author_2 = excel_file_to_read['Author 2']
    if author_2 == 'NaN':
        author = (author_1)
    else:
        author = (author_1, author_2)
    # line_num_as_int = excel_file[excel_file['Tittle'] == "Atomic Habits"].index[0]
    '''
    
workable_file()

def graph_per_genre():
    """graph books based on main genre"""
    pass

def graph_per_genre_read():
    """graph read books based on main genre"""
    pass

def graph_per_genre_unread():
    """graph unread books based on main genre"""
    pass


def books_per_year():
    """graphs books read per year"""
    pass


def main():
    """main loop with what data you want to display"""
    pass


