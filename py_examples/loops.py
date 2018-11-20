def for_loop(p_range):
    for p_value in p_range:
        print(p_value)


def while_loop1(p_range):
    p_value = 1
    while p_value < p_range:
        if p_value == 3:
            break
        print(p_value)
        p_value += 1


def while_loop2(p_range):
    p_value = 0
    while p_value < p_range:
        p_value += 1
        if p_value == 3:
            continue
        print(p_value)


def main():
    #for_loop(5)
    while_loop1(10)
    while_loop2(10)


if __name__ == "__main__":
    # calling the main function
    main()

