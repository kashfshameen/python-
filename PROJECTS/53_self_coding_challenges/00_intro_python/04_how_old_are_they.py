# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end

anton:int=21
beth:int=anton+6
chen=beth+20
drew=chen+anton
ethan=chen

print("Anton is", anton)
print("Beth is", beth)
print("Chen is", chen)
print("Drew is", drew)
print("Ethan is", ethan)