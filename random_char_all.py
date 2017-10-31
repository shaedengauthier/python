from random import randint
def randlist(r,usedlist,done,):
	alpha = ["0","1","2","3","4","5","6","7","8","9","0",")",
				"a","A","b","B,","c","C","d","D","e","E","f",
				"F","g","G","h","H","i","I","j","J","k","K",
				"l","L","m","M","n","N","o","O","p","P","q",
				"Q","r","R","s","S","t","T","u","U","v","V",
				"w","W","x","X","y","Y","z","Z","`","[","]",
				"\\",";","'",",",".","/","~","!","@","#","$",
				"%","^","&","*","(",")","_","+","{","}","|",
				":",'"',"<",">","?"]
	c = alpha[r]
	return c # this is belongs to ranlist(r)
	
def main():
	count = 0
	checklist = [0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,0,
			0,0,0,0]
	done = False
	while (done == False):
		r = randint(0,93)
		while (used[r] != 1):
			c,used,done = randlist(r,used,done)
			#print (used)
			print(c,end="")
			count += 1
	print ("\n\n",count," randoms numbers used")

	main()
