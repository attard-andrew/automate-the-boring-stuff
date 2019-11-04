#! python3
# backup_to_zip.py - Copies an entire folder and its contents into a ZIP file
# whose filename increments

import zipfile, os

def backupToZip(folder):
	# Backup the entire contents of 'folder' into a ZIP file
	folder = os.path.abspath(folder) # ensures that the path is absolute

	# Determine the filename this code should use based on what files already
	# exist
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFilename):
			break
		number = number + 1

	# Create the ZIP file
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# For the folder, subfolders, and files passed to the function...
	for foldername, subfolders, filenames in os.walk(folder):
		# Print a message stating which folder's files are being added
		print('Adding files in %s...' % (foldername))
		# Write the current folder to the previously created ZIP object
		backupZip.write(foldername)

		for filename in filenames:
			if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
				continue # Then move to the next iteration and continue executing (prevents .zip files from being backed up)
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()
	print('Done.')

backupToZip('C:\\dev_projects\\automate_the_boring_stuff\\chapter_projects\\09_zip_backup\\folder_to_backup')