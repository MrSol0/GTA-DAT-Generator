import os
path = 'C:\Program Files\GTA San Andreas\data\maps'
DATA = open("GTA.DAT","w")
Files = os.listdir(path)
IDEFiles = []
IPLFiles = []

for file in Files:
    if '.' in file:
        if '.ipl' in file.lower():
            IPLFiles.append(path+'\\'+file)
        elif '.ide' in file.lower():
            IDEFiles.append(path + '\\' + file)
    else:
        nsub = path+'\\'+file
        sub = os.listdir(nsub)
        for file in sub:
            if '.' in file:
                if '.ipl' in file.lower():
                    IPLFiles.append(nsub + '\\' + file)
                elif '.ide' in file.lower():
                    IDEFiles.append(nsub + '\\' + file)
            else:
                nsub1 = nsub + '\\' + file
                sub = os.listdir(nsub1)
                for file in sub:
                    if '.' in file:
                        if '.ipl' in file.lower():
                            IPLFiles.append(nsub1 + '\\' + file)
                        elif '.ide' in file.lower():
                            IDEFiles.append(nsub1 + '\\' + file)


for ide in IDEFiles:
    nide = ide[ide.lower().find('data\\maps\\'):]
    DATA.write('IDE '+nide+'\n')

DATA.write('\n')

for ipl in IPLFiles:
    nipl = ipl[ipl.lower().find('data\\maps\\'):]
    DATA.write('IPL '+nipl+'\n')
