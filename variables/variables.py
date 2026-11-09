# ============================================================
#  VARIABLES IN PYTHON  (run:  python variables.py)
#
#  A variable is a named "box" that stores a value
#  so you can use it again later.
# ============================================================

# ------------------------------------------------------------
# 1. CREATING VARIABLES
#    Format:  name = value
#    (no "let", "var", or type declaration needed)
# ------------------------------------------------------------
name = "Tharuka"        # str   -> text
age = 23                # int   -> whole number
height = 5.8            # float -> decimal number
is_student = True       # bool  -> True or False

print("Name:", name)
print("Age:", age)

# ------------------------------------------------------------
# 2. CHECK THE TYPE of a variable with type()
# ------------------------------------------------------------
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# ------------------------------------------------------------
# 3. RE-ASSIGN  (variables can change value)
# ------------------------------------------------------------
age = 24                 # age is now 24
print("New age:", age)

# ------------------------------------------------------------
# 4. NAMING RULES
#    - start with a letter or underscore (NOT a number)
#    - no spaces  -> use _ instead
#    - can't use Python keywords (if, for, while, class, def...)
#    - case-sensitive:  Age and age are DIFFERENT
# ------------------------------------------------------------
my_variable = 10         # good
my_variable_2 = 20       # good (underscore)
# 2nd_var = 30           # BAD: starts with a number
# my var = 40            # BAD: has a space

# ------------------------------------------------------------
# 5. STRINGS (text)
#    Combine strings with +  (called concatenation)
# ------------------------------------------------------------
first_name = "Tharuka"
last_name = "Perera"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# ------------------------------------------------------------
# 6. F-STRINGS  (the easy, modern way to mix text + variables)
#    Put an f before the quotes, and { } around each variable
# ------------------------------------------------------------
print(f"My name is {name} and I am {age} years old.")

# ------------------------------------------------------------
# 7. MULTIPLE ASSIGNMENT  (create several in one line)
# ------------------------------------------------------------
x, y, z = 1, 2, 3
print(x, y, z)           # 1 2 3

# ------------------------------------------------------------
# 8. CONSTANTS  (values that should NOT change)
#    Written in UPPER_CASE as a convention
# ------------------------------------------------------------
PI = 3.14159
MAX_USERS = 100
print("PI =", PI)

# ------------------------------------------------------------
# 9. COMMON MISTAKES TO AVOID
# ------------------------------------------------------------
# (a) using a variable before creating it  -> NameError
# (b) mixing str and int with +             -> TypeError
#       print("age is " + age)      # ERROR  (str + int)
#       print("age is " + str(age)) # OK     (convert to str)
print("age is " + str(age))   # works

# ------------------------------------------------------------
# 10. YOUR TURN
#     Create a variable with your city and print it
# ------------------------------------------------------------
# city = "Colombo"
# print("I live in", city)
