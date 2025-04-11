with open("chapter9\\practice_set\\09_problem\\old.txt", "r") as f:
    content = f.read()
    # Rename the file
with open("chapter9\\practice_set\\09_problem\\renamed.txt", "w") as f:
    f.write(content)
#  ^^^^^^^^^^^^^^^^^^^^^^^^^ABOVE CODE WILL NOT DELETE THE OLD FILE BUT CREATE A NEW ONE^^^^^^^^^^^^^^^^^^^^^^^^^


#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^FOLLOWING CODE WILL DELETE THE OLD FILE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# import os
# os.rename("chapter9\\practice_set\\09_problem\\old.txt", "chapter9\\practice_set\\09_problem\\renamed.txt")