import string 
import re     

#Part 1 - Create a class called Text to analyze a string or file
class Text:
    def __init__(self, text):
        self.text = text

    #Method word_frequency() returns how many times a word appears in the text
    def word_frequency(self, word):
        words = self.text.lower().split() #Split the text into words and convert all to lowercase
        count = words.count(word.lower()) #Count how many times the given word appears
        if count > 0:
            return count
        else:
            return f"'{word}' not found in the text." #Return a meaningful message if not found

    #Method most_common_word() returns the most frequent word in the text
    def most_common_word(self):
        words = self.text.lower().split() #Split the text into lowercase words
        freq = {} #Initialize an empty dictionary to store word frequencies
        for word in words:
            freq[word] = freq.get(word, 0) + 1 #Increment the word count in the dictionary
        return max(freq, key=freq.get) if freq else None #Return the word with the highest frequency

    #Method unique_words() returns a list of all unique words in the text
    def unique_words(self):
        words = self.text.lower().split() #Split the text into lowercase words
        return list(set(words)) #Convert to a set to remove duplicates, then back to a list

    #Class method from_file() allows creating a Text object using a file path
    @classmethod
    def from_file(cls, file_path): #Takes the file path as a parameter
        with open(file_path, "r") as file:
            content = file.read() #Read the entire file content
        return cls(content) #Return a new Text instance with the file content

#Part 2 - Create a class called TextModification to clean and process text
class TextModification(Text): #Inherits from the Text class
    #Method remove_punctuation() removes punctuation from the text
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation) #Create a translation table to remove punctuation
        return self.text.translate(translator) #Apply the translation and return the cleaned text

    #Method remove_stop_words() removes common stop words from the text
    def remove_stop_words(self):
        #Define a small set of common English stop words
        stop_words = {
            "a", "an", "the", "is", "are", "and", "or", "in", "on", "of", "to", "with", "as", "at", "by", "for", "from"
        }
        words = self.text.split() #Split the text into words
        filtered = [word for word in words if word.lower() not in stop_words] #Filter out stop words
        return " ".join(filtered) #Join the remaining words into a string

    #Method remove_special_characters() removes all characters except letters, numbers, and spaces
    def remove_special_characters(self):
        return re.sub(r"[^a-zA-Z0-9\s]", "", self.text) #Use regular expression to remove unwanted characters
    
text_obj = TextModification("The quick brown fox!!! jumps over the lazy dog, right? Right.")
print("Most common word:", text_obj.most_common_word()) #Print most frequent word
print("Unique words:", text_obj.unique_words()) #Print all unique words
print("Without punctuation:", text_obj.remove_punctuation()) #Text without punctuation
print("Without stop words:", text_obj.remove_stop_words()) #Text without common stop words
print("Without special characters:", text_obj.remove_special_characters()) #Text with only letters/numbers