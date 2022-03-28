# File Integrity Monitor
## What is this?
This python program is a cross-plateform proof-of-concept **file integrity monitor** that monitors a sepcific location in a file system to detect changes and alert the user of those changes.

## How does it work?
This program computes initial hash values of all files within the given directory to develop an initial **baseline**.  It then continues to compute the hash values of these files and compares them against the baseline.  It can also detect if new files are added, or if files are deleted.

## Why did you make this?
I wanted to develop a deeper understanding of of how the integrity of information is confirmed, and the methods that could be used to monitor for breaches of data integrity.