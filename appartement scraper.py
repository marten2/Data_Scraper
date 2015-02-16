#!/usr/bin/env python
# Name:
# Student number:
'''
This script scrapes IMDB and outputs a CSV file with highest ranking tv series.
'''
# IF YOU WANT TO TEST YOUR ATTEMPT, RUN THE test-tvscraper.py SCRIPT.
import csv

from pattern.web import URL, DOM

OUTPUT_CSV = 'appartementen.csv'


def extract_rooftrack():    
    '''
    extract list of appartements from rooftrack.nl with:
    'Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link'
    '''
    appartement_l = []
    
    for i in range(50):
        TARGET_URL = "http://www.rooftrack.nl/Zoeken/geo-52;3651323157895,4;88880105263158,0,Amsterdam/huur-0-9999/order-prijsmin,DESC/page-"+str(i)+",20"

        url = URL(TARGET_URL)
        # Download HTML
        html = url.download()
        # HTML in DOM representation
        dom = DOM(html)

        results = dom.by_tag("div.row ResultBox ClickRow")
        # Check voor lege pagina
        if not len(results):
            break

        print "Page ",i+1
        for e in results:
            l = []

            # Plaats
            plaats = e("p.plaatswijk")[0].content
            if not "Amsterdam" in plaats:
                continue

            # Straat
            l.append(e("h6")[0].content)

            comb = e("p.eigenschappen")[0].content.split('<br />')
            soortKamer = comb[0].split(' ')
            
            # Soort
            l.append(soortKamer[0].strip())
            # Kamers
            l.append(soortKamer[1])
            # Opp
            opp = comb[1]
            l.append(opp.split('&')[0].strip())
            # Makelaar
            makelaar = e("small")[0].content
            l.append(makelaar.strip('Aangeboden door '))
            # Huur
            huur = e("strong")[0].content.encode("ascii","ignore")
            l.append(huur.strip())
            
            ascii_l = []
            for c in l:
                ascii_l.append(c.encode("ascii","ignore"))

            appartement_l.append(ascii_l)
    return appartement_l

def extract_stadgenoot():    
    '''
    extract list of appartements from stadgenoot.nl with:
    'Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link'
    '''
    appartement_l = []

    TARGET_URL = "http://www.stadgenoot.nl/zoeken?q=&sort=updatedate&priceRange_use=on&priceRange_valuefrom=650&priceRange_valueto=1500&district=on&type_wonen=on&type_parkeren=&type_ondernemen=&soort_huur=on&city_=on&q-wonen=&q-parkeren=&q-ondernemen="
    url = URL(TARGET_URL)
    # Download HTML
    html = url.download()
    # HTML in DOM representation
    dom = DOM(html)

    print "Page 1"
        
    for e in dom.by_tag("li.object-listitem-search clearfix"):
        l = []

        # Straat
        l.append(e("h3")[0].content.strip())
        
        comb = e("li")[1].content.split('sup>')
        # Soort
        l.append(comb[0].split(',')[0].strip())
        # Kamers
        l.append(comb[2].split('-')[1][1].strip())
        # Opp
        l.append(comb[0].split(',')[1].strip()[:-1])
        # Makelaar
        l.append("Stadgenoot")
        # Huur
        l.append(e("div.object-price")[0].content.strip())
            
        ascii_l = []
        for c in l:
            ascii_l.append(c.encode("ascii","ignore"))

        appartement_l.append(ascii_l)
    return appartement_l

def extract_pararius():    
    '''
    extract list of appartements from pararius.nl with:
    'Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link'
    '''
    appartement_l = []
    
    for i in range(50):
        TARGET_URL = "http://www.pararius.nl/huurwoningen/amsterdam/0-2000/page-"+str(i+1)

        url = URL(TARGET_URL)
        # Download HTML
        html = url.download()
        # HTML in DOM representation
        dom = DOM(html)

        results = dom.by_tag("li.hproduct")
        # Check voor lege pagina
        if not len(results):
            break

        print "Page ",i+1

        for e in results:
            l = []

            # Sommige woningen zijn dode links op pararius
            try: comb_l = e("div.addressTitle a")[0]
            except: continue
            comb_s = comb_l.content.split('-')

            # Straat
            straat = ''.join(comb_s[0].split(' ')[1:])
            
            # Soort
            l.append(comb_s[0].split(' ')[0])

            comb2 = e("div.deform")[0].content
            comb2_s = comb2.split('-')
            # Kamers
            try: l.append(comb2_s[2].strip()[0])
            except: l.append("")
            # Opp
            try: l.append(comb2_s[3].split(' ')[1]+"m")
            except: l.append("0m")
            # Makelaar
            l.append(e("span.spannend a")[0].content)
            # Huur
            huur = e("strong.price b")[0].content
            l.append(huur.strip('Vanaf '))
            # Link
            link = comb_l.attr['href']
            if not 'http' in link: link = "http://www.pararius.nl"+link
            l.append(link)
            
            ascii_l = []
            for c in l:
                ascii_l.append(c.encode("ascii","ignore"))

            appartement_l.append(ascii_l)

    return appartement_l

def save_csv(f, appartement_l):
    writer = csv.writer(f)
    writer.writerow(['Straat', 'Soort', 'Oppervlak', 'Makelaar', 'Huurprijs', 'Link'])
    for l in appartement_l:
        writer.writerow(l)

if __name__ == '__main__':

    # Extract the appartements
    appartement_l = []
##    print "Extracting Rooftrack.nl..."
##    for appartement in extract_rooftrack():
##        appartement_l.append(appartement)
##    print "Extracting Stadgenoot.nl..."
##    for appartement in extract_stadgenoot():
##        appartement_l.append(appartement)
    print "Extracting Pararius.nl..."
    for appartement in extract_pararius():
        appartement_l.append(appartement)

    # Write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'wb') as output_file:
        save_csv(output_file, appartement_l)
