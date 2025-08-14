# 1
fullname = "Mike Jon Vanderpool"
split_name = fullname.split()
print(split_name)

test_scores = "12,14,99"
split_scores = test_scores.split(",")
print(split_scores)

class_roster = "Mike|Jen|Apsan|Yoni"
split_roster = class_roster.split("|")
print(split_roster)

class_roster = """Mike Vanderpool
Jen X
Apsan B
Devin What"""

split_roster = class_roster.splitlines()
print(split_roster)

favorite_foods = """ice cream
soup dumplings
oysters
rice and beans"""

split_fav_foods = favorite_foods.splitlines()
print(split_fav_foods)

name = "Mike Vanderpool"
name_length = len(name)
print(name_length)

my_path = '  /c/users/mike/downloads/   '
path_no_spaces = my_path.strip()
list_folders = path_no_spaces.split("/")
print(list_folders)

composers = "Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
# separate names
composers_split = composers.split(";")
print(composers_split)
third_composer = composers_split[2]
print(third_composer)
comma_position = third_composer.find(",")
print(comma_position)
lastname = third_composer[0:comma_position]
print(lastname)