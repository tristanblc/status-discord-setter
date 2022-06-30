from email import header
import requests
from urllib import request
import pip._vendor.requests as res
from xmlrpc.client import boolean
import emoji
import time
import random
import datetime 
import time
import json
import keyboard
from pathlib import Path

class Status: 
    def __init__(self,emoji,message):
        token = None
        env_path = Path(__file__).parent.parent / "json" / "app.json"
        print(env_path)
        with open(env_path ) as f:
            data = json.load(f)
            if data  == None or data == "":
                return None

            token = data["token"]
 

        self.autorize = {"authorization":   str(token) }
        self.requete = "https://discord.com/api/v9/users/@me/settings"
        if(emoji == None) :
             self.list_emoji = []
        else:
            self.list_emoji = emoji.split(',')
        if(message != None) :
            self.list_message = message.split(',')
            print(self.list_message)
        else :
            self.list_message = [""]
        self.message = message
        self.boolean = False

 
    def stopStatus(): 
        self.boolean = False

    def startStatus(self):
     i =0
     j = 0
     self.boolean = True
     while self.boolean: 
        if  keyboard.is_pressed('q'):  
            self.boolean = False
            break 
        else:
         
            if(i == len(self.list_emoji)):
                 i = 0
            
            if(j == len(self.list_message)):
                     j = 0

            text = set() 
            custom_status = { "custom_status" : {"text" : self.list_message[j], "emoji_name": self.list_emoji[i]}}
            requete =  requests.patch(self.requete, json = custom_status,headers=self.autorize)
            i = i+1 
            j = j+1
            time.sleep(4)           
           


