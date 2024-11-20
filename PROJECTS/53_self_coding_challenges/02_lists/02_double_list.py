# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# ####################Starter Code  ######################

def double_number(number):
    double_num_list:list=[]
    numbers:int=0
    for i in number:
        numbers=i*2
        double_num_list.append(numbers)
    return double_num_list
def main():
    numbers:list=[1,2,3,4]
    D_num=double_number(numbers)
    print(D_num)
main()
