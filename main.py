def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_count_char = count_char(text)
    report(num_words, dict_count_char)

def report(num_words, dict_count_char):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    
    l = []
    for k in dict_count_char:
        l.append({"key": k, "count": dict_count_char[k]})
    l.sort(reverse=True, key=lambda i: i["count"])
    for i in l:
        if i["key"].isalpha():
            print("The '{key}' character was found {count} times".format(**i))
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_char(text):
    m = {}
    for w in text.split():
        for c in w:
            key = c.lower()
            if key in m:
                m[key] += 1
            else:
                m[key] = 0

    return m

main()
