#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Anant Sharma <"anant.2047@gmail.com">
# Created:     26-12-2015
#-------------------------------------------------------------------------------

import os,shutil
class File_organiser(object):
	'A class to organise file in a direcory'

	#class variables
	PATH = "//"
	DIR = {
		"programming_files":0,
		"video_files" : 0,
		"audio_files" : 0,
		"ppt_files" : 0,
		"document_files" : 0,
		"compressed_files" : 0,
		"image_files" : 0
		}
	SCRIPT_FORMATS = [".c",".py",".java",".erl",".class",".sh",".js",".css",".beam",".html",".htm",".ahk",".applescript",".as",".au3",".bat",".bas",".cljs",".cmd",".coffee",".egg",".egt",".erb",".hta",".ibi",".ici",".ijs",".ipynb",".itcl",".jsfl",".lua",".m",".mrc",".ncf",".nut",".php",".pl",".pm",".ps1",".ps1xml",".psc1",".psd1",".psm1",".pyc",".pyo",".r",".rb",".rdp",".scpt",".scptd",".sdl",".syjs",".sypy",".tcl", ".vbs",".xpl",".ebuild"]	
	VIDEO_FORMATS = [".webm",".mkv",".mp4",".mpeg",".flv",".vob",".ogv",".ogg",".drc",".gif",".gifv",".mng",".avi",".mov",".qt",".wmv",".yuv",".rm",".rmvb",".asf",".webm",".m4v",".mpg",".m2v",".svi",".3gp",".3g2",".mxf",".roq",".nsv",".f4v",".f4p",".f4a",".f4b"]
	AUDIO_FORMATS = [".wav",".aa",".mp3",".aac",".aax",".act",".aiff",".amr",".ape",".au",".awb",".dct",".dss",".dvf",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mpc",".msv",".ogg",".oga",".opus",".ra",".raw",".sIn",".tta",".vox",".wrna",".wv",".webm"]
	PRESENTATION_FORMATS = [".gslides",".key", ".keynote",".nb",".nbp" ,".odp" ,".otp" ,".pez" ,".pot" ,".pps" ,".ppt" ,".pptx" ,".prz" ,".sdd" ,".shf" ,".show" ,".shw" ,".slp" ,".sspss", ".sti" ,".sxi" , ".thmx" ,".watch" ]
	DOCUMENT_FORMATS = [".602" ,".abw" ,".acl" ,".afp" ,".ami" ,".ans" ,".asc" ,".aww" ,".ccf" ,"csv" ,"cwk" ,".dbk" ,".doc" ,".docm" ,".docx" ,".dot" ,".dotx" ,".egt" ,".epub" ,".ezw" ,".fdx" ,".ftm" ,".ftx" ,".gdoc" ,".html" ,".htm" ,".hwpml" ,".log" ,".lwp" ,".mbp" ,".md" ,".mcw" ,".mobi" ,".nb" ,".nbp" ,".odm" ,".odt" ,".ott" ,".omm" ,".pages" ,".pap" ,".pdax" , ".pdf" ,".rtf",".quox" ,".rpt" ,".sdw" ,".se" ,".stw" ,".sxw" ,".tex" ,".info" ,".txt" ,".uof" ,".uoml" ,".via" ,".wpd" ,".wps" ,".wpt" ,".wrd" ,".wrf" ,".wri" ,".xhtml" ,".xml" ,".xps" ]
	COMPRESSED_FORMATS = [".zip",".tar.bz2",".cab", ".?q?", ".7z" ,".aac" ,".ace",".alz" ,".apk" ,".at3" ,".bke" ,".arc",".arj" ,".ass" ,".b" ,".ba" ,".big" ,".bik" ,".bin" ,".bkf" ,".bzip2" ,".bld" ,".c4" ,".cab" ,".cals" ,".clipfair" ,".cpt",".sea" ,".daa" ,".deb" ,".dmg" ,".ddz" ,".dpe" ,".egg" ,".egt" ,".ecab" , ".ezip",".ess" ,".gho", ".ghs",".gz",".ipg" ,".lbr",".Lawrence" ,".lbr",".lqr" ,".lha" ,".lzh",".lzip" ,".lz",".lzo",".lzma",".lzx",".mbw",".mpq",".bin",".nth",".osz" ,".pak" ,".par",".par2",".paf",".pyk",".pk3",".pk4",".rar",".rag",".rags",".rpm",".sen",".sit",".sitx ",".skb",".tar" ,".tar.gz",".tgz",".tb",".tib",".uha",".uue",".viv" ,".vol" ,".vsa",".z",".zoo"]
	IMAGE_FORMATS = [".ani", ".anim", ".apng", ".art", ".bmp" ,".bpg" ".bsave", ".cal" ,".cin", ".cpc" ,".cpt", ".dds", ".dpx" ,".ecw", ".exr",".fits", ".flic", ".flif", ".fpx" ,".gif" ,".hdri", ".hevc" ,".icer", "icns", ".ico" , ".cur", ".ics" ,".ilbm", ".jbig" , ".jbig2" ,".jng" ,".jpeg", ".jpeg 2000" ,".jpeg-ls", ".jpeg xr", ".miff", ".nrdd", ".pam", ".pbm" , ".pgm" , ".ppm" , ".pnm", ".pcx" ,".pgf", "PICtor", ".png", ".psd" , ".psb", ".psp", ".qtvr", ".ras" ,".rbe",".jpeg-hdr", ".logluv" ".tiff", ".sgi", ".tga",".wbmp", ".webp" ,".xbm", ".xcf", ".xpm", ".xwd",".ciff", ".dng" ,".ai", ".ccdr", ".cgm", ".dxf", ".eva", ".emf"	, ".gerber", ".hvif", ".iges", ".pgml", ".svg", ".vml", ".wmf", ".xar" ,".cdf", ".djvu", ".eps", ".pict", ".ps" ,".swf", ".xaml"]
	FORMAT_LIST = { "programming_files":SCRIPT_FORMATS , "video_files":VIDEO_FORMATS,"audio_files":AUDIO_FORMATS,"ppt_files":PRESENTATION_FORMATS,"document_files":DOCUMENT_FORMATS,"compressed_files":COMPRESSED_FORMATS,"image_files":IMAGE_FORMATS} 
	DIRECTORY_NAMES = ["programming_files","video_files","audio_files","ppt_files","document_files","compressed_files","image_files"]


	def make_directory(self,str):
		#making desired directory if not present
		try:
			if self.DIR.get(str) == 0:
				os.makedirs(self.PATH + str)
				print "making " + str + " directory"
				self.DIR[str] = 1

		except OSError:
			if not os.path.isdir(self.PATH + str):
				raise

	def transfer_to_directory(self,file,str):
		file_name = self.PATH + file 
		try:
			shutil.move(file_name,self.PATH + str)
			print "moving " + file + " to " + str + " directory"
		except shutil.Error:
			print "ERROR: " + file + " already exists in " + " " + str + " directory "
			print "Manual copying is recommended. Leaving this file"
			pass

	def iterate_over_formats(self,file,str):
		for format in self.FORMAT_LIST[str]:
			if file.endswith(format):
				print file + " " + str + " found"
				self.make_directory(str)
				self.transfer_to_directory(file,str)
				return True

		return False

	def set_path(self,PATH):
		self.PATH = PATH

	def get_path(self):
		print "enter path of the directory :: should end with /"
		PATH = str(raw_input())
		# self.PATH = PATH
		self.set_path(PATH)
		# #<----------warning--------->
		# self.set_path(self.PATH)

	def path_checker(self):
		print "you have entered this path: " + self.PATH
		print "enter y to run the script else press n"
		check = str(raw_input())
		if check.lower() == 'y':
			return True
		else :
			return False

	def start_organisation(self):
		Check = self.path_checker()

		if Check :
			for file in os.listdir( self.PATH ):
				if self.iterate_over_formats(file,"programming_files"):
					pass
				elif(self.iterate_over_formats(file,"video_files")):
					pass
				elif(self.iterate_over_formats(file,"audio_files")):
					pass
				elif(self.iterate_over_formats(file,"ppt_files")):
					pass
				elif(self.iterate_over_formats(file,"document_files")):
					pass
				elif(self.iterate_over_formats(file,"compressed_files")):
					pass
				elif(self.iterate_over_formats(file,"image_files")):
					pass

		else:
			print "end."

def main():
	organiser = File_organiser()
	organiser.get_path()
	organiser.start_organisation()

if __name__ == "__main__":
	main()



