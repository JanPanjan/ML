from list import List

def main():
    # Create a new linked list
    my_list = List()

    # Insert some elements
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)

    # Display the list (will print: 3 -> 2 -> 1 -> None)
    my_list.pll()

    # Search for an element
    if my_list.search(2):
        print(f"Found: 2")

    # Delete an element
    my_list.delete(2)

    # Display the updated list (will print: 3 -> 1 -> None)
    my_list.pll()


if __name__ == "__main__":
    main()