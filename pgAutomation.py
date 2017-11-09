import mechanize
import scipy

#initialize mechanize
br = mechanize.Browser()

#open press ganey portal
br.open('https://identity.pressganey.com/')
print(br.title())

#select log-in form and fill with credentials
br.form = list(br.forms())[0]
email = br.form.find_control("Email")
email.value = 'colleen.bosse@sharp.com'
password = br.form.find_control("Password")
password.value = 'colleen.bosse@sharp.com'

#submit login
req = br.submit()
print(br)

#navigate to the reports

#select report

#fill in report specifics

#download report

#open report file

#export data

