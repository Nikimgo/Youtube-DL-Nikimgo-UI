import eel
from ytdl import Ytdl
from io import StringIO 
import os

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
    
    settings = {'directory':None}
    
    try:
        
        with open('settings', 'r') as file:
            
            for line in file:
                
                line = line.strip().split()
                
                settings[line[0]] = line[1]
    except FileNotFoundError:
        
        print('settings file doesn\'t exist');
    finally:
        
        with open('settings', 'w') as file:
            
            settings[setting] = value
            
            for key in settings:
                
                file.write(f'{key} {settings[key]}')
                
        
    
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
        ytdl.download_video()
    except:
        eel.logs_from_python('Error: Something went wrong, check if all required options are set and try again')

eel.init('web')
eel.start('html\\index.html', size=(1200, 700))