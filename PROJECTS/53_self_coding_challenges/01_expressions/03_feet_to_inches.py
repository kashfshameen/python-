# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. 
# Foot is the singular, and feet is the plural.
inches_in_foot:int=12
def main():
    feet:float=float(input("enter the feet"))
    inches_in_foot=feet * inches_in_foot
    print("convert feet into inches:",inches_in_foot)
    