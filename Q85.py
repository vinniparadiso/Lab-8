#Vinni, Benthany, Krista
#Number 5
dict_1={"To Kill a Mockingbird":"Harper Lee", "It Ends With Us":"Coleen Hoover", "Cat In The Hat":"Dr. Seuss"}
# if key in dict:
#     if key = "To Kill a Mockingbird":
#         print (dict[key])
# a=dict.get()
# print(dict.get("To Kill a Mockingbird"))
def find_author (title, dict):
    for key in dict:
        if key == title:
            print (dict[key])

find_author("To Kill a Mockingbird", dict_1)
