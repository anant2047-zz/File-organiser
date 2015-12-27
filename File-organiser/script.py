import os,shutil

#global variables
PATH = "/home/anant/pyScript/"
DIR = {
	"c_files" : 0,
	"java_files" : 0,
	"python_files" : 0,
	"video_files" : 0,
	"audio_files" : 0,
	"ppt_files" : 0,
	"document_files" : 0,
	"compressed_files" : 0	
	}
VIDEO_FORMATS = [".webm",".mkv",".mp4",".mpeg",".flv",".vob",".ogv",".ogg",".drc",".gif",".gifv",".mng",".avi",".mov",".qt",".wmv",".yuv",".rm",".rmvb",".asf",".webm",".m4v",".mpg",".m2v",".svi",".3gp",".3g2",".mxf",".roq",".nsv",".f4v",".f4p",".f4a",".f4b"]
AUDIO_FORMATS = [".wav",".aa",".mp3",".aac",".aax",".act",".aiff",".amr",".ape",".au",".awb",".dct",".dss",".dvf",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mpc",".msv",".ogg",".oga",".opus",".ra",".raw",".sIn",".tta",".vox",".wrna",".wv",".webm"]
PRESENTATION_FORMATS = [".gslides",".key", ".keynote",".nb",".nbp" ,".odp" ,".otp" ,".pez" ,".pot" ,".pps" ,".ppt" ,".pptx" ,".prz" ,".sdd" ,".shf" ,".show" ,".shw" ,".slp" ,".sspss", ".sti" ,".sxi" , ".thmx" ,".watch" ]
DOCUMENT_FORMATS = [".602" ,".abw" ,".acl" ,".afp" ,".ami" ,".ans" ,".asc" ,".aww" ,".ccf" ,"csv" ,"cwk" ,".dbk" ,".doc" ,".docm" ,".docx" ,".dot" ,".dotx" ,".egt" ,".epub" ,".ezw" ,".fdx" ,".ftm" ,".ftx" ,".gdoc" ,".html" ,".htm" ,".hwpml" ,".log" ,".lwp" ,".mbp" ,".md" ,".mcw" ,".mobi" ,".nb" ,".nbp" ,".odm" ,".odt" ,".ott" ,".omm" ,".pages" ,".pap" ,".pdax" , ".pdf" ,".rtf",".quox" ,".rpt" ,".sdw" ,".se" ,".stw" ,".sxw" ,".tex" ,".info" ,".txt" ,".uof" ,".uoml" ,".via" ,".wpd" ,".wps" ,".wpt" ,".wrd" ,".wrf" ,".wri" ,".xhtml" ,".xml" ,".xps" ]
COMPRESSED_FORMATS = [".zip",".cab", ".?q?", ".7z" ,".aac" ,".ace",".alz" ,".apk" ,".at3" ,".bke" ,".arc",".arj" ,".ass" ,".b" ,".ba" ,".big" ,".bik" ,".bin" ,".bkf" ,".bzip2" ,".bld" ,".c4" ,".cab" ,".cals" ,".clipfair" ,".cpt",".sea" ,".daa" ,".deb" ,".dmg" ,".ddz" ,".dpe" ,".egg" ,".egt" ,".ecab" , ".ezip",".ess" ,".gho", ".ghs",".gz",".ipg" ,".lbr",".Lawrence" ,".lbr",".lqr" ,".lha" ,".lzh",".lzip" ,".lz",".lzo",".lzma",".lzx",".mbw",".mpq",".bin",".nth",".osz" ,".pak" ,".par",".par2",".paf",".pyk",".pk3",".pk4",".rar",".rag",".rags",".rpm",".sen",".sit",".sitx ",".skb",".tar" ,".tar.gz",".tgz",".tb",".tib",".uha",".uue",".viv" ,".vol" ,".vsa",".z",".zoo"]
FORMAT_LIST = {"video_files":VIDEO_FORMATS,"audio_files":AUDIO_FORMATS,"ppt_files":PRESENTATION_FORMATS,"document_files":DOCUMENT_FORMATS,"compressed_files":COMPRESSED_FORMATS} 

def transfer_to_directory(file,str):
	global PATH
	global DIR
	try:
		if DIR.get(str) == 0:
			os.makedirs(PATH + str)
			print "making " + str + " directory"
			DIR[str] = 1

	except OSError:
		if not os.path.isdir(PATH + str):
			raise
	file_name = PATH + file 
	try:
		shutil.move(file_name,PATH + str)
		print "moving " + file + " to " + str + " directory"
	except shutil.Error:
		print "ERROR: " + file + " already exists in " + " " + str + " directory "
		print "Manual copying is recommended. Leaving this file"
		pass

def iterate_over_formats(file,str):
	for format in FORMAT_LIST[str]:
		if file.endswith(format):
			print file + " " + str + " found"
			transfer_to_directory(file,str)
			return True

def main():

	print "enter path of the directory :: should end with /"
	#PATH = str(raw_input())

	for file in os.listdir( PATH ):
		if file.endswith(".c") :
			print file + ".c file format found => "
			transfer_to_directory(file,"c_files")
		
		elif file.endswith(".java") or file.endswith(".java") or file.endswith(".jar")  :
			print file + ".java file format found => "
			transfer_to_directory(file,"java_files")
		
		elif file.endswith(".py") :
			print file + ".py file format found => "
			transfer_to_directory(file,"python_files")

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
		
main()

