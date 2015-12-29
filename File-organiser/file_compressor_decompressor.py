#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Anant Sharma <"anant.2047@gmail.com">
#Other Contributor : Shreyansh Chajjer,Snimerpal Singh
# Created:     30-12-2015
#-------------------------------------------------------------------------------

import os,shutil,zipfile


#global variables
PATH = "/home/anant/pyScript/"
DIR = {
	"script_files":0,
	"video_files" : 0,
	"audio_files" : 0,
	"ppt_files" : 0,
	"document_files" : 0,
	"compressed_files" : 0,
	"image_files" : 0
	}
SCRIPT_FORMATS = [".c",".py",".java",".erl",".class",".sh",".js",".css",".beam"]	
VIDEO_FORMATS = [".webm",".mkv",".mp4",".mpeg",".flv",".vob",".ogv",".ogg",".drc",".gif",".gifv",".mng",".avi",".mov",".qt",".wmv",".yuv",".rm",".rmvb",".asf",".webm",".m4v",".mpg",".m2v",".svi",".3gp",".3g2",".mxf",".roq",".nsv",".f4v",".f4p",".f4a",".f4b"]
AUDIO_FORMATS = [".wav",".aa",".mp3",".aac",".aax",".act",".aiff",".amr",".ape",".au",".awb",".dct",".dss",".dvf",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mpc",".msv",".ogg",".oga",".opus",".ra",".raw",".sIn",".tta",".vox",".wrna",".wv",".webm"]
PRESENTATION_FORMATS = [".gslides",".key", ".keynote",".nb",".nbp" ,".odp" ,".otp" ,".pez" ,".pot" ,".pps" ,".ppt" ,".pptx" ,".prz" ,".sdd" ,".shf" ,".show" ,".shw" ,".slp" ,".sspss", ".sti" ,".sxi" , ".thmx" ,".watch" ]
DOCUMENT_FORMATS = [".602" ,".abw" ,".acl" ,".afp" ,".ami" ,".ans" ,".asc" ,".aww" ,".ccf" ,"csv" ,"cwk" ,".dbk" ,".doc" ,".docm" ,".docx" ,".dot" ,".dotx" ,".egt" ,".epub" ,".ezw" ,".fdx" ,".ftm" ,".ftx" ,".gdoc" ,".html" ,".htm" ,".hwpml" ,".log" ,".lwp" ,".mbp" ,".md" ,".mcw" ,".mobi" ,".nb" ,".nbp" ,".odm" ,".odt" ,".ott" ,".omm" ,".pages" ,".pap" ,".pdax" , ".pdf" ,".rtf",".quox" ,".rpt" ,".sdw" ,".se" ,".stw" ,".sxw" ,".tex" ,".info" ,".txt" ,".uof" ,".uoml" ,".via" ,".wpd" ,".wps" ,".wpt" ,".wrd" ,".wrf" ,".wri" ,".xhtml" ,".xml" ,".xps" ]
COMPRESSED_FORMATS = [".zip",".tar.bz2",".cab", ".?q?", ".7z" ,".aac" ,".ace",".alz" ,".apk" ,".at3" ,".bke" ,".arc",".arj" ,".ass" ,".b" ,".ba" ,".big" ,".bik" ,".bin" ,".bkf" ,".bzip2" ,".bld" ,".c4" ,".cab" ,".cals" ,".clipfair" ,".cpt",".sea" ,".daa" ,".deb" ,".dmg" ,".ddz" ,".dpe" ,".egg" ,".egt" ,".ecab" , ".ezip",".ess" ,".gho", ".ghs",".gz",".ipg" ,".lbr",".Lawrence" ,".lbr",".lqr" ,".lha" ,".lzh",".lzip" ,".lz",".lzo",".lzma",".lzx",".mbw",".mpq",".bin",".nth",".osz" ,".pak" ,".par",".par2",".paf",".pyk",".pk3",".pk4",".rar",".rag",".rags",".rpm",".sen",".sit",".sitx ",".skb",".tar" ,".tar.gz",".tgz",".tb",".tib",".uha",".uue",".viv" ,".vol" ,".vsa",".z",".zoo"]
IMAGE_FORMATS = [".ani", ".anim", ".apng", ".art", ".bmp" ,".bpg" ".bsave", ".cal" ,".cin", ".cpc" ,".cpt", ".dds", ".dpx" ,".ecw", ".exr",".fits", ".flic", ".flif", ".fpx" ,".gif" ,".hdri", ".hevc" ,".icer", "icns", ".ico" , ".cur", ".ics" ,".ilbm", ".jbig" , ".jbig2" ,".jng" ,".jpeg", ".jpeg 2000" ,".jpeg-ls", ".jpeg xr", ".miff", ".nrdd", ".pam", ".pbm" , ".pgm" , ".ppm" , ".pnm", ".pcx" ,".pgf", "PICtor", ".png", ".psd" , ".psb", ".psp", ".qtvr", ".ras" ,".rbe",".jpeg-hdr", ".logluv" ".tiff", ".sgi", ".tga",".wbmp", ".webp" ,".xbm", ".xcf", ".xpm", ".xwd",".ciff", ".dng" ,".ai", ".ccdr", ".cgm", ".dxf", ".eva", ".emf"	, ".gerber", ".hvif", ".iges", ".pgml", ".svg", ".vml", ".wmf", ".xar" ,".cdf", ".djvu", ".eps", ".pict", ".ps" ,".swf", ".xaml"]
FORMAT_LIST = { "script_files":SCRIPT_FORMATS , "video_files":VIDEO_FORMATS,"audio_files":AUDIO_FORMATS,"ppt_files":PRESENTATION_FORMATS,"document_files":DOCUMENT_FORMATS,"compressed_files":COMPRESSED_FORMATS,"image_files":IMAGE_FORMATS} 
DIRECTORY_NAMES = ["script_files","video_files","audio_files","ppt_files","document_files","compressed_files","image_files"]

def decompress_file(file,str):
	zfile = zipfile.ZipFile(PATH + "/" + str + "/" + file)
	zfile.extractall(PATH + str)
	print "decompressing it in : " + PATH + str + " directory"
	print "removing compressed file"
	os.remove(PATH + "/" + str + "/" + file) 


def transfer_to_directory(file,str):
	global PATH
	global DIR

	#making desired directory
	try:
		if DIR.get(str) == 0:
			os.makedirs(PATH + str)
			print "making " + str + " directory"
			DIR[str] = 1

	except OSError:
		if not os.path.isdir(PATH + str):
			raise


	file_name = PATH + file

	#moving compressed file and than decompressing them
	if  file.endswith(".zip"):
		try:
			shutil.move(file_name,PATH + str)
			print "moving " + file + " to " + str + " directory"

		except shutil.Error:
			print "ERROR: " + file + " already exists in " + " " + str + " directory "
			print "Manual copying is recommended. Leaving this file"
			pass
		decompress_file(file,str)
	
	#moving normal files
	else:
		try:
			shutil.move(file_name,PATH + str)
			print "moving " + file + " to " + str + " directory"
		except shutil.Error:
			print "ERROR: " + file + " already exists in " + " " + str + " directory "
			print "Manual copying is recommended. Leaving this file"
			pass


def compressing_file(file,str):
	os.chdir(PATH)
	z = zipfile.ZipFile(PATH + str + ".zip", "a",zipfile.ZIP_DEFLATED)
	z.write(file)
	os.remove(file)
	z.close()

	#if size of compressed file becomes bigger than 1MB, move it to desired directory and decompress it.
	if os.stat(PATH + str + ".zip").st_size > 1000000:
		print "size of compressed file exceeds 1MB"
		print "\n"
		transfer_to_directory( str + ".zip",str)

def Check_size_and_decide(file,str):
	if os.stat(PATH + file).st_size > 1000000 :
		print "size of file greater than 1MB"
		print "directly transfering it to the required folder"
		transfer_to_directory(file,str)
	#no need to compress
	elif str == "compressed_files":
		transfer_to_directory(file,str)
	#better to compress small files and then transfer them
	else :
		print "size of file: " + file + " is small, compressing it"
		compressing_file(file,str)	



def iterate_over_formats(file,str):
	for format in FORMAT_LIST[str]:
		if file.endswith(format):
			print file + " " + str + " found"
			Check_size_and_decide(file,str)
			return True

	return False



def main():
	global DIRECTORY_NAMES
	print "enter path of the directory :: should end with /"
	#PATH = str(raw_input())

	for file in os.listdir( PATH ):
		if iterate_over_formats(file,"script_files"):
			pass
		elif(iterate_over_formats(file,"video_files")):
			pass
		elif(iterate_over_formats(file,"audio_files")):
			pass
		elif(iterate_over_formats(file,"ppt_files")):
			pass
		elif(iterate_over_formats(file,"document_files")):
			pass
		elif(iterate_over_formats(file,"compressed_files")):
			pass
		elif(iterate_over_formats(file,"image_files")):
			pass


	# Extra Cases: In linux some word files are not given extensions so we need to run a loop again and sort them accordingly
	for file in os.listdir( PATH ):
		if file.endswith("") and not file.endswith(".zip") and os.path.isfile(PATH + file) :
			Check_size_and_decide(file,"document_files")
	

	#moving all compressed file to desired folder and decompressing it(size of the compressed file may not have exceeded 1MB,
	# so those files needs to be transfered)
	for file in os.listdir( PATH ):
		if file.endswith(".zip"):

			#extracting the str value from the name of the compress file (as name of compress file == name of desired folder) 
			str,scrap_variable = file.split(".z")
			if str in DIRECTORY_NAMES:
				transfer_to_directory(file,str)
			
			#if it is not compressed file that is used for fast copying and is a normal user's compressed file 
			#than transfer it normally to the desired folder
			else:
				file_name = PATH + file
				str = "compressed_files"
				try:
					shutil.move(file_name,PATH + str)
					print "moving " + file + " to " + str + " directory"
				except shutil.Error:
					print "ERROR: " + file + " already exists in " + " " + str + " directory "
					print "Manual copying is recommended. Leaving this file"
					pass

if __name__ == "__main__":
	main()

