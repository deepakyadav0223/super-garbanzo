import datetime
import winsound

def Alaram(timeing):
    altt = str(datetime.datetime.now().strptime(timeing,"%I:%M:%p"))
    altt = altt[11:-3]
    h=altt[:2]
    h=int(h)
    m= altt[3:5]
    m=int(m)
    print(f"Alram Set Successfully for {timeing}")

    while True:
        if h==datetime.datetime.now().hour:
            if m==datetime.datetime.now().minute:
                print("alram is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif m<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    Alaram('1:26:AM')