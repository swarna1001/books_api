from django.db.models.aggregates import Count
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Book

import csv

# Create your views here.


def clean_data():
    datafile = open(
        "C:/Users/Administrator/Desktop/books/main_dataset_edited.csv", newline='')

    # create a dictReader object
    my_reader = csv.DictReader(datafile)

    book_dict = {}

    book_list = {}
    count = 0

    for row in my_reader:
        #print(row['name'], row['author'], row['isbn'], row['img_paths'])
        count = count+1
        """book_dict.update({count:
                          {'name': row['name'], 'author': row['author'], 'isbn': row['isbn']}})"""

        """book_dict.update({count:
                          {row['name'], row['author'],  row['isbn']}})"""

        Book.objects.create(
            name=row['name'], image=row['img_paths'],
            author=row['author'], isbn=row['isbn'], category=row['category'])

        # book_list.append(book_ob)

    # print(book_dict)

        # print(book_list)

    # datafile.close()

    # print(book_dict)


def nested_dict_values_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all values of given dictionary
    for value in dict_obj.values():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for v in nested_dict_values_iterator(value):
                yield v
        else:
            # If value is not dict type then yield the value
            yield value


def update_database():

    count = 32582

    books = clean_data()

    some_list = []

    # for i in range(1, count):
    for num, value in books.items():
        print(num, ":", value)

        for val in value:
            print(val)

            # Book.objects.create()


def book(request):

    clean_data()
    print("1111111111111111111111111")
    # print(ab)

    """for value in nested_dict_values_iterator(ab):
        print(value)"""

    # update_database()

    """Book.objects.create(name="swarna3", image="book_images/0000001.jpg",
                        author="me", isbn="4587878999", category="moron")"""

    return HttpResponse("<h1> hello </h1>")
