import sdf
import os, sys
print('#########################################################################')
print('#      This python script helps to read sdf file content                #')
print('#        Version 1.1  Proudly Presented by Haotian Mao                  #')
print('#########################################################################')
dirs = os.listdir('./')
filename = 'No sdf file Detected'
prefix = raw_input('\nPlease type in sdf file prefix (Default none):')
no = input('\nEnter the sdf file number you want: ')
for file in dirs:
    if (file[0:len(prefix)] == prefix)&(file[-8:] == str(no).zfill(4)+'.sdf'):
        filename = file
print('Reading file : ' + filename)
Item = ['Density', 'Px', 'Py', 'Pz', 'Ex','Ey', 'Ez','Bx','By','Bz','ID']
#print('Please enter file prefix (type N/A if not applicable)')
#filename=input('FIle Prefix: ')
#if filename == 'N/A' or 'n/a':
#   filename = ''
if filename == 'No sdf file Detected':
    print('Reading failed. Desired sdf file not detected. Please Check again.')
else:
    print('Reading Completed. ')
#print('Please enter file prefix (type N/A if not applicable)'):
a= sdf.read(filename, dict=True)
menu ='\n0.Exit   1.Density   2.Px     3.Py    4.Pz     5.Ex    6.Ey    7.Ez\n8.Bx     9.By        10.Bz    11.ID   12.Search'
print(menu)
num = input('What you want to see: ')
while num != 0:
    if num == len(Item)+1:
        print('\nHere\'s everything in sdf file:\n')
        liststr = a.keys()
        liststr.sort()
        print "\n".join(liststr)
        print(menu)
        num = input('\nWhat you want to see : ')
    elif num == len(Item)+2:
        search = raw_input('Please enter the item you want: ')
        print('\nHere\'s everything regarding \'' + search + '\' in sdf file:\n')
        print "\n".join([s for s in a.keys() if search in s])
        print(menu)
        num = input('\nWhat you want to see : ')
    elif num == 0:
        print('Searching Script Exit.')
        exit()
    else:
        print('\nHere\'s everything regarding \'' + Item[num-1] + '\' in sdf file:\n')
        print "\n".join([s for s in a.keys() if Item[num -1] in s])
        print(menu)
        num = input('What you want to see :')
