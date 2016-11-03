from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_soupdata(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webdata = urlopen(req).read()
    webdata = webdata.decode('UTF-8')
    soup = BeautifulSoup(webdata, 'html.parser')
    return soup

def download_transcript(link):
    soup = get_soupdata(link)
    data = soup.find('div',{'class':'speech'})
    title = data.find('h3').get_text()
    title = title.replace(' ','_').replace(',','').replace("'",'')\
                .replace('"','').replace('?','').replace('â€','')\
                .replace('œ','').replace('™','').replace('/','-').replace(':','') + '.txt'
    file = open('./speeches/'+title,'w')
    speech_content = data.find('div',{'class':'speech-content'}).get_text()
    speech_content = speech_content.replace('‘',"'").replace('’',"'").replace('','').replace('\u2011','')
    try:
        file.write(speech_content)
        print(title,'created')
    except Exception as e:
        print(e)

def get_list():
    url = 'http://www.britishpoliticalspeech.org/'
    archive_link = url+'speech-archive.htm'
    soup = get_soupdata(archive_link)

    data = soup.find('table',{'class':'results-table'})
    links = data.find('tbody').find_all('a')

    for link in links:
        link = url+'/'+link.get('href')
        download_transcript(link)

if __name__ == "__main__":
    get_list()