# Magic regex
```
(?<=(.))(?!\1)
```

# Python

> hakerrank
```
def decor(fun):
  def wrapper(par):
    print("Decorated ", end="")
    return fun(par)
  return wrapper

def printSqr(x):
  print(x * x)

printSqr = decor(printSqr)
printSqr(9)     # returens "Decorated 81"
```

# Book  
> #convert number 12 into 8-digit binary  
> format(12, "08b")  
>
> #

# Flask  
 -- to make docker deamon working on M1:  
> $ softwareupdate --install-rosetta  
  
-- to make Flask working  
https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web->  
https://medium.com/fintechexplained/running-python-in-docker-container-58cda72>  
  
> $ export FLASK_APP=app  // this is just name, can be different  
$ export FLASK_ENV=development  // not sure if needed  
$ export FLASK_RUN_PORT=8800  
  
> $ flask run --port 8765 --debug  // inside app.py folder  

# BeautifulSoup
```
import requests
from bs4 import BeautifulSoup

def fetch_quote():
    response = requests.get('http://quotes.toscrape.com/random')
    soup = BeautifulSoup(response.text)
    quote_element = soup.find(class_='quote')
    author  = quote_element.find(class_='author').get_text()
    text = quote_element.find(class_='text').get_text()\
                        .replace('“', '').replace('”', '')
    return { 'author': author, 'text': text }
```
  
# HTTP
```
import http.client
import sys

def main(host, port, url):

  conn = http.client.HTTPConnection(host, port)
  conn.request("HEAD", url)
  response = conn.getresponse()

  print("Http response code:", response.status)
  print("web server banner:", response.getheader('Server'))
  print("ALL: ", response)

if __name__ == '__main__':
  host = sys.argv[1]
  port = sys.argv[2]
  url = sys.argv[3]
```
# RHEL
```
$ yum install -y yum-utils
$ yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
$
$ yum install iputils procps net-tools pip tree netcat crontab jq
```
  
# pcap  
Get files from S3 (local name test2.txt required)  
```
aws s3 cp s3://mybucket/test.pcap test2.pcap
```
    
# JavaScript, self invoking function definition  
```
(function diy(x){setTimeout(diy, 1000, x+1); console.log("counting: ", x)})(1)
```
(function definition in parenasis + argument)  
- or -
```
function diy(){setTimeout(diy, 1000); console.log(Date.now())}
diy()
```

  main(host, port, url)
```
