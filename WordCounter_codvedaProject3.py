def word_counter(text):
    words = text.split()
    return len(words)

def main():
    text = input("Enter text : ")
    print("length of your text :", word_counter)
main()