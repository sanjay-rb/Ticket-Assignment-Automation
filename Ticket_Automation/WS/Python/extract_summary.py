'''Summary Extraction'''
import nltk, re, heapq, string

def extractSummary(text):
    text = str(text)
    article_text = re.sub(r'\s+', ' ', text) # remove unwanted space....
    formatted_article_text = re.sub(r'\s+', ' ', article_text)
    # token the sentence....
    sentence_list = nltk.sent_tokenize(article_text)
    # print("Sentence in the paragraph : \n\n", sentence_list, "\n")
    # Word frequency....
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
	    if word not in stopwords:
		    if word not in word_frequencies.keys():
			    word_frequencies[word] = 1
		    else:
			    word_frequencies[word] += 1
	# max of frequency
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
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
    sentence_limit = len(sentence_list)//2
    summary_sentences = heapq.nlargest(sentence_limit+1, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    # print("Final Summary : ", summary)
    return(summary)
