def deZipper(inputZip):
	'''   A general purpose tool that unzips a folder
             to a folder of the same name (minus the .zip)
             in the same directory.
          deZipper(inputZippedFolder)			 
	'''
    import zipfile, os.path,shutil
    
    name = inputZip.split('.')
    zipPathSplit = os.path.split(inputZip)
    os.chdir(zipPathSplit[0])
    outDir = zipPathSplit[1].split('.')[0]  
    try:  shutil.rmtree(outDir)
    except:  pass
    os.mkdir(outDir)
    fh = open(inputZip,'rb')
    z = zipfile.ZipFile(fh)
    print z.namelist()
    for name in z.namelist():
        outfile = open(outDir+os.sep+name,'wb')
        outfile.write(name)
        outfile.close()
    fh.close()