# File Integrity Monitor
## What is this?
This python program is a cross-plateform proof-of-concept **file integrity monitor** that monitors a sepcific location in a file system to detect changes and alert the user of those changes.

## How does it work?
This program computes initial hash values of all files within the given directory to develop an initial **baseline**.  It then continues to compute the hash values of these files and compares them against the baseline.

![Example](https://i.imgur.com/OyaGfdq.png "Example")

## Usage
Edit the source file and make changes to the appropriate variables to change top level directory, hashing algorithm used, and scan interval.

![Configuration](https://i.imgur.com/Zr8dPYJ.png "Configuration")

Then simply run the program, and changes will be displayed to the command line.

## Why did was this made?
I wanted to develop a deeper understanding of of how the integrity of information is verified, and the methods that could be used to monitor for breaches of data integrity.