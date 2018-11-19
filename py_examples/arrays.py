def array_list(p_list):
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


def array_tuple(p_tuple):
    try:
        for element in p_tuple:
            print(element)
    except:
        print("Error during list")


def main():
    v_list = ['element1', 'element2', 'element3', 'element4']
    array_list(v_list)
    v_tuple = ('element1', 'element2', 'element3', 'element4')
    array_tuple(v_tuple)


if __name__ == "__main__":
    # calling the main function
    main()

