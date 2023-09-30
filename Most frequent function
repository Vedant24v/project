def most_frequent(input_string):
    # Remove spaces and convert the input string to lowercase
    input_string = input_string.replace(" ", "").lower()
    
    # Create an empty dictionary to store character frequencies
    char_count = {}
    
    # Count the frequency of each character in the input string
    for char in input_string:
        if char.isalpha():  # Ignore non-alphabetical characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Sort the dictionary by values in decreasing order
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    # Print the characters and their frequencies
    for char, count in sorted_char_count:
        print(f"{char} = {count:02d}", end=" ")
    print()

# Input string
input_str = input("Please enter a string: ")

# Call the most_frequent function
most_frequent(input_str)
