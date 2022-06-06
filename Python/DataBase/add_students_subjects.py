import cs50
from cs50 import SQL


open('list_of_classes.db', 'w')
db = SQL('sqlite:///list_of_classes.db')


student_name = input('Type in the full name (and the family name) of the student\n')
list_of_subjects = input('Type in all the subjects this students has participated in, \
                         separate them by commmas\n').split(',')


id = db.execute('INSERT INTO students (student) VALUES(?)', student_name)
for subject in list_of_subjects:
    id_class = db.execute('INSERT INTO classes (class) VALUES(?)', subject)

close('list_of_classes.db')
