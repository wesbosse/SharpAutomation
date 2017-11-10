import mechanize
import cookielib
import scipy
import urllib2
import time

#initialize mechanize and cookie jar
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()

br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_redirect(mechanize.HTTPRedirectHandler)

#open press ganey portal
br.open('https://identity.pressganey.com/')
print(br.title())

#select log-in form and fill with credentials
br.form = list(br.forms())[0]
email = br.form.find_control("Email")
email.value = 'colleen.bosse@sharp.com'
password = br.form.find_control("Password")
password.value = '#Reports4me'

#submit login and wait for response
req = br.submit()
time.sleep(2)
print(req.read())

#PG 'noscript' handling
br.form = list(br.forms())[0]
requestURL = br.form.action
request = mechanize.Request(requestURL)
try:
    response = mechanize.urlopen(request)
except urllib2.HTTPError as e:
    print(e.read())


print(response.read())
#navigate to the reports

#select report

#fill in report specifics

#download report

#open report file

#export data

