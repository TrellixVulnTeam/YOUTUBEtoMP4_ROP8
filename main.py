from pytube import YouTube

link = input("Enter link : ")
print("downloading.....")
YouTube(link).streams.first().download()
print("Video downloaded!")