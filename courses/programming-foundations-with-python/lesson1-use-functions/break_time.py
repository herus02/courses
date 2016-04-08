import time
import webbrowser

print ("This program started on" + time.ctime())
for i in range(0, 3):
  time.sleep(5)
  webbrowser.open("https://www.youtube.com/watch?v=vl-v4Hj6CcU")