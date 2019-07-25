import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Shorcut for help you')
print(b+'\t    Lil_Dwagz')
print('\t https://Instagram/lil_dwagz')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] membuat termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Membuat setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Berhasil !')
sleep(1)
print(b+'\n[!] Setting up..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully !! ^^'+c+'\n\nhubungi https://Instagram/lil_dwagz untuk requests\natau pertanyaan Thanks :*\n\n')


# ini cuma shortcut buat bantu para nub
# karjok pangesty
