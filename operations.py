
def is_sorted(word_list):
    return word_list == sorted(word_list)

def search_word(word_list, word):
    for index, w in enumerate(word_list):
        if w == word:
            return index
    return -1

def merge_sort(word_list):
    if len(word_list) <= 1:
        return word_list

    mid = len(word_list) // 2
    left = merge_sort(word_list[:mid])
    right = merge_sort(word_list[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def binary_search(word_list, word):
    left, right = 0, len(word_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if word_list[mid] == word:
            return mid
        elif word_list[mid] < word:
            left = mid + 1
        else:
            right = mid - 1

    return -1



