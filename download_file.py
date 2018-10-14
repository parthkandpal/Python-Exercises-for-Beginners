from urllib import request
file_url= "https://www.google.co.in/robots.txt"

def download_file(url):
    response= request.urlopen(url)
    file = str(response.read())
    lines = file.split("\\n")
    file_destination = r'robots.txt'
    fx = open(file_destination, 'w')

    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_file(file_url)