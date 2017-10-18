import urllib2

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
html = response.read()
line = len(html.splitlines())
print('*'*20,"Questions",'*'*20)
print('Total requests made in log:',line)

    