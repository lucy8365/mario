#mario pyramid programming task round 1 python round 2 c
def marioblocks():
    towerheight =int(input("please input how many levels of the pyramid you would like"))
    #^turns user input into integer
    for line in range(towerheight):
        #^towerheight here acts as a len usually would so the program repeats for the amount of lines the user input
        blanks = '  '  *  (towerheight - line)
        #^adds a blank space so that the output forms a pyramid instead a row of #
        hashtags = (line + 1) * "#"
        #^adds a hashtag and each time it runs through another one is added
        print(hashtags + blanks)
        #^prints output


marioblocks()
#^calls the program so it can run
