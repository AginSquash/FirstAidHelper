
def readFile():
    sympotms_dict = {}
    #f = open('FIRSTAIDHELPER.txt')
    with open("FIRSTAIDHELPER.txt", encoding='utf-8') as file:
        for line in file:
            data = line.split("-", maxsplit=1)
            sympotms_dict[data[0]] = data[1]
    return sympotms_dict
import locale
import os.path
locale.setlocale(locale.LC_ALL,"ru")
def inputdate(filename):
	if(os.path.isfile(filename)):
		handle = open(filename,'r',encoding='utf-8')
		a = handle.readline()
		b = handle.readline()
		c = handle.readline()
		handle.close()
		return (a,b,c)
	else:
		return False

def outputdate(filename,name,age,comment):
	handle = open(filename,'w',encoding='utf-8')
	handle.writelines(name+'\n')
	handle.writelines(str(age)+'\n')
	handle.writelines(comment+'\n')
	handle.close()

def Find(filename,findobject):
	handle = open(filename,'r',encoding='utf-8')
	for line in handle:
		findstring = ""
		returnstring = ""
		issecondword = False
		for i in range(len(line)):
			if((line[i]!='/') and (not issecondword)):
				findstring +=line[i]
			elif((line[i]=='/')):
				issecondword = True
			else:
				if(findstring == findobject):
					returnstring+=line[i]
		if(returnstring !=""):
			return returnstring
		#print(findstring)

	
name,age,comment = inputdate("input.txt")
print(name,age,comment)
print(Find("output.txt",'болезнь3'))
outputdate("input.txt","Vasya",18,"Vvedenie v specialnost")



