def  countWordsFromFile():
    fileName = input("Enter your file name: ")
    
    NumberOfWords = 0
     
    file = open(fileName, 'r')
    for  line in file:
        words = line.split()
        NumberOfWords = NumberOfWords + len(words)
    print ("Number of words: ")
    print (NumberOfWords)

countWordsFromFile()
