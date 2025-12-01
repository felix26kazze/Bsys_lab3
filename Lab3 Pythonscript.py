#!/bin/python3
import time
start = time.time()
file1 = '/home/kazze/file1.txt'
file2 = '/home/kazze/file2.txt'

def write_to_file(txtwr):
    for i in range (25):
        timestamp = time.time()
        print("Write Line: " + str(i) + str(timestamp))
        with open(txtwr, "w") as write:
            write.write("Write Line: " + str(i) + str(timestamp))
            write.close()
        time.sleep(1)

def append_to_file(txtap):
    for i in range (25):
        timestamp = time.time()
        print("Write Line: " + str(i) + str(timestamp))
        with open(txtap, "a") as append:
            append.write("Write Line: " + str(i) + str(timestamp) + "\n")
            append.close()
        time.sleep(1)

def read_from_file(txtrd):
    row_count = sum(1 for row in txtrd)
    for i in range(row_count):
        with open(txtrd, "r") as read:
            read.read()
            read.close()
    time.sleep(1)

write_to_file(file1)
append_to_file(file2)
read_from_file(file1)
read_from_file(file2)
