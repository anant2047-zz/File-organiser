#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Anant Sharma <"anant.2047@gmail.com">
#Other Contributor : Shreyansh Chajjer,Snimerpal Singh
# Created:     5-01-2016
#-------------------------------------------------------------------------------
import os,mmap
PATH = "/home/"

def search_string(search):
	count = 0
	for path, dirs, all_files in os.walk(PATH):
	 	for file in all_files:
			f = open(path + "/" + file,"rb",0)
			if os.stat(path + "/" + file).st_size == 0L:
				continue
			else:
				mf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
				if mf.find(search) != -1:
					count+=1
					print str(count) + "---> given string present in the file: " + file
					print "location:" + path 
					print "\n"
			f.close()	

def main():
	print "enter the string that you want to search"
	search = raw_input()

	search_string(search)
	
main()
