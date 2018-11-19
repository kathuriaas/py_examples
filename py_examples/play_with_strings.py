def str_func(str1):
    try:
        print(str1)
        print(str1[0])  # First character of string
        print(str1[2])  # Third character of string
        print(str1[0:2])  # String starting at position 0 with 2 (2-0) characters
        print(str1[5:11])  # String starting at position 5(6th) with 6 (11-5) characters
        print(len(str1))  # Length of string
        print(str1.lower())  # Lower of string
        print(str1.upper())  # Upper of string
        print(str1.replace("T", "Z"))  # Replace string character
        print(str1.split(" "))  # Split into substrings returning list of values
        print(str1 + " " + str1)  # Concatenate strings
        print(str1.capitalize())  # First Upper of string
        print(str1.split(" ")[0] + " " + str1.split(" ")[3])  # AWK alternate
    except:
        print("Error during string function")


def main():
    print('Enter string:')
    x = input()
    if x == '':
        x = "this is a string"
    str_func(x)


if __name__ == "__main__":
    # calling the main function
    main()

