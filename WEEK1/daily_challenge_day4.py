#Daily challenge
# Matrix string input 
MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Clean and split the string into separate lines (rows)
def clean(matrix_string):
    # Remove leading/trailing spaces and split by line
    return matrix_string.strip().splitlines()

# Step 2: Convert each row string into a list of characters (to form a 2D list / matrix)
def convert_to_matrix(rows):
    matrix = []
    for row in rows:
        matrix.append(list(row))  #  for eg. turn "7ii" into ['7','i','i']
    return matrix

# Step 3: Read the matrix column by column (top to bottom, left to right)
def read_columns(matrix):
    message = ""
    rows = len(matrix)
    cols = len(matrix[0])

    # Loop through each column (left to right)
    for col in range(cols):
        # Loop through each row in that column (top to bottom)
        for row in range(rows):
            message += matrix[row][col]
    return message  # This gives us the raw text read column-wise

# Step 4: Clean up the message 
def clean_message(text):
    result = ""
    i = 0
    while i < len(text):
        if text[i].isalpha():
            # If it's a letter, keep it
            result += text[i]
        else:
            # Check ahead — is there a letter after a group of junk characters?
            j = i
            while j < len(text) and not text[j].isalpha():
                j += 1
            if j < len(text):
                result += " "  # Replace junk with a space
                i = j - 1       # Skip ahead to just before the next letter
        i += 1
    return result

# Run the program step-by-step
rows = clean(MATRIX_STR)              # Step 1
matrix = convert_to_matrix(rows)      # Step 2
raw_text = read_columns(matrix)       # Step 3
decoded_message = clean_message(raw_text)  # Step 4

# Final output
print(decoded_message)



{x: x^2 for x in range(1, 11) if x % 2 == 0}
