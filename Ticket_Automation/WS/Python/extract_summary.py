'''Summary Extraction'''
import nltk, re, heapq, string, gensim

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


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

def gensimSummary(text):
	return summarize(text)

print(
gensimSummary('''Rice Pudding - Poem by Alan Alexander Milne What is the matter with Mary Jane? She's crying with all her might and main, And she won't eat her dinner - rice pudding again - What is the matter with Mary Jane? What is the matter with Mary Jane? I've promised her dolls and a daisy-chain, And a book about animals - all in vain - What is the matter with Mary Jane? What is the matter with Mary Jane? She's perfectly well, and she hasn't a pain; But, look at her, now she's beginning again! - What is the matter with Mary Jane? What is the matter with Mary Jane? I've promised her sweets and a ride in the train, And I've begged her to stop for a bit and explain - What is the matter with Mary Jane? What is the matter with Mary Jane? She's perfectly well and she hasn't a pain, And it's lovely rice pudding for dinner again! What is the matter with Mary Jane?''')
)

print()

print(keywords(gensimSummary('''Rice Pudding - Poem by Alan Alexander Milne What is the matter with Mary Jane? She's crying with all her might and main, And she won't eat her dinner - rice pudding again - What is the matter with Mary Jane? What is the matter with Mary Jane? I've promised her dolls and a daisy-chain, And a book about animals - all in vain - What is the matter with Mary Jane? What is the matter with Mary Jane? She's perfectly well, and she hasn't a pain; But, look at her, now she's beginning again! - What is the matter with Mary Jane? What is the matter with Mary Jane? I've promised her sweets and a ride in the train, And I've begged her to stop for a bit and explain - What is the matter with Mary Jane? What is the matter with Mary Jane? She's perfectly well and she hasn't a pain, And it's lovely rice pudding for dinner again! What is the matter with Mary Jane?'''),ratio = 1, split  = True))

print(
extractSummary("Hi I am Sam, Recently I bought a new Air Quality sensor module support from you! Suddenly GPRS of the module is not working properly! please help me!")
)
