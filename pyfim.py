#!/usr/bin/env python3

#Python File Integrity Monitor
#Author: Derek Nocera

import os
import hashlib
from time import sleep

def hash_file(filename, hashtype):

    #More hash alogirthms can be added here if they are supported in hashlib
    if hashtype == "SHA1":
        hasher = hashlib.sha1()
    elif hashtype == "MD5":
        hasher = hashlib.md5()
    elif hashtype == "SHA256":
        hasher = hashlib.sha256()
    elif hashtype == "SHA512":
        hasher = hashlib.sha512()
    else:
        #We will choose SHA1 hash in case the hash type is invalid
        hashtype = "SHA1"
        hasher = hashlib.sha1()

    #Read file in chunks to avoid filling our memory for large files
    buf_size = 65536
    with open(filename, "rb") as open_file:
        data = open_file.read(buf_size)
        while data:
            hasher.update(data)
            data = open_file.read(buf_size)
    
    return hasher.hexdigest()

def alert(oldhash, newhash, filename, hashtype):
    print("File change detected at:")
    print(curfile)
    print("Old " + hashtype + ": " + oldhash)
    print("New " + hashtype + ": " + newhash)
    print("")

#Change this to modify the hashing algorithm utilized
#Supported algorithms: MD5, SHA1, SHA256, SHA512
hashtype = "SHA1"

#The directory we want to monitor
directory = "./TestFolder"

#The interval to perform new scans, in seconds
scaninterval = 1

filesigs = {}
#Populate the initial baseline signatures of the file structure
for root, dirs, files in os.walk(directory):
    for file in files:
        curfile = os.path.join(root,file)
        filesigs[curfile] = hash_file(curfile, hashtype)

while True:
    for root, dirs, files in os.walk(directory):
        for file in files:
            curfile = os.path.join(root,file)
            curhash = hash_file(curfile, hashtype)
            if curhash != filesigs[curfile]:
                alert(filesigs[curfile], curhash, curfile, hashtype)
                filesigs[curfile] = curhash
    sleep(scaninterval)


