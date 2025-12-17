import sys 

def add_nums(args):
    total=0
    for num in args:
        total+=int(num)
    return total

def main():
    scriptname=sys.argv[0]
    result = add_nums(sys.argv[1:])
    print("the script name is:", scriptname)
    print("Total:", result)


if __name__ == "__main__":
    main()




# TODO add print statement
