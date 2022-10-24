#LocateForWindows V 0.1
#Made by Shdaowclone
#Link https://github.com/shdaowclone/LocateForWindows

import sqlite3
import os
from sys import argv

def fill_table():
    master_db = sqlite3.connect(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows\\Masterdb.db')
    nave = master_db.cursor()
    drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
    Errors = 0
    for partation in drives:
        try:
            dir_content = os.listdir(partation+'\\')      
            for ffile in dir_content:
                if os.path.isfile(partation+'\\'+ffile):
                    try:
                        nave.execute('insert into Files (file) values(\''+partation+'\\'+ffile+'\')')
                    except:
                        pass
                else:
                    drives.append(partation+'\\'+ffile)
        except:
            Errors += 1
    master_db.commit()
    master_db.close()
    print("[!] Number of Folders that weren't accessable: "+str(Errors))
    return

def create_master_table():
    master_db = sqlite3.connect(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows\\Masterdb.db')
    nave = master_db.cursor()
    nave.execute('create table Files (id INTEGER PRIMARY KEY AUTOINCREMENT, file TEXT NOT NULL UNIQUE)')
    master_db.close()
    print("[+] Updating Table!")
    fill_table()
    return

def check_db():
    if os.path.isdir(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows') == False:
        print('[+] First Time execution')
        print('[+] Creating Database at: '+os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows')
        os.mkdir(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows')
        create_master_table()
    elif os.path.isfile(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows\\Masterdb.db') == False:
        print('[!] Coudn\'t Find the Database!')
        print('[+] Creating New Database at: '+os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows')
        create_master_table()
    return

def search(sfile):
    master_db = sqlite3.connect(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows\\Masterdb.db')
    nave = master_db.cursor()
    result = nave.execute('select file from Files where file like ?', ('%'+sfile+'%',)).fetchall()
    if len(result) == 0:
        return None
    else:
        return result

def main():
    check_db()
    if len(argv) == 1:
        print('[!] Usage: '+argv[0].split('\\')[-1]+' name_of_file')
        print('\n-refill_database  -----  to update the database with new files\n')
        os.close(0)
    else:
        if argv[1] == "-refill_database":
            os.remove(os.getenv('userprofile')+'\\appdata\\roaming\\LocateForWindows\\Masterdb.db')
            create_master_table()
        else:
            sfile = argv[1].replace('#','').replace(';','').replace('"','').replace('|','')
            try:
                res = search(sfile)
                if res == None:
                    os.close(0)
                else:
                    for r in res:
                        print(r[0])
            except:
                print("[!] Search Cancled!")
                os.close(0)

if __name__ == '__main__':
    main()
