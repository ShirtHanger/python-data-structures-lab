# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

students = ['Jotaro', 'Josuke', 'Giorno']

def manage_students():
    first_student = students[1]
    last_student = students[-1]
    return 'The first', first_student, 'the last', last_student
    # your code here

# Call the function and print the result
print('Exercise 1:', manage_students())
