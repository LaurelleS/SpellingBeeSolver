def main():
    # ask user for letters of the spelling bee and store them
    let = input("Enter the 7 letters of the Spelling Bee. Make sure to capitalize the center letter: ")
    let_arr = []
    centr = ""
    # keep 6 letters and center letter separate
    for i in let:
        if i.isupper():
            centr = i
        else:
            let_arr.append(i)
    word_list1 = find_val_words(let_arr, centr, "words.txt")
    word_list2 = find_val_words(let_arr, centr, "SpellingBeeWords.txt")
    for word in word_list1:
        print(word + "\n")
    for word in word_list2:
        print(word + "\n")


def let_not_used(arr, centr):
    arr.append(centr.lower())
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
           "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    not_used = []
    for let in abc:
        if not (let == arr[0] or let == arr[1] or let == arr[2] or let == arr[3] \
                or let == arr[4] or let == arr[5] or let == arr[6]):
            not_used.append(let)
        else:
            continue
    return not_used


def find_val_words(arr, centr, fileName):
    val_words = []
    cpy_wrds = []
    unused = let_not_used(arr, centr)
    # search for words containing given letters
    with open(fileName, "r") as words:
        for line in words:
            line_s = line.strip()
            # start with center letter
            if centr.lower() in line_s and len(line_s) > 3:
                val_words.append(line_s)
                cpy_wrds.append(line_s)
            # go through val_words and remove any words not containing given letters
    for i in range(0, len(cpy_wrds)):
        for let in unused:
            if let in cpy_wrds[i].lower():
                val_words.remove(cpy_wrds[i])
                break
    return val_words


if __name__ == "__main__":
    main()
