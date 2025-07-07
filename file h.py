def length_words(file_name,word_length):
    try:
        with open(file_name,"r") as file:
            text = file.read()
            words_r = text.split()

            match_words = [word for word in words_r if len(word) == word_length]

            if match_words:
                print(f"The word of length {word_length}")
                for word in match_words:
                    print(word)

            else:
                print("The word not found")

        file.close()

    except:
        print("File not found")

file_name = 'text.txt'
word_len = int(input("Enter the word length"))

length_words(file_name,word_len)
