#Program obliczajacy ile dana litera pojawila sie w zdaniu
import letters

def main():
    text = "You never get a second chance to make a first impression"
    letter = "e"
    print("The number of letter 'e' is:",(letters.count_letter(text, letter)))

if __name__ == "__main__":
    main()