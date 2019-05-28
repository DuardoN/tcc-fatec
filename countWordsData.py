# Get Word Count
word_data = [
    'bad',
    'triste',
    'tristeza',
    'repudio',
    ':(',
    'sad',
    'caralho',
    'decepcionado',
    'decepcionada',
    'insatisfeito',
    'cansada',
    'exausta',
    'cansado',
    'exausto',
    'feliz',
    'alegre',
    'sorrindo',
    'apaixonada',
    'apaixonado',
    'paz',
    ':)',
    'felicidade',
    'top',
    'topzera',
]

for word_tweet in word_data:
    file = open('tweets-'+ word_tweet +'.csv', 'r')
    book = file.read()

    def tokenize():
        if book is not None:
            words = book.lower().split()
            return words
        else:
            return None


    def count_word(tokens, token):
        count = 0

        for element in tokens:
            # Remove Punctuation
            word = element.replace(",","")
            word = word.replace(".","")

            # Found Word?
            if word == token:
                count += 1
        return count
        
    print('---------------------- File with '+ word_tweet +' ----------------')
    
    # Tokenize the Book
    words = tokenize()
    for word in word_data:
        frequency = count_word(words, word)
        print('Word: [' + word + '] Frequency: ' + str(frequency))