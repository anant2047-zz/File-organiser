#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Anant Sharma <"anant.2047@gmail.com">
#Other Contributor : Shreyansh Chajjer,Snimerpal Singh
# Created:     30-12-2015
#-------------------------------------------------------------------------------

import os,shutil,zipfile
from script import File_organiser

class organisation_via_compression_decompression(File_organiser):
	PATH = "//"
	
	def set_path(self,PATH):
		self.PATH = PATH

	def correct_path(self):
		if not self.PATH.endswith("/") :
			self.PATH = self.PATH + "/"
		else:
			pass

	def get_path(self):
		print "enter path of the directory :: should end with /"
		PATH = str(raw_input())
		self.set_path(PATH)
		#if user forgets to enter "/" in the end append "/" in the end
		self.correct_path()


	def decompress_file(self,file,str):
		zfile = zipfile.ZipFile(self.PATH + str + "/" + file)
		zfile.extractall(self.PATH + str)
		print "decompressing it in : " + self.PATH + str + " directory"
		print "removing compressed file"
		os.remove(self.PATH + str + "/" + file) 


	def transfer_to_directory(self,file,str):
		#making desired directory
		super(organisation_via_compression_decompression,self).make_directory(str)

		file_name = self.PATH + file
		#moving compressed file and than decompressing them
		if  file.endswith(".zip"):
			try:
				shutil.move(file_name,self.PATH + str)
				print "moving " + file + " to " + str + " directory"

			except shutil.Error:
				print "ERROR: " + file + " already exists in " + " " + str + " directory "
				print "Manual copying is recommended. Leaving this file"
				pass
			self.decompress_file(file,str)
		
		#moving normal files
		else:
			super(organisation_via_compression_decompression,self).transfer_to_directory(file,str)


	def compressing_file(self,file,str):
		os.chdir(self.PATH)
		z = zipfile.ZipFile(self.PATH + str + ".zip", "a",zipfile.ZIP_DEFLATED)
		z.write(file)
		os.remove(file)
		z.close()

		#if size of compressed file becomes bigger than 1MB, move it to desired directory and decompress it.
		if os.stat(self.PATH + str + ".zip").st_size > 1000000:
			print "size of compressed file exceeds 1MB"
			print "\n"
			self.transfer_to_directory( str + ".zip",str)

	def Check_size_and_decide(self,file,str):
		if os.stat(self.PATH + file).st_size > 1000000 :
			print "size of file greater than 1MB"
			print "directly transfering it to the required folder"
			self.transfer_to_directory(file,str)
		#no need to compress
		elif str == "compressed_files":
			self.transfer_to_directory(file,str)
		#better to compress small files and then transfer them
		else :
			print "size of file: " + file + " is small, compressing it"
			self.compressing_file(file,str)	



	def iterate_over_formats(self,file,str):
		for format in self.FORMAT_LIST[str]:
			if file.endswith(format):
				print file + " " + str + " found"
				self.Check_size_and_decide(file,str)
				return True

		return False



	def start_organisation(self):
		super(organisation_via_compression_decompression,self).start_organisation()
		
		# Extra Cases: In linux some word files are not given extensions so we need to run a loop again and sort them accordingly
		for file in os.listdir( self.PATH ):
			if file.endswith("") and not file.endswith(".zip") and os.path.isfile(self.PATH + file) :
				self.Check_size_and_decide(file,"document_files")
		

		#moving all compressed file to desired folder and decompressing it(size of the compressed file may not have exceeded 1MB,
		# so those files needs to be transfered)
		for file in os.listdir( self.PATH ):
			if file.endswith(".zip"):

				#extracting the str value from the name of the compress file (as name of compress file == name of desired folder) 
				str,scrap_variable = file.split(".z")
				if str in self.DIRECTORY_NAMES:
					self.transfer_to_directory(file,str)
				
				#if it is not compressed file that is used for fast copying and is a normal user's compressed file 
				#than transfer it normally to the desired folder
				else:
					file_name = self.PATH + file
					str = "compressed_files"
					try:
						shutil.move(file_name,self.PATH + str)
						print "moving " + file + " to " + str + " directory"
					except shutil.Error:
						print "ERROR: " + file + " already exists in " + " " + str + " directory "
						print "Manual copying is recommended. Leaving this file"
						pass


def main():
	organiser = organisation_via_compression_decompression()
	organiser.set_path("/home/anant/pyScript/")
	organiser.start_organisation()

if __name__ == "__main__":
	main()

