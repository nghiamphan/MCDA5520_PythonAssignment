def stack(new_list: list, operation: str, new_element: any = None) -> list:
    if operation == "add":
        if new_element != None:
            new_list.append(new_element)
        else:
            raise Exception("Missing element to add to the stack")
    elif operation == "remove":
        new_list.pop()
    else:
        raise Exception("Invalid operation")

    return new_list


def queue(new_list: list, operation: str, new_element: any = None) -> list:
    if operation == "add":
        if new_element != None:
            new_list.append(new_element)
        else:
            raise Exception("Missing element to add to the queue")
    elif operation == "remove":
        new_list.pop(0)
    else:
        raise Exception("Invalid operation")

    return new_list


def test():
    new_list = [1, 2, 3, 4]
    print("Add a new element to the stack")
    new_list = stack(new_list, "add", 0)
    print(new_list)
    print("Remove an element from stack")
    stack(new_list, "remove")
    print(new_list)
    print("Adding a new element to the queue")
    new_list = queue(new_list, "add", 5)
    print(new_list)
    print("Remove an element from the queue")
    new_list = queue(new_list, "remove")
    print(new_list)


if __name__ == "__main__":
    test()
