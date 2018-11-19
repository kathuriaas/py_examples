def array_list(p_list):
    print("List example started:")
    try:
        for element in p_list:
            print(element)
        if "element4" in p_list:
            print("Element present in list")
        else:
            print("Element not present in list")
        p_list.append('element6')
        print(p_list)
        print(p_list[2:])
        print(p_list[:2])
        print(len(p_list))
        p_list.remove('element4')
        print(p_list)
        print(p_list.count('element7'))
        p_list.clear()
        print(p_list)
    except:
        print("Error during list")
    print("List example Ended\n")


def array_tuple(p_tuple):
    print("Tuple example started:")
    try:
        for element in p_tuple:
            print(element)
        print(p_tuple[2:])
        if 'element1' in p_tuple:
            print('element1', ' is present in ', p_tuple)
        print(p_tuple.count('element1'))  # Count of element1 in tuple
    except:
        print("Error during list")

    try:
        p_tuple[0] = 'New_element'  # This will raise error
        print(p_tuple)
    except:
        print('Error during tuple change--tuples are immutable')

    try:
        del p_tuple  # Delete this tuple completely
        print(p_tuple)
    except:
        print('Tuple deleted')
    print("Tuple example Ended\n")


def array_set(p_set):
    print("Set example started:")
    try:
        print(p_set)
    except:
        print("Error during set")
    print("Set example Ended\n")


def main():
    v_list = ['element1', 'element2', 'element3', 'element4']
    array_list(v_list)
    v_tuple = ('element1', 'element2', 'element3', 'element4')
    array_tuple(v_tuple)
    v_set = {'set_element1', 'set_element2', 'set_element3', 'set_element4'}
    array_set(v_set)


if __name__ == "__main__":
    # calling the main function
    main()

