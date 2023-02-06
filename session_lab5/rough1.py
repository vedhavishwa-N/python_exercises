# class linguistic(object):
#     def __init__(self,inputstring):
#         self.string = inputstring
#     def analyze_text(self):
#         test = self.string
#         length = len(test)
#         #change to word_count same for word count
#         word_count = len(test.split())
#         char_count = 0
#         for i in self.string:
#             if i =="":
#                 continue
#             else:
#                 char_count +=1

#         unique_words = []
#         #change string
#         for word in self.string.split():

#             if word not in unique_words:
#                unique_words.append(word)

#         unique_characters = len(str(self.string))

#         #made changes here and the ouput indent should be within length scope
#         output ={"length": length, "total_words:" : word_count,
#              "total_Characters":char_count,"total_unique_words:" :len(unique_words),
#                  "unique_characters":unique_characters}

#         print(output)
# j=linguistic("hi hello hi")
# print(j.analyze_text())
text=input("enter the txt: ")
nc=0
for i in text:
    if i !=" ":
        nc+=1
list_w=text.split()
print("no of chars",nc)
print("lenth of txt-",len(text))
print("number of word",len(list_w))
uni_w=[]
for i in list_w:
    if i not in uni_w:
        uni_w.append(i)
print("number of uni words",len(uni_w))
chars=[]
for i in text:
    if i !=" ":
        if i not in chars:
            chars.append(i)
print("number of uni char",len(chars))
