import tkinter
from tkinter import filedialog
import shutil
import codecs
import os
import string

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def ensure_file(src,f):
	if not os.path.isfile(f):
		shutil.copy(src,np)	

def copy_song(src,f):
	try:
		ensure_dir(np)
	except:
		print('Problem making Directory')
		pass
	try:
		ensure_file(line.strip(),np)
	except:
		print('Problem making File:')
		pass
		
##Dialog options
#root = tkinter.Tk()
#root.withdraw()
#write_path = filedialog.askopenfilename()

file_path=r"F:\Favorites_full.m3u8"
ext=os.path.splitext(file_path)[1]

if ext=='.m3u':
	fp=open(file_path,'r')
	write_path=r"F:Music"
elif ext=='.m3u8':
	#have to decode as utf-8-sig to remove BOM characters at start of file
	fp=codecs.open(file_path,'r',encoding='utf-8-sig')
	write_path=r"F:Music"
	
#Assumes file structure is <blah>\Artist\Album\song and grabs <blah>

line=fp.readline().strip()

base=line.split("\\")
base="\\".join(base[:-3])

np=line.replace(base,write_path)
copy_song(line,np)

for line in fp:
	np=line.replace(base,write_path).strip()
	copy_song(line.strip(),np)

fp.close()

##Need to figure out how to write to either MTP or PTP devices for now...
##write to a file and then copy manually.