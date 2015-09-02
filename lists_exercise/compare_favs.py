
maggie_fav_foods = open ("maggie_fav_foods.txt")

with open('tia_fav_foods.txt') as tia_fav_foods:
	tia_list = tia_fav_foods.readlines()

with open('maggie_fav_foods.txt') as maggie_fav_foods:
	maggie_list = maggie_fav_foods.readlines()

def compare_favs( list1, list2 ):
	if list1[0] == list2[0]:
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different - sad trombone"

compare_favs( tia_list, maggie_list )

