# -*- coding: utf-8 -*-

seznam = ["pes","kočka","králík","had"]


def getNameShorter5Chars(seznam):
	new = []
	
	for item in seznam:
		if (len(item) < 5):
			new.append(item)
	
	return new
	

print(getNameShorter5Chars(seznam))


	
	
	
	



