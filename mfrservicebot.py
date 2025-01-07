import os,string
os.system('title,@cmfr Bot .')
os.system("mode 60,20")
def clear():
    os.system("clear || cls")
#---------------------------------------
def install(package):
    os.system(f"pip install {package}")
try:
    import requests
except ImportError:
    install('requests')
try:
    import colorama
    from colorama import Fore,Style
except ImportError:
    install('colorama')
try:
    import re
except ImportError:
    install('re')
try:
    import telebot
except ImportError:
    install('pyTelegramBotAPI')
try:
    import random
except ImportError:
    install('random')
try:
    import threading
except ImportError:
    install('threading')
try:
    import hashlib
except ImportError:
    install('hashlib')
clear()
import telebot,requests,threading,os,time,hashlib,random,string,uuid
from telebot import types
from time import sleep
from colorama import Style,Fore
from datetime import datetime
colorama.init()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
open(f"MembersID.txt","a")
token = open("stoken.txt","r").read()
adminid = open("sid.txt","r").read()
def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))
def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result
def RandomNum(n=5):
    letters = '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
class ServicesBot:
    def __init__(self,bot):
        self.bot = bot
        self.lock = threading.Lock()
        self.enough = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Cancel",callback_data="enough"))
        self.stop = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Stop",callback_data="stop"))
        self.AdminID = adminid
    def generate_DeviceId(self,ID):
        volatile_ID = "12345"
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]
    def generateUSER_AGENT(self):
        Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
        DPIs = [
            '480', '320', '640', '515', '120', '160', '240', '800'
        ]
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180
        DEVICE_SETTINTS = {
            'system': "Android",
            'Host': "Instagram",
            'manufacturer': f'{random.choice(Devices_menu)}',
            'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
            'android_version': random.randint(18, 25),
            'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
            "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
            'resolution': f'{randResolution}x{lowerResolution}',
            'randomL': f"{RandomString(6)}",
            'dpi': f"{random.choice(DPIs)}"
        }
        return '{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
            **DEVICE_SETTINTS)
    def run(self):
        @self.bot.message_handler(content_types=['text'])
        def Button(message):
            if str(message.chat.id) in [uid for uid in open('MembersID.txt','r').read().splitlines()] or str(message.chat.id) == self.AdminID:
                try:
                    if message.text == "/start" or message.text == "start":
                        if str(message.chat.id) == self.AdminID:
                            self.key = types.ReplyKeyboardMarkup(True).row('Session Info')
                            self.key.row('Reset','Remove Biography')
                            self.key.row('Accept Terms','Accept Dismiss')
                            self.key.row('Regex for user:pass','Regex for Session-iD')
                            self.key.row("Settings")
                            self.bot.send_message(message.chat.id,text=f"[mfr](https://www.instagram.com/cmfr)"+"* ServicesBot.*",parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=self.key)
                        else:
                            self.key = types.ReplyKeyboardMarkup(True).row('Session Info')
                            self.key.row('Reset','Remove Biography')
                            self.key.row('Accept Terms','Accept Dismiss')
                            self.key.row('Regex for user:pass','Regex for Session-iD')
                            self.bot.send_message(message.chat.id,text=f"*Welcome, Member to *"+"[cmfr](https://www.instagram.com/cmfr)"+"* ServicesBot.*",parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=self.key)
                    elif message.text == "Remove Biography":
                        sent = self.bot.send_message(message.chat.id,text="*Now, send Session-iD ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                        self.bot.register_next_step_handler(sent,self.RemoveBio)
                    elif message.text == "Session Info":
                        sent = self.bot.send_message(message.chat.id,text="*Now, send Session-iD ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                        self.bot.register_next_step_handler(sent,self.CheckSession,key="checkSession")
                    elif message.text == "Reset":
                        sent = self.bot.send_message(message.chat.id,text="*Now, send Email/User ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                        self.bot.register_next_step_handler(sent,self.Reset)
                    elif message.text == "Accept Terms":
                        sent = self.bot.send_message(message.chat.id,text="*Now, send Session-iD ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                        self.bot.register_next_step_handler(sent,self.Accept_Terms)
                    elif message.text == "Accept Dismiss":
                        sent = self.bot.send_message(message.chat.id,text="*Now, send Session-iD ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                        self.bot.register_next_step_handler(sent,self.CheckSession,key="Accept_Dismiss")
                    elif message.text == "Regex for user:pass":
                        sent = self.bot.send_message(message.chat.id, "send order.txt file to filter to user:pass.")
                        self.bot.register_next_step_handler(sent,self.set_input_for_regex, filename="Accounts-{0}.txt".format(RandomNum()), key="Regex for logins")
                    elif message.text == "Regex for Session-iD":
                        sent = self.bot.send_message(message.chat.id, "send order.txt file to filter to sessionid.")
                        self.bot.register_next_step_handler(sent, self.set_input_for_regex, filename="Sessions-{0}.txt".format(RandomNum()), key="Regex for sessionid")
                    elif message.text == "Add Member [ID]":
                        if str(message.chat.id) == self.AdminID:
                            sent = self.bot.send_message(message.chat.id,text="*Now, send iD ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                            self.bot.register_next_step_handler(sent,self.AddID)
                    elif message.text == "Broadcast":
                        if str(message.chat.id) == self.AdminID:
                            sent = self.bot.send_message(message.chat.id,text="*Now, send broadcast message ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                            self.bot.register_next_step_handler(sent,self.Broadcast)
                    elif message.text == "Remove Member [ID]":
                        if str(message.chat.id) == self.AdminID:
                            sent = self.bot.send_message(message.chat.id,text="*Now, send iD ?*",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=self.enough)
                            self.bot.register_next_step_handler(sent,self.RemoveID)
                    elif message.text == "Settings" and str(message.chat.id) == self.AdminID:
                        self.setting = types.ReplyKeyboardMarkup(True).row('Add Member [ID]','Remove Member [ID]')
                        self.setting.row('Broadcast')
                        self.setting.row('Back')
                        self.bot.send_message(message.chat.id,text=f"*[Admin] Settings :*",parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=self.setting)
                    elif message.text == "Back" and str(message.chat.id) == self.AdminID:
                        self.key = types.ReplyKeyboardMarkup(True).row('Session Info')
                        self.key.row('Reset','Remove Biography')
                        self.key.row('Accept Terms','Accept Dismiss')
                        self.key.row('Regex for user:pass','Regex for Session-iD')
                        self.key.row("Settings")
                        self.bot.send_message(message.chat.id,text=f"[mfr](https://www.instagram.com/cmfr)"+"* ServicesBot.*",parse_mode='markdown',reply_to_message_id=message.message_id,reply_markup=self.key)
                except Exception as e:
                    print(str(e))
                    edit = self.bot.send_message(message.chat.id,text=f"*Invalid Button .*",parse_mode='markdown',reply_to_message_id=message.message_id)
                    self.bot.edit_message_text('*choose a valid button ./start*',edit.chat.id,edit.message_id,parse_mode='markdown')
            else:
                self.bot.send_message(message.chat.id,text=f"*Plz dm if you want use it > *"+"[mfr](https://www.instagram.com/cmfr)"+f"*\nMembership iD : *"+f"`{message.chat.id}`",parse_mode='markdown',reply_to_message_id=message.message_id)
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback(call):
            global edit
            if call.data == "enough":
                self.bot.clear_step_handler_by_chat_id(call.message.chat.id)
                self.bot.send_message(call.message.chat.id,"*Entry has been cancelled .*",parse_mode="markdown",reply_to_message_id=call.message.message_id)
            
    def CheckSession(self,message, key=str):
        self.sid = message.text
        edit = self.bot.send_message(message.chat.id,text="*Checking Session-iD ... ♻️*",parse_mode="markdown",reply_to_message_id=message.message_id)
        
        self.current_user = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true',headers={'User-Agent': 'Instagram 275.0.0.27.98 Android', "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Connection': 'keep-alive'},cookies={'sessionid': self.sid})
        if "fbid_v2" in self.current_user.text and self.current_user.status_code == 200:
            self.username = self.current_user.json()["user"]["username"]
            self.bio = self.current_user.json()['user']['biography']
            self.name = self.current_user.json()['user']['full_name']
            self.email = self.current_user.json()['user']['email']
            self.phone = self.current_user.json()['user']['phone_number']
            self.trusted = self.current_user.json()['user']['trusted_username']
            self.bot.edit_message_text(f"*Done Login as @*"+f'[{self.username}](https://www.instagram.com/{self.username})'+"* .*",edit.chat.id,edit.message_id,parse_mode="markdown")
            if key == "Getinfo":
                return self.username,self.bio,self.name,self.email,self.phone
            elif key == "checkSession":
                # info = f'*Session is working*\n*Username:* @{self.username}\n*Name:* {self.name}\n*Email:* {self.email}\n*Phone Number:* {self.phone}\n*Bio:* {self.bio}'
                info = (
                        f"Session Info [Good]:\n"
                        f"Username: @{self.username}\n"
                        f"Trusted-User: @{self.trusted}\n"
                        f"Name: {self.name}\n"
                        f"Email: {self.email}\n"
                        f"Phone Number: {self.phone}\n"
                        f"Bio: {self.bio}"
                    )
                self.bot.send_message(message.chat.id,text=info)
        # i was here
        elif self.current_user.status_code == 400 and "challenge_required" in self.current_user.text and key == "Accept_Dismiss":
            challenge_url = self.current_user.json()['challenge']['url']
            if challenge_url == "https://i.instagram.com/challenge/?next=/api/v1/accounts/current_user/%253Fedit%253Dtrue":
                self.Accept_Dismiss(message, challenge_url)
            elif challenge_url == "https://www.instagram.com/accounts/suspended/":
                self.bot.edit_message_text(f"*Account is Suspended.*",edit.chat.id,edit.message_id,parse_mode="markdown")
        elif self.current_user.status_code == 403:
            self.bot.edit_message_text(f"*Session-iD is invalid .*",edit.chat.id,edit.message_id,parse_mode="markdown")
        else:
            self.bot.edit_message_text(f"*Session-iD is invalid .*",edit.chat.id,edit.message_id,parse_mode="markdown")
    def RemoveBio(self,message):
        self.sid = message.text
        edit = self.bot.send_message(message.chat.id,text="*Trying to change bio ... ♻️*",parse_mode="markdown",reply_to_message_id=message.message_id)
        username,bio,name,email,phone = self.CheckSession(message,"Getinfo")
        self.bot.send_message(message.chat.id,text=f"*Current Bio :* {bio}",parse_mode="markdown",reply_to_message_id=message.message_id)
        databio = {"biography":"","email":email,"first_name":name,"phone_number":phone,"username":username}
        self.removebio = requests.post("https://www.instagram.com/api/v1/web/accounts/edit/",headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0", "Content-Type": "application/x-www-form-urlencoded","X-Csrftoken": "v7R8E82W7nvN7bcie2JsrpSBqZOMjLEo","Cookie":f"sessionid={self.sid}"},data=databio)
        if self.removebio.json().get("status") == "ok":
            self.bot.edit_message_text(f"*Done removed biography .*",edit.chat.id,edit.message_id,parse_mode="markdown")
        else:
            self.bot.edit_message_text(f"*Fail removed biography .*",edit.chat.id,edit.message_id,parse_mode="markdown")
            with open(f"Logs-{message.chat.id}.txt","a") as file:
                file.write(f"RemoveBio >> {self.removebio.text}\n")
            self.bot.send_document(message.chat.id,open(f'Logs-{message.chat.id}.txt','rb'),reply_to_message_id=message.message_id)
    def Reset(self,message):
        self.username = message.text
        if "@" in self.username and '.' not in self.username:
            self.username = self.username.split('@')[1]
        edit = self.bot.send_message(message.chat.id,text="*Checking Email/User ... ♻️*",parse_mode="markdown",reply_to_message_id=message.message_id)
        self.send_password = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers={'Content-Length': '305','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'i.instagram.com','Connection': 'Keep-Alive','User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)','Accept-Language': 'en-US','X-IG-Connection-Type': 'WIFI','X-IG-Capabilities': 'AQ==','Accept-Encoding': 'gzip',},data={'ig_sig_key_version': '3','username':self.username})
        if '"status":"ok"' in self.send_password.text:
            msgjson = self.send_password.json()["toast_message"]
            self.bot.edit_message_text(msgjson,edit.chat.id,edit.message_id)
        elif "Page Not Found" in self.send_password.text:
            self.bot.edit_message_text(f"*User not found @{self.username} .*",edit.chat.id,edit.message_id,parse_mode="markdown")
        else:
            self.bot.edit_message_text('*"error_type":"rate_limit_error"*',edit.chat.id,edit.message_id,parse_mode="markdown")
    def Accept_Terms(self,message):
        self.sid = message.text
        edit = self.bot.send_message(message.chat.id,text="*Trying to accept terms ... ♻️*",parse_mode="markdown",reply_to_message_id=message.message_id)
        self.consent1 = requests.post("https://www.instagram.com/web/consent/update/",headers={'Accept':'*/*','x-csrftoken':'missing','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)','cookie':f'sessionid={self.sid}','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://www.instagram.com','referer':'https://www.instagram.com/terms/unblock/?next=/api/v1/web/fxcal/ig_sso_users/'},data='updates={"existing_user_intro_state":2}&current_screen_key=qp_intro').text
        self.consent2 = requests.post("https://www.instagram.com/web/consent/update/",headers={'Accept':'*/*','x-csrftoken':'missing','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)','cookie':f'sessionid={self.sid}','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://www.instagram.com','referer':'https://www.instagram.com/terms/unblock/?next=/api/v1/web/fxcal/ig_sso_users/'},data='updates={"tos_data_policy_consent_state":2}&current_screen_key=tos').text
        if '{"screen_key":"finished","status":"ok"}' in self.consent1 or '{"screen_key":"finished","status":"ok"}' in self.consent2:
            self.bot.edit_message_text(f"*Done accepted terms .*",edit.chat.id,edit.message_id,parse_mode="markdown")
        else:
            self.bot.edit_message_text(f"*Fail accepted terms .*",edit.chat.id,edit.message_id,parse_mode="markdown")

    def set_input_for_regex(self,message, filename=str, key=str):
        with open(filename, 'w') as file:
            file.write("")  # Clear the file contents

        if message.document:
            proxy = document(message)
            formatted_lines = []

            for line in proxy.splitlines():
                if key == "Regex for logins":
                    # Extract user:pass format
                    parts = line.split(":")
                    if len(parts) > 1:
                        user_pass = f"{parts[0]}:{parts[1].split('|')[0]}"
                        formatted_lines.append(user_pass)
                elif key == "Regex for sessionid":
                    # Perform cut -d "=" -f 5 | cut -d ";" -f 1
                    try:
                        sessionid_part = line.split("=")[4].split(";")[0]
                        formatted_lines.append(sessionid_part)
                    except IndexError:
                        continue

            # Write the formatted lines to the file
            with open(filename, 'a') as file:
                file.write("\n".join(formatted_lines) + "\n")
            with open(filename, 'rb') as file:
                self.bot.send_document(message.chat.id, file) 
        self.bot.send_message(message.chat.id,f"{key} Done.")
    def Accept_Dismiss(self,message,challenge_url):
        edit = self.bot.send_message(message.chat.id,text="*Trying to accept challenge ... ♻️*",parse_mode="markdown",reply_to_message_id=message.message_id)
        session_obj = requests.Session()
        headers = {
            "User-Agent": "Instagram 275.0.0.27.98 Android",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Csrftoken": "missing",
        }
        session_obj.headers.update(headers)
        session_obj.cookies.update({'sessionid': self.sid})
        session_obj.cookies.update({'csrftoken': 'WVZrkclCFKDTEalVUCOGoHBv7XIDdIu4'}) 
        s = accept_challenge(session_obj, challenge_url)
        if s == True:
            self.bot.edit_message_text(f"*Done accepted challenge .*",edit.chat.id,edit.message_id,parse_mode="markdown")
        else:
            self.bot.edit_message_text(f"*Fail accepted challenge . Reson: {s}*",edit.chat.id,edit.message_id,parse_mode="markdown")
    def AddID(self,message):
        self.id = message.text
        with open("MembersID.txt","a") as a:
            a.write(f"{self.id}\n")
        self.bot.send_message(message.chat.id,text="*Done Add New Member [ID] ✅*",parse_mode="markdown",reply_to_message_id=message.message_id)
    def RemoveID(self,message):
        self.id = message.text
        with open("MembersID.txt", "r+") as file:
            lines = file.readlines()
            filtered_lines = [line for line in lines if line != (self.id + "\n")]
            file.seek(0)
            file.truncate(0)
            file.writelines(filtered_lines)
        self.bot.send_message(message.chat.id,text="*Done Remove Member [ID] ✅*",parse_mode="markdown",reply_to_message_id=message.message_id)
    def Broadcast(self,message):
        self.msg = message.text
        edit = self.bot.send_message(message.chat.id,text="*[Broadcast] sending message ... ♻️*",parse_mode="markdown")
        for uid in open('MembersID.txt','r').read().splitlines():
            self.bot.send_message(uid,text=self.msg,parse_mode="markdown")
        self.bot.send_message(message.chat.id,text="*[Broadcast] Done sent message ✅*",parse_mode="markdown",reply_to_message_id=message.message_id)
def document(message: types.Message) -> str:
    if message.document.mime_type == 'text/plain':
        File = requests.get('https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, message.document.file_id)).json()['result']['file_path']
        inside_file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, File))
        return inside_file.text
    return 'bruh'


def accept_challenge(session_obj, challenge_url: str):
    headers = {
        'Host': 'i.instagram.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-Gpc': '1',
        'Priority': 'u=0, i',
        'Te': 'trailers'
    }

    response = session_obj.get(challenge_url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        with open("challenge.txt", "w") as f:
            f.write(response.text)
        
        with open('challenge.txt', 'r') as file:
            text = file.read()
        
        match = re.search(r'\\"([^\\"]+)\\"\, \(bk\.action\.i32\.Const, 0\)\)\)', text)
        if match:
            challenge_context = match.group(1)
            x= take_challenge(session_obj, challenge_context)
            return x
        else:
            return "No match found. // this is not challenge error"
    else:
        return f"Failed to get the challenge page. Status code: {response.status_code}"


def take_challenge(session_obj, challenge_context: str):
    post_url = "https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Bloks-Version-Id": "5d9af7318e9ff0ac69aa387c21c0913044bd3067683554a96c0024aa52262e82",
        "X-Csrftoken": "WVZrkclCFKDTEalVUCOGoHBv7XIDdIu4",
        "X-Instagram-Ajax": "143df0f9f635",
        "X-Ig-App-Id": "936619743392459",
        "X-Asbd-Id": "129477",
        "X-Ig-Www-Claim": "hmac.AR18BS6MZflRc4LCXZDTJF8bcvgoiaxIwYg94sxOivsnN_rt",
        "Origin": "https://i.instagram.com",
        "Referer": "https://i.instagram.com/challenge/?next=/api/v1/accounts/current_user/%253Fedit%253Dtrue"
    }

    payload = {
        "challenge_context": challenge_context,
        "has_follow_up_screens": "0",
        "nest_data_manifest": "true"
    }

    response = session_obj.post(post_url, data=payload, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return "Failed to take the challenge. Status code: {response.status_code}"

if __name__ == '__main__':
    bot = telebot.TeleBot(token)
    Run = ServicesBot(bot)
    Run.run()
    print(Style.BRIGHT + '< ' + Fore.LIGHTGREEN_EX + '$' + Fore.RESET + f' > Bot is Alive  {datetime.now()}')
    bot.infinity_polling()