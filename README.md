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

  main(host, port, url)
```
