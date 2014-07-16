import mechanize
import re
import bs4
import urllib
import OS
import time

URL_ROOT = "http://pokemondb.net"
DEFAULT_DEST = "../Sprites/"
START_TIME = time.time()

def request_page(link):
	webpage = bs4.BeautifulSoup(mechanize.urlopen(link).read())
	print('* HTTP Request Sent -> Opened: ' + link)
	return webpage

def construct_link_pattern():
	return re.compile(r'/sprites/\w+')

def locate_sprites_pages(webpage, link_patt):
	sprites_pages = []
	for link in webpage.findAll('a'):
		if re.match(link_patt, link['href']):
			sprites_pages.append(link['href'])
	print ('* Crawled -> Sprite Links')
	return sprites_pages

def construct_sprite_pattern():
	return re.compile(r'.+\.gif')

def scrape_sprites(webpage, sprite_patt):
	count = 0
	for sprite in webpage.findAll('a'):
		if re.match(sprite_patt, sprite['href']:
			filename = re.search(r'\w+/\w+[-\w]*\.gif',sprite['href']).group(0).replace('/','_')
			if count % 2 == 0
				filename = 'front_' + filename
			else
				filename = 'back_' + filename
			outpath = os.path.join(DEFAULT_DEST, filename)
			urllib.urlretrieve(sprite['href'], outpath)
			count += 1
			print('$ GIF Saved -> ' + filename)

def main():
	webpage = request_page(URL_ROOT + '/sprites')
	link_patt = construct_link_pattern
	sprites_pages = locate_sprites_pages(webpage)
	sprite_patt = construct_sprite_pattern()
	for link in sprites_pages:
		webpage = open_browser(URL_ROOT + link)
		scrape_sprites(webpage, sprite_patt)

print('====================================================================================')
print('                               Becoming a Pokemon Master    ')
print('====================================================================================')
main()
exec_time = time.time() - START_TIME
print('====================================================================================')
print('                 Became a master in: %d m %d s' % (exec_time/60,exec_time%60))
print('====================================================================================')