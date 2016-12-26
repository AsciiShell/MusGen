from winsound import Beep
import time
class Music:
    stdTime = 2400
    root24 = 1.0293022366434920287823718007739
    root12 = 1.0594630943592952645618252949463

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
        base = 0
        if t[0] == '-':
            base = int(t[1])
        else:
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

