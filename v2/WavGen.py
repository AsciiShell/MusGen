import wave,random,struct,math,time
class Music:
    stdTime = 2400
    root12 = 1.059763074359
    root24 = 1.029302236643

    @staticmethod
    def getFrequency(s):
        d = 0
        sharpCount = s.count('#')
        flatCount = s.count('b')
        if sharpCount > 0 and flatCount == 0:
            d = sharpCount
        elif sharpCount ==0 and flatCount > 0:
            d = flatCount
        elif sharpCount > 0 and flatCount > 0:
            raise Exception('Tone cannot be flat and sharp at the same time')
        #X1 tone
        if s[0] == 'A':
            r =  55.0000
        elif s[0] == 'B':
            r = 61.7354
        elif s[0] == 'C':
            r = 32.7032
        elif s[0] == 'D':
            r = 36.7081
        elif s[0] == 'E':
            r = 41.2035
        elif s[0] == 'F':
            r = 43.6536
        elif s[0] == 'G':
            r = 48.9995
        #Transform to target tone
        #r *= 2 ** (int(s[1]) - 1)
        for i in s:
            if ord(i) in range(48,58):#from '0' to '9'
                r *= 2 ** (int(i) - 1)
                break
        #Sharp&Float
        r *= Music.root24 ** d
        return round(r)
    
    @staticmethod
    def getTime(t = 2):
        if len(str(t)) == 1:
            return 2 ** -int(t)
        base = -int(t[0])
        r = 2 ** base
        for i in range(len(t) - 1):
            base -= 1
            r += 2 ** base
        return r
            
    @staticmethod        
    def playTone(tone, duration):
        if tone == 0 or tone == '0':
            time.sleep(round(Music.getTime(duration) * Music.stdTime)/1000)
            return
        Beep(Music.getFrequency(tone), round(Music.getTime(duration) * Music.stdTime))


noise_output = wave.open('noise2.wav', 'w')
#Normal 2 2 for stereo
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

values = []

for i in range(0, 44100*2):
        #value = random.randint(-30000, 32000)

        #d1 = round(math.sin(220* 2*i*math.pi/(44100))*32000)
        d2 = round(
            (math.sin(440 * 2*i*math.pi/(44100))*10 +
             math.sin(880 * 2*i*math.pi/(44100))*7 +
             math.sin(1760 * 2*i*math.pi/(44100))*4 +
             math.sin(3520 * 2*i*math.pi/(44100)) +
             math.sin(220 * 2*i*math.pi/(44100)) +
             math.sin(660 * 2*i*math.pi/(44100)) +
             math.sin(330 * 2*i*math.pi/(44100)) +
             math.sin(100 * 2*i*math.pi/(44100)) +
             math.sin(200 * 2*i*math.pi/(44100))
             )*32000/27)
        #packed_value = struct.pack('h',d1)
        pv2 = struct.pack('h',d2)
        values.append(pv2)
        values.append(pv2)

value_str = values[0]
for i in range(len(values)):
        value_str += values[i]
noise_output.writeframes(value_str)

noise_output.close()
