import urllib

def read_text():
    quotes = open("movie_quotes.txt")
    file_contents = quotes.read()
    print(file_contents)
    quotes.close()
    find_profanity(file_contents)

def find_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="
                                + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("You filthy animal!")
    elif "false" in output:
        print("Nice one!")
    else:
        print("Something's wrong...")

read_text()
