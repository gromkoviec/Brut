import argparse

def parsing():
    parser = argparse.ArgumentParser(description='Add config file')
    parser.add_argument('-f', help='Name of the required JASON config file')
    args = parser.parse_args()
    return(args.f)