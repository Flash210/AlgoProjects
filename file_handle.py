def create_file(filename):
    with open(filename, 'w') as f:
        while True:
            word = input("Enter a word (or type 'done' to finish): ")
            if word.lower() == 'done':
                break
            f.write(word + '\n')

def read_file_to_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def save_list_to_file(word_list, filename):
    with open(filename, 'w') as f:
        for word in word_list:
            f.write(word + '\n')