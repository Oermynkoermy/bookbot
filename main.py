def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.lower()
        count = 0
        for i in words.split():
            count += 1

        word_count = {}
        for c in words:
            if c in word_count:
                word_count[c] += 1
            else:
                word_count[c] = 1

        final_list = [{"char": ch, "num": num} for ch, num in word_count.items() if ch.isalpha()]
        final_list.sort(reverse=True, key=lambda item: item["num"])
        


        print (f"--- Begin report of {book_path} ---")
        print(f" The number of words in the books is {count}")
        for value in final_list:
            char = value["char"]
            num = value ["num"]
            print (f"The '{char}' character was found '{num}' times")
        print ("End report")



main()