'''Summary Extraction'''
import nltk, re, heapq, string

def extractSummary(text):
    text = str(text) # ensoure that text convert to text....
    
    article_text = re.sub(r'\s+', ' ', text) # remove unwanted space....
    
    formatted_article_text = re.sub(r'\s+', ' ', article_text) # format the text....
    
    sentence_list = nltk.sent_tokenize(article_text) # token the sentence....
    
    # Word frequency....
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
	    if word not in stopwords:
		    if word not in word_frequencies.keys():
			    word_frequencies[word] = 1
		    else:
			    word_frequencies[word] += 1
			    
    maximum_frequency = max(word_frequencies.values())# max of frequency....
    
    # word frequency.....
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
					    
    sentence_limit = len(sentence_list)//2 # half the amount of total length of query....
    
    summary_sentences = heapq.nlargest(sentence_limit+1, sentence_scores, key=sentence_scores.get) # join the sentence heap of sentence score....
    summary = ' '.join(summary_sentences)
    return(summary)
