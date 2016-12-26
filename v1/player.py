from Music import Music
file = open('Полет шмеля.k2tf','r')
for line in file:
    if line == '\n':
        continue
    data = line.split()
    if data[0].lower() == 'speed':
        t = data[1].split('/')
        Music.stdTime = 60 * 1000 * 2**int(t[0])/ int(t[1])
    else:
        Music.playTone(data[0],data[1])
