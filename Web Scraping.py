'''import webbrowser,sys, pyperclip
#webbrowser.open("https://inventwithpython.com")

if len(sys.argv)>1:
    address=''.join(str(sys.argv[1:]))
else:
    address=pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)'''
#Downloading a Web Page with the requests.get() Function
import requests
res=requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))


print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

#Checking for Errors
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
print(res.raise_for_status())