def count_unique_words(statement):
   
    exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    word_count = {}
    for word in statement.split():
        normalized_word = word.strip(",.!?;:()[]{}").lower()
        
        if normalized_word not in exclude_words:
            original_word = word.strip(",.!?;:()[]{}")
            word_count[original_word] = word_count.get(original_word, 0) + 1
    
    # Initialize different categories
    lower_case = {}
    upper_case = {}
    capitalized_words = {}
    
    # Separate into categories
    for word, count in word_count.items():
        if word.islower():
            lower_case[word] = count
        elif word.isupper():
            upper_case[word] = count
        elif word[0].isupper():
            capitalized_words[word] = count
    
    # Sort and print results
    for category in [lower_case, capitalized_words, upper_case]:
        for word, count in sorted(category.items()):
            print(f"{word:<10} - {count}")
    
    total_filtered = sum(word_count.values())  # Total of filtered words
    print(f"Total words filtered: {total_filtered}")

statement = input("Enter a string statement:\n")
count_unique_words(statement)