# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5
def main():
    length_of_side_1:float=float(input("What is the length of side 1?"))
    length_of_side_2:float=float(input("What is the length of side 2?"))
    length_of_side_3:float=float(input("What is the length of side 3?"))

    print("The perimeter of the triangle is" , length_of_side_1+length_of_side_2+length_of_side_3)
main()