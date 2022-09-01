import eel
from ytdl import Ytdl
from io import StringIO 
import os
import json

'''
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
'''
class MyLogger(object):
    def debug(self, msg):
        print(msg)
        eel.logs_from_python(msg)

    def warning(self, msg):
        print(msg)
        eel.logs_from_python(msg)

    def error(self, msg):
        print(msg)
        eel.logs_from_python(msg)        

ytdl = Ytdl()
debugging = 1

@eel.expose
def send_hello():
    print('Hello, world')
    
@eel.expose
def save_prefs(setting, value):
    
    match setting:
        
        case 'directory':
            
            if os.path.isdir(value) == False: return 0
    
    settings = {}
    
    try:
        
        with open('settings.json', 'r') as file:
            
            settings = json.load(file)
            print(f'settings loaded: {settings}')
    except FileNotFoundError:
        
        print('settings file doesn\'t exist');
    finally:
        
        settings[setting] = value
        print(f'settings saved: {settings}')
        
        with open('settings.json', 'w') as file:
            
            json.dump(settings, file)
                
@eel.expose
def load_prefs():
    
    try:
        
        with open('settings.json', 'r') as file:
            
            settings = json.load(file)
            print(f'settings loaded: {settings}')
            
            return settings
    except FileNotFoundError:
        
        print('settings file doesn\'t exist');
        return 0
    
@eel.expose
def change_link(link):
    
    ytdl.link = link
    return ytdl.link
    
@eel.expose
def change_option(option, value):
    
    ytdl.change_option(option, value)
    
@eel.expose
def change_directory(directory):
    
    if os.path.isdir(directory) == False: return 0
    ytdl.change_option('output', directory)
    
    return 1

@eel.expose
def download_video():
    
    #eel.logs_from_python('Hejka')
    eel.logs_from_python('Trying to execute download function')
    
    '''
    with Capturing() as output:
        
        try:
            ytdl.change_option('output', 'F:\Programy\Youtube-DLG-Downloads')
            ytdl.download_video(link)
        except:
            print('something went wrong')
        
    print(output)
    '''
    #ytdl.change_option('output', 'F:\Programy\Youtube-DLG-Downloads')
    try:
        ytdl.change_option('logger', MyLogger())
        
        for link in ytdl.link:
            
            eel.logs_from_python(f'\nLink: {link}')
            ytdl.download_video(link)
    except:
        eel.logs_from_python('Error: Something went wrong, check if all required options are set and try again')

eel.init('web')
eel.start('html\\index.html', size=(900, 600))