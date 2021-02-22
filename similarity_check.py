from difflib import SequenceMatcher

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

string1 = input("Actual Text :-  ")
print("Keywords\n")
key1 = input("1 :-  ")
key2 = input("2 :-  ")
key3 = input("3 :-  ")
key4 = input("4 :-  ")
key5 = input("5 :-  ")
string3 = input("Test Text :-  ")

lists = []
lists.append(key1)
lists.append(key2)
lists.append(key3)
lists.append(key4)
lists.append(key5)
k = 0

matches = [x for x in lists if x in string1]
while '' in matches:
    matches.remove('')

answer = similar(string1, string3)
final_answer = answer * 100
a = truncate(final_answer, 3)

print("Keyword :- ", len(matches), "/5")
print("Similarity Score :- " , a , " %")
