from yt_dlp import YoutubeDL


(C1,C2,C3) = ("https://youtu.be","https://www.youtube.com","https://youtube.com")

option = dict(format="22")

link = input("Enter Youtube Video Url:>")

if C1 in link or C2 in link or C3 in link:
    with YoutubeDL(option) as YTD:
    
        YTD.download([link])
    print("\n[+] Downloaded ...")
else:
    print("[!] Invalid Video Url\n")








