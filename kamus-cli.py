#!/usr/bin/python
import requests, re, argparse, sys
from bs4 import BeautifulSoup

main_url = "https://www.kamus.net/"


def main():
	parser = argparse.ArgumentParser(
        description='Word translator Bahasa Indonesia to English(default) or otherwise')
	parser.add_argument('word',metavar='Word(s)', action="store", nargs="+",
                		help='Word to translate')
	parser.add_argument('-e', action='store_true', default=False, dest='lang_en',
                		help="English to Bahasa Indonesia")
	args = vars(parser.parse_args())

	url = main_url
	if args['lang_en']:
		url += "english/"
	else:
		url += "indonesia/"
	if type(args["word"]) == list:
		for word in args["word"]:
			url += word
			url += " "
	else:
		url += args["word"]

	do_requests(url)


def do_requests(url):
	headers = {"user-agent":"Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0"}
	try:
		#print "Sending request",url
		req = requests.get(url, headers=headers)
		soup = BeautifulSoup(req.text, "html.parser")
		kamus_action(soup)

	finally:
		req.close()


def kamus_action(soup):
	not_found = soup.find('hgroup').find('h1')
	found = soup.find('div', id ="featured-term-trans")
	if (not_found != None) and ("couldn't find" in not_found.string):
		terms = soup.find('hgroup').find_all('a')
		print "[!]", not_found.string
		print "Maybe you were looking for one of these:"
		count = 0
		for term in terms:
			count += 1
			if count < len(terms):
				print term.string+",",
			else:
				print term.string
	elif (found != None):
		results = found.find_all('div', class_='trans') #.trans .clearfix
		for result in results:
			try:
				print "[Term]:  ", result.find('div',class_="trans-source").p.strong.string,
			except:
				pass

			try:
				print result.find('div',class_="trans-source").p.span.string,
			except:
				pass
			print 

			print "[Result]:", 
			try:
				res = result.find('div',class_="trans-target").find_all("p")
				count = 0
				for r in res:
					count += 1
					if count < len(res):
						print r.a.strong.string + ",",
					else:
						print r.a.strong.string
			except:
				pass
	else:
		print "[!] Something gone wrong"
		print "[!] Check the code or the website please"


if __name__ == '__main__':
	main()
