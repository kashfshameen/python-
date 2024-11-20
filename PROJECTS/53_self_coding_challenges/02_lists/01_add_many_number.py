# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

########################## Starter Code####################
def sum_of_list(number):
    SumOfList:int=0
    for i in number:
        SumOfList += i
    return (SumOfList)

def main():
    number:list=[1,2,3,4,5,6]
    sum_of_lists:int=sum_of_list(number)
    print(sum_of_lists)

main()