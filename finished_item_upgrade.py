
"""
# Date() class, that
#     - stores the: "yyyy-mm-ddThh:mm:ss" string
#     - supports a .str() method for str(Date)
#     - supports now()

# finish_item()
#     to do: insert these into item
#
#     active: False,
#     finished: [ {'d':date,'l':[id,id,id]}, {'d':date,'l':[id,id,id]} ]

# new_item()
#     // on create, add this member:
#     active: True
#
#     // looks for item w/ matching title and active==False before creating new one
#     // If not found, a new one is created. This way, items can be reused but we still will only ever create as many new items as we need. Some items will be created and finished, created and finished, multiple times. Each one, adds an entry to the finished array.
#
#     // the Finished array is unset when the item is created. It is created on first finish, with one entry

#* EVERYWHERE
#    - everywhere the "finished" is checked, now we must check active==True instead

* DATABASE - write a tiny script to
    x on active set {active: 1}
    x on all finished
        x set {active: 0}
        x remove member_of
        x rewrite finished on finished items
    x remove index from all (if any)
    - rewrite dates to be in dbfmt = '%Y-%m-%d %H:%M:%S'
"""

from json import loads, dumps
with open( '/home/gnaughto/Private/logs/databases/todo.json' ) as f:
    blob = f.read()
rows = loads(blob)

jarg = {'sort_keys':True, 'indent':2}

for row in rows:
    if row.get('_t') and row.get('_t') == 'list':
        continue

    fin = row.get('finished')

    if row.get('index'):
        del row['index']

    if row.get('added'):
        row['added'] = row['added'].replace('T', ' ')[:19]

    if not fin:
        row['active'] = 1
        continue
    else:
        row['active'] = 0
        fin = fin.replace('T', ' ')[:19]

    member_of = row.get('member_of',[])
    new_fin = []
    new_fin.append( {'d':fin, 'l':member_of} )
    row['finished'] = new_fin
    if member_of:
        del row['member_of']

with open( './todo_fixed.json', 'w') as f:
    f.write(dumps(rows, **jarg))
