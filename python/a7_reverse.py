def rev(l1):
	lFor = l1
	lRev = 0				
	for i in range(len(str(l1))):
		numRev 	= lFor % 10 		# TAKE ONE'S DIGIT
		lFor 	= (lFor-numRev)/10	# UPDATE lFor WITHOUT ONE'S DIGIT
		lRev 	= lRev*10 + numRev	# CREATE REVERSE NUMBER
	return lRev