from bs4 import BeautifulSoup
import requests
import re
import os


def load_LMS(linksfile):
    with open(linksfile) as fin:
        vol = []

        s = ""
        for line in fin:
            if "Volume" in line:
                if s != "":
                    vol.append(s)
                s = ""
            s += line
        vol.append(s)
        
        for v in vol:
            volregx = re.search("Volume (\d+)", v)
            volNum = volregx.group().replace("Volume ", "")
            # print(volNum)
            soup = BeautifulSoup(v)

            
            baseDir = f"./raw_htmls/V{volNum}/"
            if not os.path.exists(baseDir):
                os.makedirs(baseDir)
            
            ch = 1
            for a in soup.find_all('a', href=True):
                partregx = re.search("part ?(\d+)", str(a.contents))
                if partregx is None:
                    filePath = baseDir+f"V{volNum}C{ch}.html"
                    ch += 1
                else:
                    partnum = partregx.group().replace("part", "").strip()
                    if partnum=="1":
                        ch += 1

                    filePath = baseDir+f"V{volNum}C{ch-1}P{partnum}.html"
                # print(filePath)
                fo = open(filePath, "w", encoding="utf-8")
                r = requests.get(a["href"])
                if r.status_code !=200:
                    print("ERROR", a.contents, a["href"])
                
                fo.write(r.text)
                fo.close()
                print(f"C{ch} {a.contents} DONE")
                
                
            print("Total", ch-1)
            
# load_LMS("v1-20.html")
# load_LMS("v21-27.html")
# load_LMS("v28-48.html")
# load_LMS("v49-58.html")