import HTML
import appartement_scraper as data

table_data = data.extract_stadgenoot()

htmlcode = HTML.table(table_data)
print htmlcode