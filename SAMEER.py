import os,platform,time
print('Join My Facebook GROUP ');time.sleep(0.5)
os.system('xdg-open https://www.facebook.com/groups/147435904593672/?ref=share ')
print('\n\x1b[1;37m[●] Checking Update....✔️✔️');time.sleep(0.5)
os.system('git pull')

SAMEER=platform.architecture()[0]
if SAMEER=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif SAMEER=="64bit":
    __import__("run")
