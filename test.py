
BOOKS_PATH = '/home/gnaughto/Private/logs/databases/books.json'
QUERYABLE_PATH = '/home/gnaughto/code/pyqueryable'

import sys
sys.path.append(QUERYABLE_PATH)
from Queryable import db_object

# globals
p    = lambda X: print( str(X) )
db   = db_object(path=BOOKS_PATH, jsonarg={'sort_keys':True,'indent':2}).load()

res = db.find({'title':'32 oz. narrow VitaMix pitcher'})

print( str(res.data) )
