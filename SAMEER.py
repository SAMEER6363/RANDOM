import os,platform,time
print('\n\x1b[1;37m[●] Checking Update....✔️✔️');time.sleep(0.5)
os.system('git pull')

SAMEER=platform.architecture()[0]
if SAMEER=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif SAMEER=="64bit":
    __import__("run")
