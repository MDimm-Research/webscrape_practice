#source: http://stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python
##################################### Method 1
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('https://github.com/login')

# View available forms
formcount=0
#for f in br.forms():
    #print f

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=0)
#print br.form['login']
# User credentials
br.form['login'] = 'miketestgit02'
br.form['password'] = 'qzfreetf59im'

# Login
br.submit()

print(br.open('https://github.com/settings/emails').read())
