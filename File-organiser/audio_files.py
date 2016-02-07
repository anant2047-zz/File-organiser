#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Anant Sharma <"anant.2047@gmail.com">
#Other Contributor : Shreyansh Chajjer,Snimerpal Singh
# Created:     12-01-2016
#-------------------------------------------------------------------------------
import os
import requests,sys,bs4
from script import File_organiser

class audio_files_Sorter(File_organiser):
	'sorts the files in audio_files directory on the basis of the movies they belong to, can also sort normal containing music files'
	PATH = "/home/anant/pyScript/audio_files/"

	def make_directory(self,str):
		#making desired directory if not present
		try:
				os.makedirs(self.PATH + str)
				print "making " + str + " directory"

		except OSError:
			if not os.path.isdir(self.PATH + str):
				raise

	def iterate_over_formats(self,file,str):
		for format in self.FORMAT_LIST[str]:
			if file.endswith(format):
				return True
		return False

	def find_movie_name(self,name):
		res = requests.get('http://google.com/search?q=' + ''.join("movie " + name + " song"))
		res.raise_for_status()
		soup = bs4.BeautifulSoup(res.text , "lxml")
		linkElems = soup.select('._m3b')
		print name
		if len(linkElems) > 0 :
			directory_name = linkElems[0].getText()
		else:
			directory_name = "unknown"

		return directory_name

	def start_organisation(self):
		for file in os.listdir( self.PATH ):
			if self.iterate_over_formats(file,"audio_files"):
				print "file : " + file + " found"
				name,format = file.split("." , 1)
				name_split = name.split("-")
				
				for i in range(len(name_split)):
					directory_name = self.find_movie_name(name_split[i])
					if not directory_name == "unknown":
						break

				if not directory_name == "unknown":
					directory_name = ''.join(i for i in directory_name if i.isalpha())
					directory_name = directory_name.lower()

				self.make_directory(directory_name)
				self.transfer_to_directory(file,directory_name)

def main():
	organiser = audio_files_Sorter()
	#organiser.get_path()
	organiser.start_organisation()

if __name__ == "__main__":
	main()


