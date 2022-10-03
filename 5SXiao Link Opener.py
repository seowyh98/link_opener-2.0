import time
import webbrowser
from datetime import datetime

bc = "https://meet.google.com/oeq-ypna-eus"
bcLink = "https://forms.gle/tssNbakPWbZBh3TeA"
bi = "https://us04web.zoom.us/j/73105043881?pwd=bmp6YmE1S0VvVGRLVVZ5M3ArTjVwUT09"
bm = "https://meet.google.com/lookup/d663sqcy5f?authuser=1&hs=179"
addmath = "https://meet.google.com/lookup/fhsefgv6cn?authuser=1&hs=179"
calculus = "https://meet.google.com/lookup/h4rhaagn4f?authuser=1&hs=179"
modernmath = "https://meet.google.com/lookup/enb4tfcfnb?authuser=1&hs=179"
phy = "https://meet.google.com/lookup/er3addd22s?authuser=1&hs=179"
che = "https://meet.google.com/lookup/fiphko2zxt?authuser=1&hs=179"
bio = "https://us04web.zoom.us/j/9627723604?pwd=UnY5cWtaZjh2RG9samlLbFRaRzZVdz09"
pe = "https://meet.google.com/lookup/hp5qq3nqiu?authuser=1&hs=179"
music = "https://zoom.us/j/3022894614?pwd=SVRJN2p5Z3RFclMrWUczSkwybHdSQT09"
moral = "https://zoom.us/j/6196952665?pwd=d2M5dlJpTTVjeVk5S203VGliVU13UT09"
sej = "https://meet.google.com/lookup/ge4afvfepp?authuser=1&hs=179"
lmh = "https://us02web.zoom.us/j/5826591153?pwd=NTB1em1yNWNLOGJuRVo0OWZ5Zngwdz09"
extra = "https://hku.zoom.us/j/92359497523?pwd=OEJlWjd4VDFYUnNkMGM5Y0l2N0U2QT09"
while True:
    day = datetime.now().strftime("%a")
    lcltime = datetime.now().strftime("%H%M%S")

    if day == "Mon":
        if lcltime == "074800":
            webbrowser.open(calculus)
        if lcltime == "082500":
            webbrowser.open(bi)
        if lcltime == "090500":
            webbrowser.open(bm)
        if lcltime == "100000":
            webbrowser.open(che)
        if lcltime == "112000":
            webbrowser.open(moral)
        if lcltime == "120000":
            webbrowser.open(calculus)
        if lcltime == "130500":
            webbrowser.open(bio)
        if lcltime == "134500":
            webbrowser.open(modernmath)
        if lcltime == "142500":
            webbrowser.open(bc)
            webbrowser.open(bcLink)
        if lcltime == "150000":
            webbrowser.open(extra)
        if lcltime == "162500":
            webbrowser.open(lmh)
            break
        else:
            time.sleep(1)

    if day == "Tue":
        if lcltime == "074800":
            webbrowser.open(bi)
        if lcltime == "082500":
            webbrowser.open(bm)
        if lcltime == "090500":
            webbrowser.open(music)
        if lcltime == "100000":
            webbrowser.open(bc)
            webbrowser.open(bcLink)
        if lcltime == "104000":
            webbrowser.open(bi)
        if lcltime == "112000":
            webbrowser.open(modernmath)
        if lcltime == "120000":
            webbrowser.open(sej)
        if lcltime == "130500":
            webbrowser.open(moral)
        if lcltime == "134500":
            webbrowser.open(bm)
        if lcltime == "142500":
            webbrowser.open(addmath)
            break
        else:
            time.sleep(1)

    if day == "Wed":
        if lcltime == "082500":
            webbrowser.open(phy)
        if lcltime == "100000":
            webbrowser.open(calculus)
        if lcltime == "104000":
            webbrowser.open(bc)
            webbrowser.open(bcLink)
        if lcltime == "120000":
            webbrowser.open(bm)
        if lcltime == "130500":
            webbrowser.open(bi) 
        if lcltime == "134500":
            webbrowser.open(addmath)
        if lcltime == "142500":
            webbrowser.open(che)
            break
        else:
            time.sleep(1)

    if day == "Thu":
        if lcltime == "074800":
            webbrowser.open(bm)
        if lcltime == "082500":
            webbrowser.open(bc)
            webbrowser.open(bcLink)
        if lcltime == "090500":
            webbrowser.open(addmath)
        if lcltime == "100000":
            webbrowser.open(calculus)
        if lcltime == "104200":
            webbrowser.open(bio)
        if lcltime == "112000":
            webbrowser.open(phy)
        if lcltime == "120000":
            webbrowser.open(bi)
        if lcltime == "130500":
            webbrowser.open(bio)
        if lcltime == "134500":
            webbrowser.open(che)
        if lcltime == "142500":
            webbrowser.open(moral)
            break
        else:
            time.sleep(1)

    if day == "Fri":
        if lcltime == "074800":
            webbrowser.open(sej)
        if lcltime == "082500":
            webbrowser.open(phy)
        if lcltime == "090500":
            webbrowser.open(calculus)
        if lcltime == "100000":
            webbrowser.open(bi)
        if lcltime == "104000":
            webbrowser.open(bi)
        if lcltime == "112000":
            webbrowser.open(bc)
            webbrowser.open(bcLink)
        if lcltime == "120000":
            webbrowser.open(pe)
        if lcltime == "130500":
            webbrowser.open(bio)
        if lcltime == "134500":
            webbrowser.open(bm)
            break   
        else:
            time.sleep(1)

    if day == "Sat":
        if lcltime == "082500":
            webbrowser.open(phy)
        if lcltime == "090500":
            webbrowser.open(bm)
        if lcltime == "100000":
            webbrowser.open(bc)
            webbrowser.open(bcLink)
        if lcltime == "104000":
            webbrowser.open(addmath)
        if lcltime == "112000":
            webbrowser.open(bi)
        if lcltime == "120000":
            webbrowser.open(sej)
        if lcltime == "130500":
            webbrowser.open(bio)
            break
        else:
            time.sleep(1)
