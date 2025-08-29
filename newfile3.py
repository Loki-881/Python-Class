from collections import Counter
import re

def word_frequency_counter(filename):
    """
    Reads a text file, counts word frequencies, and prints the top 5.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Read the file and convert to lowercase
            words = re.findall(r'\b\w+\b', text)  # Find all words using regex
            
            # Use collections.Counter to count word frequencies
            word_counts = Counter(words)
            
            # Get the top 5 most common words
            top_5 = word_counts.most_common(5)
            
            print("Top 5 most frequent words:")
            for word, count in top_5:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage:
# Create a dummy file for the example
with open('sample.txt', 'w') as f:
    f.write("Freedom is the right of all sentient beings, Autobots, transform and roll out, and We've suffered losses, but we've not lost the war")

word_frequency_counter('sample.txt')
