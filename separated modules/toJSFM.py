def toJSFM(convert):
	converted = "["
	for i in range(0, len(convert)): 					#Parses through the string you want to convert
		converted += "[" + str(i*5) + ", " + str(convert[i]) + "]"	#Formats it
		if(i < len(convert)-1):
			converted += ", "					#Checks for last entry to determine if it should
		else:								#end with ", " or "]"
			converted += "]"

	#print converted
	return converted

conv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

toJSFM(conv)
