import os

from ytdl import Ytdl

ytdl = Ytdl()

# https://www.youtube.com/watch?v=Hsg1LRkzru0 | do you know kids how fast
# https://www.youtube.com/watch?v=5izMdVdZJ8M | 4k demon slayer
# https://www.youtube.com/watch?v=6XC76oKLZpw | JoJo Stands Lore
# https://www.youtube.com/watch?v=kt0bfw4YkFk | TODO: Write Good Code Comments #Shorts
# https://www.youtube.com/watch?v=X2Wn-sJx56g | short: He filmed the president of Austria and made him laugh tiktok by niklaskima

#ytdl.change_option('format', 'bestaudio')
ytdl.change_option('output', 'F:\Programy\Youtube-DLG-Downloads')

ytdl.download_video('https://www.youtube.com/watch?v=5izMdVdZJ8M')