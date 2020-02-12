# Most of this code was made by https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
# credit goes to the website, I used it to get practice with tries
# Python3 program to demonstrate auto-complete
# feature using Trie data structure.
# Note: This is a basic implementation of Trie
# and not the most optimized one.
class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def search(self, key):

        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)

        for s in self.word_list:
            print(s)
        return 1


# Driver Code
keys = []  # keys to form the trie structure.
key = "hel"  # key for autocomplete suggestions.
status = ["Not found", "Found"]

# create array of words using english_words.txt
f = open("../english_words.txt", "r")
for x in f:
    keys.append(x.replace("\n",""))
# create trie using keys
t = Trie()
t.formTrie(keys)

# autocompleting the given key using
# our trie structure.
print("*********************************")
print("Welcome to Autocomplete, be sure to type /quit when you are finished")
print("*********************************")
while(1):
    userWord = input("Type in a word:")
    if userWord == "/quit":
        print("quiting out of program")
        break
    wordStatus = t.printAutoSuggestions(userWord)
    if wordStatus == -1:
        print("You entered a unique word, it forms no other prefixes\n")
    elif wordStatus == 0:
        print("No string found with this prefix\n")