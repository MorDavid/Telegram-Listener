import argparse
import time
import datetime
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument("-a","--api-key",dest="api_key",type=str,required=True,help="For Example: 1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ")
parser.add_argument("-s","--sleep",dest="time_sleep",type=int,required=True,help="Seconds")
parser.add_argument("-o","--output",dest="output_filename",type=str,required=True,help="You know.. Output file...")
args = parser.parse_args()

print('''
___ ____ _    ____ ____ ____ ____ _  _    ____ ____ ____ _ _  _ ____ ____ 
 |  |___ |    |___ | __ |__/ |__| |\/|    |__/ |___ |    | |  | |___ |__/ 
 |  |___ |___ |___ |__] |  \ |  | |  |    |  \ |___ |___ |  \/  |___ |  \ 
                                                        by Mor David - V1
''')

if(args.api_key):
    print("[+] API Key: "+args.api_key)
if(args.time_sleep):
    print("[+] Timesleep: "+str(args.time_sleep)+" seconds")
if(args.output_filename):
    print("[+] Output Filename: "+args.output_filename)
    if not os.path.exists(args.output_filename):
        current_datetime = datetime.datetime.now()
        with open(args.output_filename, 'w') as file:
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            file.write("[+] Telegram Listener by Mor David\n")
            file.write("[+] Start time: "+formatted_datetime+"\n")
while 1==1:
    url = "https://api.telegram.org/bot" + args.api_key + "/getUpdates"
    r = requests.get(url=url)
    data = r.json()
    for line in data["result"]:
        line = str(line)
        f = open(args.output_filename, "r")
        if line not in f.read():
            z = open(args.output_filename, "a")
            print(line)
            try:
                z.write(line+"\n")
            except :
                print(line)
            z.close()
        f.close()
    time.sleep(int(args.time_sleep))