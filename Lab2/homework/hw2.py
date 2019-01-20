from youtube_dl import YoutubeDL

# S1. Download a single youtube video:
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

# S2. Download multiple youtube videos:
dl = YoutubeDL()
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=e-ORhEE9VVg', 'https://www.youtube.com/watch?v=aJOTlE1K90k'])

# S3: Download audio
options = {
    "format": "bestaudio/audio",
}
dl = YoutubeDL(options)
dl.download(["https://www.youtube.com/watch?v=OZqyyY9h0B0"])

# S4. Search and then download the first video:
options ={
    "default_search": "ytsearch",
    "max_download":1,
}
dl =YoutubeDL(options)
dl.download(["Home Michael Buble"])

# S5. Search and then download the first audio
options = {
    "default_search": "ytsearch",
    "max_download":1,
}
dl = YoutubeDL(options)
dl.download(["Đừng hỏi em mỹ tâm"])