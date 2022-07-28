from string import punctuation

def remove_punc(text):
    '''Remove punctuations from a text and return cleaned text
    -> clean_Text=remove_punc(text)
    '''
    for punc in punctuation:
        # print(punc)
        text=text.replace(punc,'')
    return text

def word_count(text):
    wordlist=text.lower().split()
    #dictionary
    wc={}
    for word in wordlist:
        if word in wc:
            wc[word]+=1
        else:
            wc[word]=1
    return wc

def sort(word_dict):
    ans=sorted(word_dict.items(),key=lambda val:val[1],reverse=True)
    return ans

if __name__=='__main__':
     msg='_@#this is a (*!)(@#) is) a) string)'
     long_text='''
     The quick brown fox jumps over the lazy dog,
     and attacks the chicken with a fying kick.
     This is a real world story about a fox,that could kick and jump.
     If you are really interested in this story, then kee reading. The End
     '''
     cln_text=remove_punc(long_text)
     counted_word=word_count(cln_text)
     print(sort(counted_word))



    #wap to replace all the multiple spaces in a single space



