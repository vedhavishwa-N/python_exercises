class Linguist( object):
    def __init__( self, string):

        self.string=string

    def analyze_text( self):
        dict_string={}

        text=self.string
        text=text.lower()
        #for finding number of characters
        no_char=0
        for char in text:
            if char != ' ':
                no_char = no_char + 1
        dict_string[ "number of characters"] = no_char

        #for finding length of the string
        length = ( len( text))
        dict_string[ "length of the string"] = length

        #for finding number of words
        
        words_list=text.split()
        no_words = len(words_list)
        dict_string[ "number of words"] = no_words

        #for finding unique characters

        
        uni_char_list = []
        for char in text:
            if char !=" ":
                if char not in uni_char_list:

                    uni_char_list.append( char)
        no_unique_char = len(uni_char_list)
        dict_string[ "number of unique characters"] = no_unique_char

        #for finding unique word
        uni_word_list=[]
        
        for word in words_list:
            if word not in uni_word_list:
                uni_word_list.append(word)
        no_unique_words = len(uni_word_list)
        dict_string[ "number of unique words"] = no_unique_words

        return dict_string

    #to test if a string is in english
    #note-isaplha fuction can be used
    def is_english (self):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

        text = self.string
        text = text.lower ()
        flag = 0
        for char in text:
            if char  not in alphabet:
              flag = 1


        if flag == 1:
            print ( "-------------the given string is not in english--------------")
        else:
            print ( "-------------the given string is in english-----------------")












