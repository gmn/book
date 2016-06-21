
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
    - on active set {active: 1}
    - on all finished
        - set {active: 0}
        - remove member_of
        - rewrite finished on finished items
    - remove index from all (if any)

"""

from datetime import datetime

class Date:
    fmt = "%a, %b %d %Y"
    dbfmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self, date=None, fmt=None):
        self.date = date if date else datetime.now()
        if fmt:
            (d, t)  = fmt.split(' ')
            self.date = datetime(*(int(s) for s in (d.split('-') + t.split(':'))))

    def str(self):
        return datetime.strftime(self.date, self.fmt)

    def __str__(self):
        return self.str()

    def db(self):
        return datetime.strftime(self.date, self.dbfmt)

d = Date()
print(str(d))
print(d.db())
