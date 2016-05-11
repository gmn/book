
# mostly this app is to keep track of what I'm reading and reading next.

# SCHEMA
## lists:
- reading
- want_to_read
- reading_next
## list:
-_t:list
- name
- books[]
## book:
- t:book
- title
- added
- author            optional
- finished          how to tell if its finished, is unset until completion,
- comments          optional
- rating            optional
- year              optional

------------
DB
- list of books
    _id
    title, author, added,
    finished, year,
    comments, rating
- list of lists
    _id
    name
    books[]
- books[]
    { book_id : N, index : M }
- index count upwards consequitively starting from 1, eg. 1,2,3
- a book can be in 0 to many lists, but not in a list more than once

INTERFACE
[x] need way to CRUD lists - immediate cmdline
[x] need way to CRUD books - immediate cmdline
[x] need way to manage what list(s) a book is in
[x] need way to view books in each list
[x] need way to CRUD book - interactive
[x] need way to CRUD list - interactive
[x] list books by author
[x] list all books in order added
[x] list all lists
------------

TODO:
[x] books listing needs to display each list a book is a member of
[x] way to list by author
[x] book: short format, 1-line
[x] way to rm book from list
[x] way to delete book
[ ] way to edit + delete list
[ ] show books that are finished
[x] sub-flags for each command such as: -l <limit> -o <order>
[ ] date pretty print
[x] edit book


