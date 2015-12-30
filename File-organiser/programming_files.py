#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Anant Sharma <"anant.2047@gmail.com">
# Created:     31-12-2015
#-------------------------------------------------------------------------------


import os,zipfile
from file_compressor_decompressor import organisation_via_compression_decompression

class Programming_files_Sorter(organisation_via_compression_decompression):
	'sorts the programming files folder'
	PROGRAMMING_FILES_FORMATS = [".c",".py",".java",".erl",".class",".sh",".js",".css",".beam",".html",".htm",".ahk",".applescript",".as",".au3",".bat",".bas",".cljs",".cmd",".coffee",".egg",".egt",".erb",".hta",".ibi",".ici",".ijs",".ipynb",".itcl",".jsfl",".lua",".m",".mrc",".ncf",".nut",".php",".pl",".pm",".ps1",".ps1xml",".psc1",".psd1",".psm1",".pyc",".pyo",".r",".rb",".rdp",".scpt",".scptd",".sdl",".syjs",".sypy",".tcl", ".vbs",".xpl",".ebuild"]
	FORMAT_DIR = {
			"c" : 0,"py" : 0,"java" : 0,"erl" : 0,"class" : 0,"sh" : 0,"js" : 0,"css" : 0,"beam" : 0,"html" : 0,"htm" : 0,"ahk" : 0,"applescript" : 0,"as" : 0,"au3" : 0,"bat" : 0,"bas" : 0,"cljs" : 0,"cmd" : 0,"coffee" : 0,"egg" : 0,"egt" : 0,"erb" : 0,"hta" : 0,"ibi" : 0,"ici" : 0,"ijs" : 0,"ipynb" : 0,"itcl" : 0,"jsfl" : 0,"lua" : 0,"m" : 0,"mrc" : 0,"ncf" : 0,"nut" : 0,"php" : 0,"pl" : 0,"pm" : 0,"ps1" : 0,"ps1xml" : 0,"psc1" : 0,"psd1" : 0,"psm1" : 0,"pyc" : 0,"pyo" : 0,"r" : 0,"rb" : 0,"rdp" : 0,"scpt" : 0,"scptd" : 0,"sdl" : 0,"syjs" : 0,"sypy" : 0,"tcl" : 0, "vbs" : 0,"xpl" : 0,"ebuild" : 0		
		}

	def iterate_over_formats(self,file):
		for format in self.PROGRAMMING_FILES_FORMATS:
			if file.endswith(format) and not os.path.isdir(self.PATH + "/" + "file"):
				print file + " with: " + format + " extension found"
				super(Programming_files_Sorter,self).Check_size_and_decide(file,format.replace(".","") + "_files")

	def make_directory(self,str):
		#making desired directory if not present
		try:
			os.makedirs(self.PATH + str)

		except OSError:
			if not os.path.isdir(self.PATH + str):
				raise

	def decompress_file(self,file,str):
		zfile = zipfile.ZipFile(self.PATH  + file)
		zfile.extractall(self.PATH + str)
		print "decompressing it in : " + self.PATH + str + " directory"
		print "removing compressed file"
		os.remove(self.PATH  + file) 

	def start_organisation(self):
		for file in os.listdir( self.PATH ):
			self.iterate_over_formats(file)
		for file in os.listdir( self.PATH ):
			#extracting the str value from the name of the compress file (as name of compress file == name of desired folder) 
			if not os.path.isdir(self.PATH + file):
				format_dir_key,scrap_variable = file.split("_")
				
				if self.FORMAT_DIR.get(format_dir_key) == 0:
					self.make_directory(format_dir_key + "_files")
					self.FORMAT_DIR[format_dir_key] = 1
				
				self.decompress_file(file,format_dir_key + "_files")

# def main():
# 	organiser = Programming_files_Sorter()
# 	organiser.get_path()
# 	# organiser.set_path("/home/anant/pyScript/programming_files/")
# 	organiser.start_organisation()

# if __name__ == "__main__":
# 	main()

def main():
	organiser = organisation_via_compression_decompression()
	organiser.get_path()
	organiser.start_organisation()
	print "press y if you wish to organise programming_files folder created by this script:"
	response = raw_input()
	if response == "y":
		sorter = Programming_files_Sorter()
		sorter.set_path(organiser.PATH + "programming_files/")
		sorter.start_organisation()
	else:
		pass

if __name__ == "__main__":
	main()
