class Linguist(object):
    def __init__(self,string):

        self.string=string

    def analyze_text(self):
        dict_string={}

        text=self.string
        text=text.lower()
        #for finding number of characters
        no_char=0
        for char in text:
            if char != ' ':
                no_char = no_char + 1
        dict_string["number of characters"]=no_char

        #for finding length of the string
        length=(len(text)-1)
        dict_string["length of the string"]=length

        #for finding number of words
        no_words=0
        for char in text:
            if char == " ":
                no_words=no_words+1
        dict_string["number of words"]=no_words

        #for finding unique characters

        no_unique_char = 0
        list = [" "]
        for char in text:
            if char not in list:
                no_unique_char = no_unique_char + 1
                list.append(char)
        dict_string["number of unique characters"]=no_unique_char

        #for finding unique word
        list2 = []
        list1 = []

        for char in text:
            if char == " ":
                st = str(list1)
                list2.append(st)
                list1 = []
            else:
                list1.append(char)
        dum = list[0]
        no_unique_words = 0
        list3 = []
        for n in list2:
            if n not in list3:
                no_unique_words = no_unique_words + 1
                list3.append(n)
        dict_string["number of unique words"]=no_unique_words

        return dict_string

    #to test if a string is in english
    #note-isaplha fuction can be used
    def is_english(self):
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
        text=self.string
        text=text.lower()
        flag=0
        for char in text:
            if char  not in alphabet:
              flag=1


        if flag==1:
            print("-------------the given string is not in english--------------")
        else:
            print("-------------the given string is in english-----------------")












