from sklearn import tree
from sys import stdin 
import re

clf = tree.DecisionTreeClassifier()
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43], [180, 78, 29]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male', 'male']

clf.fit(X, Y);

while (True):
	print("Height: ")
	h = stdin.readline()
	re.sub(r"\n", "", h)
	print("Weight: ")
	w = stdin.readline()
	re.sub(r"\n", "", w)
	print("Age: ")
	a = stdin.readline()
	re.sub(r"\n", "", a)
	test = [[h, w, a]]
	prediction = clf.predict(test)
	print(prediction)
	print("Do you want to make another prediction?")
	is_continue = stdin.readline()
	if (re.match(r"no", is_continue)):
		break;

