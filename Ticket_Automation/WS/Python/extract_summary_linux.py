import nltk, re, heapq
text = '''"Hi I am Sanjay, Recently I bought a new Air Quality sensor   	module from you! Suddenly GPRS	of   	the module is not working properly! please help me!"'''




article_text = re.sub(r'\s+', ' ', text) # remove unwanted space....

# print("After remove brakets and space : \n\n", article_text, "\n")

formatted_article_text = re.sub(r'\s+', ' ', article_text)

# print("After remove special char : \n\n", article_text, "\n")

# token the sentence....
sentence_list = nltk.sent_tokenize(article_text)

print("Sentence in the paragraph : \n\n", sentence_list, "\n")

# Word frequency....

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
                if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                else:
                        word_frequencies[word] += 1

# Print word frequency....
'''
print("Word Frequency Table : ")r
for k, v in word_frequencies.items():
	print (k, v)
'''
# max of frequency
maximum_frequency = max(word_frequencies.values())
# print(maximum_frequency)
for word in word_frequencies.keys():
	word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

# Print word frequency....
'''
print("Word Frequency Table : ")
for k, v in word_frequencies.items():
	print (k, v)
'''

# Calc Sentence score....
sentence_scores = {}
for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                                if sent not in sentence_scores.keys():
                                        sentence_scores[sent] = word_frequencies[word]
                                else:
                                        sentence_scores[sent] += word_frequencies[word]

# Print Sentence score....
'''
print("Sentence score Table : ")
for k, v in sentence_scores.items():
	print (k, v)
'''

sentence_limit = len(sentence_list)//2

summary_sentences = heapq.nlargest(sentence_limit+1, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
# print("Input Text : ",  text, "\n\n")

print("Final Summary : ", summary)
