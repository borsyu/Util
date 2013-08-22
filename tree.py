#! /usr/bin/python
#coding gbk

import os
import os.path

def listfiles():
	output = ""
	for root, dirs, files in os.walk("."):
		idx = max(root.rfind("/"), root.rfind("\\"))
		prefix = root[:idx + 1]
		rootIdent = root.count("/") + root.count("\\")
		output += rootIdent * "-*" + "|" + root[idx + 1:] + "\n"
		for fileName in files:
			fullName = os.path.join(root, fileName)
			size = os.path.getsize(fullName)
			print( rootIdent * 2 * " " + fileName + ", " + str(size) )

if __name__ == "__main__":
	listfiles()
