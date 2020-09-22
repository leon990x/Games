#  File: WordSearch.py

#  Leon L

in_file = open("hidden.txt", "r")


s = in_file.readline()

s = s.split() # by default splits spaces
dimensions = [int(s[0]), int(s[1])]

in_file.readline() # skips over lines

word_search = []

for line in range(dimensions[0]):
    row = in_file.readline()
    row = row.split()
    word_search.append(row)

in_file.readline() # skips over line

number_words = int(in_file.readline())

# make a word bank

word_bank = []
for i in range(number_words):
    word = in_file.readline()
    word = word.strip()
    word_bank.append(word)


# make an outfile
outfile = open ("found.txt", "w")



# select word from word bank


# get value of word[0] in word bank


# loop through word_search for word[0] (first letter)



def adjacent(word, pos_start, outfile):
    m = pos_start[0]
    n = pos_start[1]
    letter2 = word[1] # second letter

    if m > 0 and n > 0 and letter2 == word_search[m - 1][n - 1]:
        pos_new_val = [m-1, n-1]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y

            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word + " "+ str(pos_start[0]+1).rjust(13-len(word)) +" "+ str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if m > 0 and letter2 == word_search[m-1][n]:
        pos_new_val = [m-1, n] # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val #pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word)-2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word +" "+ str((pos_start[0]+1)).rjust(13-len(word)) +" "+ str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if m > 0 and n < (len(word_search)-1) and letter2 == word_search[m - 1][n + 1]:
        pos_new_val = [m-1, n+1]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word +" "+str((pos_start[0]+1)).rjust(13-len(word)) +" "+ str((pos_start[1]+1)).rjust(3)
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if n < (len(word_search)-1) and letter2 == word_search[m][n + 1]:
        pos_new_val = [m, n+1]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word+" "+str(pos_start[0]+1).rjust(13-len(word))+" "+str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if m < (len(word_search)-1) and n <(len(word_search)-1) and letter2 == word_search[m + 1][n + 1]:
        pos_new_val = [m+1, n+1]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word+" "+str(pos_start[0]+1).rjust(13-len(word))+" "+str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if m < (len(word_search)-1) and letter2 == word_search[m + 1][n]:
        pos_new_val = [m+1, n]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word+" "+str(pos_start[0]+1).rjust(13-len(word))+" "+str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if m < (len(word_search)-1) and n > 0 and letter2 == word_search[m + 1][n - 1]:
        pos_new_val = [m+1, n-1]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word+" "+str(pos_start[0]+1).rjust(13-len(word))+" "+str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

    if n > 0 and letter2 == word_search[m][n - 1]:
        pos_new_val = [m, n-1]  # set our new value's position
        change_x = int(pos_new_val[0]) - int(pos_start[0])
        change_y = int(pos_new_val[1]) - int(pos_start[1])
        target_pos = pos_new_val  # pos_new_val is an array that stores coordinates of newest target to start of next loop
        found = True
        for k in range(len(word) - 2):
            target_pos[0] += change_x
            target_pos[1] += change_y
            # if statement for out of bounds here (try except)
            if target_pos[0] < 0 or target_pos[0] >= len(word_search):
                found = False
                break
            if target_pos[1] < 0 or target_pos[1] >= len(word_search):
                found = False
                break
            target = word_search[target_pos[0]][target_pos[1]]
            if target != word[k+2]:
                found = False
        if found:
            print(word, " ", (pos_start[0]+1), (pos_start[1]+1))
            o = word+" "+str(pos_start[0]+1).rjust(13-len(word))+" "+str(pos_start[1]+1).rjust(3)
            str(o).strip("(")
            outfile.write(str(o) + '\n')
            # if statement word is finally looped all the way through

#pos_start is an array that stores the x and y coordinates of the starting letter found




def main():
    for word in word_bank:
        first_letter = word[0]
        for m in range(len(word_search)):
            for n in range(len(word_search)):
                if word_search[m][n] == word[0]:
                    #pos_start = [word_search[m], word_search[n]]  # fall back
                    pos_start = [m, n]
                    adjacent(word, pos_start, outfile)
                      # must store m and n a

                    #account for conventional coordinates in our PRINT statement to not affect our adjacent function
                    #print(word, "", pos_start)
    in_file.close()
    outfile.close()




main()