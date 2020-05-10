from pytube import YouTube

nnnnn = 'https://www.youtube.com/watch?v=HFPxuzPhT6k&list=PLWseNH7jVTv4znuzRgAGqxnn5CVmGRJ_j&index=2&t=0s'
YouTube(nnnnn).streams.first().download()