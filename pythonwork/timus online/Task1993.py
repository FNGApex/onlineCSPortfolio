x = input()
sentences = x.split(",")
result = True
for i in sentences:
    unclassified_words = i.split()
    classified_words = {}
    words = []
    classification_in_progress = False
    for j in unclassified_words:
        if classification_in_progress:
            if j[-1].isalpha():
                words.append(j.lower())
                # print(j, "Appending to Words")
            else:
                # print(j, "Appending to Words and appending", end=" ")
                words.append(j[:-1].lower())
                # print(words, " to classified_words")
                classification_in_progress = False
                classified_words[classification_type] = (words, 1)
        else:
            if not j[-1].isalpha() and not j[0].isalpha():
                if j[0] == "(":
                    classified_words["second"] = ([j[1:-1].lower()], 0)
                if j[0] == "{":
                    classified_words["first"] = ([j[1:-1].lower()], 0)
                if j[0] == "[":
                    classified_words["third"] = ([j[1:-1].lower()], 0)
            else:
                # print(j, "Deciding")
                # print(j[0])
                words = []
                words.append(j[1:])
                classification_in_progress = True
                if j[0] == "(":
                    classification_type = "second"
                elif j[0] == "{":
                    classification_type = "first"
                elif j[0] == "[":
                    classification_type = "third"
                else:
                    classification_type = "special"
                    classified_words["special"] = (j)
                    classification_in_progress = False
    if classified_words.get("special", None) != None:
        print(", ", classified_words["special"], end=" ", sep="")
    if result:
        classified_words["first"][0][0] = classified_words["first"][0][0][0].upper(
        )+classified_words["first"][0][0][1:]
    print(*classified_words["first"][0], end=" ", sep=" ")
    print(*classified_words["second"][0], end=" ", sep=" ")
    print(*classified_words["third"][0], end="", sep=" ")
    result = False
