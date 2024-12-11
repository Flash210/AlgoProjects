from file_handle import create_file, read_file_to_list, save_list_to_file
from operations import is_sorted, search_word, merge_sort, binary_search



def main():
    filename = 'words.txt'

    # Step 1: Create a text file
    create_file(filename)

    # Step 2: Read the file and build a list
    words = read_file_to_list(filename)

    # Step 3: Verify if the list is sorted
    print(f"Is the list sorted? {is_sorted(words)}")

    # Step 4: Search for a word
    word_to_search = input("Enter a word to search for: ")
    position = search_word(words, word_to_search)
    if position != -1:
        print(f"Word found at position: {position}")
    else:
        print("Word not found.")

    # Step 5: Sort the list using merge sort
    sorted_words = merge_sort(words)

    # Step 6: Save the sorted list back into the file
    save_list_to_file(sorted_words, filename)

    # Step 7: Perform a binary search
    word_to_search = input("Enter a word to search in the sorted list: ")
    position = binary_search(sorted_words, word_to_search)
    if position != -1:
        print(f"Word found at position: {position}")
    else:
        print("Word not found.")

    # Step 8: Cost of a non-binary search (linear search)
    print("Worst-case cost of non-binary search: O(n)")

    # Step 9: Cost of a binary search
    print("Worst-case cost of binary search: O(log n)")


if __name__ == '__main__':
    main()
