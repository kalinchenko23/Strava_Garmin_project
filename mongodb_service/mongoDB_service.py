import pathlib

import mongoengine

db= mongoengine.connect("myfirstdb")
print(db)
