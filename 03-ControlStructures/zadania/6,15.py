
number_ean = input("Enter the number: ")

if len(number_ean) == 13:
    print(f"Number is correct. EAN-13: {number_ean}")
else:
    print("Incorrect number")

if number_ean[:3] == "590":
    print("Product made in Poland")