'''Summary Extraction'''
import nltk, re, heapq, string

def extractSummary(text):
    text = str(text)
    print(text)

    final_text = re.sub(r'\s+', ' ', text) # reomve space....
    
    print(final_text)
