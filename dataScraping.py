import requests
import semChunk as chunking
from bs4 import BeautifulSoup
import preProcessing


url='https://indiankanoon.org/search/?formInput=doctypes:supremecourt%20fromdate:1-1-2017%20todate:%2031-12-2017'

response=requests.get(url)

if response.status_code == 200:
    hData=BeautifulSoup(response.text,'html.parser')
    results=hData.find_all('div',class_='result')

    for result in results:
        case_url=result.find('a')
        if case_url:
            link=case_url['href']
            link='https://indiankanoon.org'+link

            #retrieving files and chunking

            docHtml=requests.get(link)

            doc=BeautifulSoup(docHtml.text,'html.parser')

            precedents = doc.find_all(attrs={"data-structure": "Precedent"})
            for precedent in precedents:
                precedent.extract() #removes precedent data structure because we do not need it
            
            content=doc.find_all('p')

            for con in content:
                con=con.get_text(strip=True)
                print("\n",con)
                #chunks=chunking.get_chunks_fixed_size(con,4)
                #chunks=preProcessing.recursiveChunk(con)
            #chunking.semChunk(chunks)
            #put in vector db

        break








else:
    print('Failed to retrieve page')

