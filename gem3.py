#notes: 
#https://views.scraperwiki.com/run/python_mechanize_cheat_sheet/?
#http://www.blog.pythonlibrary.org/2012/06/08/python-101-how-to-submit-a-web-form/
#http://stackoverflow.com/questions/7896829/using-python-mechanize-to-log-into-websites
#http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/
import mechanize
from lxml import html, etree
import lxml
import configparser

config = configparser.ConfigParser()
config.read('gem.ini')


url = 'https://egem.gemfellowship.org/Login.aspx'

# browser object, optional settings for aspx pages.
br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
#form.set_all_readonly(False) # allow changing the .value of all controls
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# open url
response = br.open(url)

## print text
#print response.read()

## list forms that are in the page
#for form in br.forms():
#    print "Form name:", form.name
#    print form

## select form
br.select_form(name="aspnetForm")	# 'aspnetForm'

## set up dictionary style payload
br["ctl00$ContentPlaceHolder1$tbEmail"] = config['account']['email']	# email
br["ctl00$ContentPlaceHolder1$tbPassword"] = config['account']['password']	# passwrod

response = br.submit()

content = response.read()

## save to file
#with open("mechanize_results.html", "w") as f:
#    f.write(content)
tree = html.fromstring(content)

tableheaders = tree.xpath("//*[@id='ctl00_ContentPlaceHolder1_pnlApplicationStatus']/table/tr/th/text()")
## recommendations
print tableheaders[0].strip()
recco = tree.xpath(".//*[@id='ctl00_ContentPlaceHolder1_pnlApplicationStatus']/table[1]/tr")
for recc in recco[1:4]:
	for rec in recc.xpath("./td/span/text()"):
		print rec,"\t",
	print ""
print

## graduate schools
print "Graduate Schools:"
schools = tree.xpath(".//*[@id='ctl00_ContentPlaceHolder1_pnlGraduateSchools']/table/tr")
for school in schools[2:5]:
	for schoo in school.xpath("./td/span/text()"):
		print schoo,"\t",
	print ""

plan = tree.xpath("//*[@id='ctl00_ContentPlaceHolder1_pnlGraduateSchools']/*")
for pla in plan[3:5]:
	for pl in pla.xpath("./text()"):
		print pl,"\t",
print

## GRE & Other information
print
table = tree.xpath(".//*[@id='ctl00_ContentPlaceHolder1_pnlApplicationStatus']/table[2]/tr")
print table[0].xpath("./th/text()")[0].strip()
for row in table[1:]:
	for col in row.xpath("./th/text() | ./td/text() | ./td/span/text()"):
		print col.strip(), 
	print ""