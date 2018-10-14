import requests,bs4,sys,webbrowser
res=requests.get("https://nostarch.com")
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
'print(res.text[:250])'
p=soup.select('#author')
print(len(p))

p[1].getText()

if len(sys.argv)<1:
    print("Please input a search keyword through command line")
Keyword=str(sys.argv)
res=requests.get('http://google.co.in/search?q=' +  ''.join(Keyword))
print(res.raise_for_status())
soup=bs4.BeautifulSoup(res.text)
