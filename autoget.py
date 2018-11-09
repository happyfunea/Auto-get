#!/usr/bin/python
#-*-coding:utf-8-*-
'''Ngapain Coy?
Mau Liat Source?
'''
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan


import urllib,requests,os,sys,json,subprocess as a,time
def generate():
    try:
        id = raw_input("enter your id or number_phone : ")
        pwd = raw_input("enter your password : ")
        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" 
        + id + "&locale=en_US&password=" + pwd + 
        "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        operan = json.load(data)
        x = open("token.log", "w")
        x.write(operan["access_token"])
        x.close()
        kontol = open("token.log", "r").read()
        parsing = urllib.urlopen("https://graph.facebook.com/me?access_token=" + kontol)
        ok = json.load(parsing)
        nama = ok["name"]
        id = ok["id"]
        print "[+] By _[@]9un9_"
        print R+"[+]"+N+" Successfully Generate Access_Token :"+G,operan["access_token"]
        print R+"[=] "+N+"Your Account :"+G,nama
        print R+"[=] "+N+"Your Id:"+G, id
        print
        print R+"[=]"+N+'your access token save in token.log'
        pass
    except:
        print "Please!!!!!"
    lol = raw_input('Press enter for back to menu...')


        	
        	
def getid():
    try:
        usr = raw_input('Masukkan Your Token: ')
        op = open(usr, 'r').read()
    except:
        print R+'Please Generate access token...'+G+'!!!'
        sys.exit()
    try:
        url = urllib.urlopen('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token='+op)
        parsing = json.load(url)
        new = open('idteman.log','w')
        for c in parsing['friends']['data']:
            url2 = urllib.urlopen('https://graph.facebook.com/'+c['id']+'/subscribers?access_token='+op)
            pusing = json.load(url2)
            new.write(c["id"]+'\n')
            print R+"[=]"+G+"===="+N+"[>]"+G, c['name']
            print N+"Get Id Success!|"+G, c['id']+'\033[0m |'
            print N+"_______________________________"
        new.close()
    except KeyboardInterrupt:
        print R+'[*]'+G+'Id Save In Idteman.log'
        print R+'Exiting!'
        sys.exit()


def getemail():
    try:
        usr = raw_input('Masukkan Token Mu: ')
        op = open(usr, 'r').read()
        url = urllib.urlopen('https://graph.facebook.com/me/friends?access_token='+op)
        parsing = json.load(url)
        file = open('email.log', 'w'+'\n')
        for i in parsing['data']:
            url2 = urllib.urlopen('https://graph.facebook.com/'+i['id']+'?access_token='+op)
            pusing = json.load(url2)
            try:
                print N+"_______________________________"
                print R+'[=]'+G+'Success!!'+N+' --->\033[1;32m'+pusing['email']+'\n'+N+'Done!!'
                file.write(pusing['email']+'\n')
            except:
           	try:
           		print R+'[!]'+N+'Failed!! --->'+pusing['name']
           	except:
           		print R+'Filed!!'+pusing['name']
        file.close()
    except KeyboardInterrupt:
    	print R+'Exiting'+N+'!!!'
    	print N+'[*]'+G+'Email Save In email.log'
        sys.exit()
				
				

def show_menu():
	title = C+'SMPL BOT'+G
	print G+'------------info------------'
	print R+'[*]'+N+' Title: Simple Bot'
	print R+'[*]'+N+' Author: Agung'
        print R+'[*]'+N+' CodeName: mr-[@9un9]'
	print G+'''----------------------------
+                          +
+\t %s          +'''% title
	print G+'____________________________'
	print R+'[√]'+G+'~'+N+'1 Generate Access Token'
	print R+'[√]'+G+'~'+N+'2 Get Id Friends'
	print R+'[√]'+G+'~'+N+'3 Get Email Friends'
        print R+'[√]'+G+'~'+N+'0 Exit'
	us = raw_input('Pilih: ')
	if us == '1':
		generate()
	elif us == '2':
		getid()
	elif us== '3':
		getemail()
	elif us== '0':
		print R+'[!]'+N+'Exiting!!'
		sys.exit()
	else:
		print G+'Your Stupid?'
		raw_input(R+'Press Enter...')
if __name__=='__main__':
	while True:
                a.call('clear', shell=True)
		show_menu()
