import random, time, os

def Ball():

	os.system('cls')
	what = ("Your answer is mine!", "I don't quite know..", "Who knows...")

	should = ("Yes, yes you should..", "Don't, please don't", "Must!")

	isvar = ("I believe so.", "No, not at all.....")

	amvar = ("Yes, definetly", "No, not at all.....")

	whyvar = ("Your answer is mine...", "I dont quite know..")

	can = ("Yes, indeed", "No.... Idiot!", "Im not sure..")

	question = input("The answer resides within your question, which is..?\n:")

	first, *middle, last = question.split()

	rwhat = random.choice(what)
	rshoud = random.choice(should)
	ris = random.choice(isvar)
	ram = random.choice(amvar)
	rwhy = random.choice(whyvar)
	rcan = random.choice(can)

	first = str(first)

	if (first) in ("what", "What"):
	    print (rwhat)
	    time.sleep(1)
	    os.system('pause')
	    Ball()

	elif (first) in ("should", "Should"):
	    print (rshoud)
	    time.sleep(1)
	    os.system('pause')
	    Ball()

	elif (first) in ("is", "Is"):
	    print (ris)
	    time.sleep(1)
	    os.system('pause')
	    Ball()

	elif (first) in ("am", "Am"):
	    print (ram)
	    time.sleep(1)
	    os.system('pause')
	    Ball()

	elif (first) in ("why", "Why"):
	    print (rwhy)
	    time.sleep(1)
	    os.system('pause')
	    Ball()

	elif (first) in ("can", "Can"):
	    print (rcan)
	    time.sleep(1)
	    os.system('pause')
	    Ball()
	else:
	    print (rwhat)
	    time.sleep(1)
	    os.system('pause')
	    Ball()

Ball()


