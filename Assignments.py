'''#Practice Problems -6:
WRITE A PYTHON PROGRAM THAT SIMULATES A SIMPLE BOOK INVENTORY SYSTEM. CREATE A DICTIONARY TO REPRESENT A LIBRARY'S BOOK INVENTORY, WHERE BOOK TITLES ARE KEYS, AND
 THE CORRESPONDING VALUES ARE THE NUMBER OF COPIES AVAILABLE. PROMPT THE USER TO ENTER THE TITLE OF A BOOK AND CHECK IF IT IS PRESENT IN THE INVENTORY. 
IF THE BOOK IS PRESENT, DISPLAY THE NUMBER OF COPIES AVAILABLE; OTHERWISE, PROMPT THE USER TO ADD THE BOOK TO THE INVENTORY ALONG WITH THE NUMBER OF COPIES.'''
book_inventory = {
    "To Kill a Mockingbird": 4,
    "1984": 6,
    "The Great Gatsby": 3,
    "Pride and Prejudice": 5
}
def display_inventory(inventory):
    print("\nInventory:")
    for title, copies in inventory.items():
        print(f"{title}: {copies} copies")
def manage_inventory(inventory):
    title = input("\nEnter book title: ").strip()
    if title in inventory:
        print(f"'{title}' has {inventory[title]} copies.")
    else:
        copies = input(f"'{title}' not found. Enter copies to add: ").strip()
        if copies.isdigit() and int(copies) > 0:
            inventory[title] = int(copies)
            print(f"'{title}' added with {copies} copies.")
        else:
            print("Invalid input. No changes made.")
display_inventory(book_inventory)
manage_inventory(book_inventory)
display_inventory(book_inventory)


'''#Problem Statement-6:WRITE A PYTHON PROGRAM THAT HAS THE DICTIONARY OF YOUR FRIENDS NAMES AS KEYS AND PHONE NUMBERS AS ITS VALUES. 
PRINT THE DICTIONARY IN A SORTED ORDER. PROMPT THE USER TO ENTER THE NAME AND CHECK IF IT IS PRESENT IN THE DICTIONARY. IF THE NAME IS NOT PRESENT, 
THEN ENTER THE DETAILS IN THE DICTIONARY.'''
friends_dict = {
    "Alice": "987-654-3210",
    "Bob": "876-5432-109",
    "Charlie": "765-432-1098",
    "David": "111-222-3333"
}
def print_sorted_dict(dictionary):
    print("Friends Dictionary (Sorted by Name):")
    for name, phone in sorted(dictionary.items()): print(f"{name}: {phone}")
def check_and_update_dict(dictionary):
    name = input("\nEnter friend's name: ").strip()
    if name in dictionary:
        print(f"{name} is already in the dictionary.")
    else:
        dictionary[name] = input(f"Enter {name}'s phone number: ").strip()
        print(f"{name} has been added.")
print_sorted_dict(friends_dict)
check_and_update_dict(friends_dict)
print_sorted_dict(friends_dict)


#Problem Statement 7:Write a Python program that reads the contents of a file and counts the occurrences of each letter, prompting the user to enter the filename.
def count_letter_occurrences(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()  
        letter_count = {}
        for char in content:
            if char.isalpha():  
                letter_count[char] = letter_count.get(char, 0) + 1
        print("\nLetter Occurrences:")
        for letter, count in sorted(letter_count.items()):
            print(f"{letter}: {count}")
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
if __name__ == "__main__":
    filename = input("Enter the file name: ")
    count_letter_occurrences(filename)


'''#Practice Problem 7:Write a Python program that reads the contents of a file and counts the occurrences of each vowel and consonant, prompting 
the user to enter the filename.'''
def count_vowels_and_consonants(file_path):
    vowels = "aeiou"
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
        vowel_count = sum(1 for char in content if char in vowels)
        consonant_count = sum(1 for char in content if char.isalpha() and char not in vowels)
        print(f"Vowels: {vowel_count}")
        print(f"Consonants: {consonant_count}")
    except FileNotFoundError:
        print("File not found. Please check the file name and path.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    filename = input("Enter the file name (with extension): ")
    count_vowels_and_consonants(filename)
