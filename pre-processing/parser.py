import csv
import os
import sys

print(len(sys.argv))

if len(sys.argv) == 3:
    input_dir = sys.argv[1] 
else:
    input_dir= "./tempdir"

if len(sys.argv) == 3:
    input_dir = sys.argv[1]
    output_file = sys.argv[2] 
else:
    input_dir= "./tempdir"
    output_file= "./Darshan_Total.csv"
print("input_dir = ", input_dir, ", output_file = ", output_file)

headerCol = []
headerValue = []
fileHeader = open('./headerTotal.csv','r')
Lines = fileHeader.readlines()
for line in Lines:
    line = line[:-1]
    headerCol.append(line)
    headerValue.append('-1')
fileHeader.close()

file_total_input = open(input_dir+'/parsed_total.txt','r')
file_total_output = open(output_file,'a+')

file_count = open(input_dir+'/count.txt','r')
count = file_count.read()
file_count.close()
print(input_dir+'/count.txt, read count =',  count)
if int(count) == 0:
    Lines = fileHeader.readlines()
    row = ''
    for line in Lines:
        line = line[:-1]
        row = row + str(line) + ','
    row = row[:-1] + '\n'
    file_total_output.write(row)
    

LinesTotal = file_total_input.readlines()
row = ''
headList = ['POSIX','STDIO','MPIIO']

for line in LinesTotal:
    if line.startswith('# exe'):
        exe = str((line.partition("# exe: ")[2])[:-1]).replace(',',';')
        headerValue[headerCol.index("exe")] = str(exe)
    if line.startswith('# uid'):
        uid = str((line.partition("# uid: ")[2])[:-1])
        headerValue[headerCol.index("uid")] = str(uid)  
    if line.startswith('# jobid'):
        jobid = str((line.partition("# jobid: ")[2])[:-1])
        headerValue[headerCol.index("jobid")] = str(jobid)    
    if line.startswith('# darshan log version'):
        darshan_log_version = str((line.partition("# darshan log version: ")[2])[:-1])
        headerValue[headerCol.index("darshan_log_version")] = str(darshan_log_version)
    if line.startswith('# start_time:'):
        start_time = str((line.partition("# start_time: ")[2])[:-1])
        headerValue[headerCol.index('start_time')] = str(start_time)
    if line.startswith('# start_time_asci'):
        start_time_asci = str((line.partition("# start_time_asci: ")[2])[:-1])
        headerValue[headerCol.index('start_time_asci')] = str(start_time_asci)
    if line.startswith('# end_time:'):
        end_time = str((line.partition("# end_time: ")[2])[:-1])
        headerValue[headerCol.index('end_time')] = str(end_time)
    if line.startswith('# end_time_asci'):
        end_time_asci = str((line.partition("# end_time_asci: ")[2])[:-1])
        headerValue[headerCol.index('end_time_asci')] = str(end_time_asci)
    if line.startswith('# nprocs'):
        nprocs = str((line.partition("# nprocs: ")[2])[:-1])
        headerValue[headerCol.index('nprocs')] = str(nprocs)
