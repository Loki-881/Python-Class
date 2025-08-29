#Word Frequency Counter 
from collections import Counter
# Read the file
with open("sample.txt", "r") as file:
	text = file.read().lower() # Convert to lowercase
	
# Split into words

words = text.split()
# Count word frequency
word_count = Counter (words)
# Get top 5 most frequent words
top5 = word_count.most_common(5)
print("Top 5 most frequent words:") 
for word, count in top5:
	print(f"{word}: {count}")