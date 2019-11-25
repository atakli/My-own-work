>>> import os
>>> d = os.listdir()
>>> len(d)
216
>>> for i in d:
...     if i[-7:-4] == '(2)':
...             os.remove(i)
# elhamdülillah. basit ama çok kullanışlı.
# automate boring stuff with python !!!