import HTML
import appartement_scraper as data

if __name__ == '__main__':
    table_data = get_appartements()#data.extract_pararius()#
    for i in table_data:
        i[6] = HTML.link('Link',i[6])

    htmlcode = HTML.table(table_data)

    Html_file= open("table.html","w")
    Html_file.write(htmlcode)
    Html_file.close()