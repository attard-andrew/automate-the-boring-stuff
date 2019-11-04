#! python3
# renameDates.y - Renames filenames with American MM-DD-YYYY date format to 
# European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format
datePattern = re.compile(r"""^(.*?) # all text before the date
	((0|1)?\d)-						# one or two digits for the month
	((0|1|2|3)?\d)-					# one or two digits for the day
	((19|20)\d\d)					# four digits for the year
	(.*?)$							# all text after the date
	""", re.VERBOSE)

# Loop over the files in the working directory. Note: The os.list argument
# indicates the path, in this case, '.' is the current directory
for amerFilename in os.listdir('.'):
	# mo or 'match object' is used to capture matches from the passed string
	# (amerFilename - which is defined as os.listdir above)
	mo = datePattern.search(amerFilename)
	#  Skip files without a date
	if mo == None:
		continue
	# Get the different part of the filename
	beforePart = mo.group(1)	# Refers to text before the date
	monthPart = mo.group(2)		# Month group
	dayPart = mo.group(4)		# Why is this group 4??? See notes in Evernote
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Form the European-style filename
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# Since we need the file path to rename files, this section comabines the
	# directory path with the filenames. One find the source filepath, and the
	# other finds the destination file path (the new name)
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# Rename the files
	print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
	shutil.move(amerFilename, euroFilename) # To be uncommented after testing