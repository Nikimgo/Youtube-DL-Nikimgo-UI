import youtube_dl

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
        
def my_hook(d):
    if d['status'] == 'downloading':
        pass
    elif d['status'] == 'finished':
        print('Downloading finished!')
        
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'F:\Programy\Youtube-DLG-Downloads\%(title)s.%(ext)s',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

class Ytdl:
    
    def __init__(self):
        
        self.link = None
        self.extension = 'bestvideo+bestaudio/best' #webm or 18 or best
        #self.directory = 'F:\Programy\Youtube-DLG-Downloads'
        self.ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'ignoreerrors': True,
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        
    def change_option(self, option, value):
        
        match option:
            case 'format':
                self.ydl_opts['format'] = value
                print(f'changed format to {value}')
            case 'output':
                self.ydl_opts['outtmpl'] = f'{value}\%(title)s.%(ext)s'
                print(f'changed output to {value}')
            case 'logger':
                self.ydl_opts['logger'] = value
                print(f'changed logger to {value}')
                
    def download_video(self, link):
        
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([link])
        
        