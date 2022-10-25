import json
from tkinter import simpledialog
movies = open('project_02/movies.json')
reader = movies.read()
movies_json = json.loads(reader)

##################################
# FOR GRAPH WITH SINGLE DATA SET #
##################################

counts_years = {}
for movie in movies_json:
    #if year == movie['year']:
        if movie['year'] not in counts_years:
            counts_years.update({movie['year']: 1})
        else:
            counts_years[movie['year']] += 1
print('moviescountstotal= ', counts_years)


moviescountstotal=  {1900: 17, 1901: 80, 1902: 7, 1903: 78, 1904: 25, 1905: 35, 1906: 7, 1907: 7, 1908: 18, 1909: 76, 1910: 26, 1911: 28, 1912: 44, 1913: 53, 1914: 179, 1915: 110, 1916: 144, 1917: 97, 1918: 128, 1919: 634, 1920: 129, 1921: 143, 1922: 421, 1923: 395, 1924: 480, 1925: 572, 1926: 491, 1927: 169, 1928: 437, 1929: 347, 1930: 361, 1931: 360, 1932: 408, 1933: 383, 1934: 407, 1935: 446, 1936: 504, 1937: 473, 1938: 423, 1939: 339, 1940: 385, 1941: 358, 1942: 359, 1943: 465, 1944: 456, 1945: 415, 1946: 423, 1947: 390, 1948: 421, 1949: 351, 1950: 443, 1951: 429, 1952: 374, 1953: 366, 1954: 251, 1955: 268, 1956: 300, 1957: 335, 1958: 281, 1959: 205, 1960: 162, 1961: 150, 1962: 144, 1963: 140, 1964: 151, 1965: 129, 1966: 131, 1967: 127, 1968: 143, 1969: 137, 1970: 137, 1971: 145, 1972: 140, 1973: 142, 1974: 142, 1975: 128, 1976: 149, 1977: 131, 1978: 134, 1979: 139, 1980: 182, 1981: 140, 1982: 142, 1983: 140, 1984: 167, 1985: 187, 1986: 192, 1987: 283, 1988: 292, 1989: 261, 1990: 269, 1991: 202, 1992: 224, 1993: 204, 1994: 292, 1995: 307, 1996: 363, 1997: 362, 1998: 242, 1999: 221, 2000: 213, 2001: 226, 2002: 232, 2003: 221, 2004: 239, 2005: 228, 2006: 425, 2007: 304, 2008: 206, 2009: 229, 2010: 210, 2011: 201, 2012: 295, 2013: 376, 2014: 214, 2015: 130, 2016: 143, 2017: 238, 2018: 236}
terms = list(moviescountstotal.keys())
counts = list(moviescountstotal.values())
terms.sort()

accumulator = []
for term in terms:
    accumulator.append(moviescountstotal[term])
counts = accumulator

# this code generates a bar graph plot (graph 1)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.title('US Movies Produced by Year (1900-2018)')
plt.xlabel('Year')
plt.ylabel('Number of Productions')
plt.locator_params(axis='x', nbins=20)
plt.xticks(rotation = 90)
plt.legend(['Movies'])
plt.show()

#################################
# FOR GRAPH WITH BOTH DATA SETS #
#################################

import csv
netflix = open('project_02/netflix_titles.csv')
reader_netflix = csv.reader(netflix)
netflix_list = list(reader_netflix)
netflix_list = netflix_list[1:]

counts_netflixyears = {}
for show in netflix_list:
    year = int(show[7])
    if 2019>year>=1990:
        if year not in counts_netflixyears:
            counts_netflixyears.update({year: 1})
        else:
            counts_netflixyears[year] += 1
print('netflixcounts= ', counts_netflixyears) 

counts_years = {}
for movie in movies_json:
    #if year == movie['year']:
    if movie['year']>=1990:
        if movie['year'] not in counts_years:
            counts_years.update({movie['year']: 1})
        else:
            counts_years[movie['year']] += 1
print('moviescounts= ', counts_years) 

moviescounts= {1990: 269, 1991: 202, 1992: 224, 1993: 204, 1994: 292, 1995: 307, 1996: 363, 1997: 362, 1998: 242, 1999: 221, 2000: 213, 2001: 226, 2002: 232, 2003: 221, 2004: 239, 2005: 228, 2006: 425, 2007: 304, 2008: 206, 2009: 229, 2010: 210, 2011: 201, 2012: 295, 2013: 376, 2014: 214, 2015: 130, 2016: 143, 2017: 238, 2018: 236}
netflixcounts= {1993: 28, 2018: 1147, 1996: 24, 1998: 36, 1997: 38, 2010: 194, 2013: 288, 2017: 1032, 2012: 237,
2001: 45, 2014: 352, 2002: 51, 2003: 61, 2004: 64, 2011: 185, 2008: 136, 2009: 152, 2007: 88, 2005: 80,
2006: 96, 1994: 22, 2015: 560, 2016: 902, 1990: 22, 1991: 17, 1999: 39, 1992: 23, 2000: 37, 1995: 25}

# this code generates a line graph plot (graph 2)
from matplotlib import pyplot as plt
#plt.style.use('fivethirtyeight')
moviecounts_x = [269, 202, 224, 204, 292, 307, 363, 362, 242, 221, 213, 226, 232, 221, 239, 228, 425, 304, 206, 229, 210, 201, 295, 376, 214, 130, 143, 238, 236]
netflixcounts_x = [22, 17, 23, 28, 22, 25, 24, 38, 36, 39, 37, 45, 51, 61, 64, 80, 96, 88, 136, 152, 194, 185, 237, 288, 352, 560, 902, 1032, 1147]
both_y = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
plt.plot(both_y, moviecounts_x, 'b', marker= '.')
plt.plot(both_y, netflixcounts_x, 'r', marker= '.')
plt.xticks(both_y, both_y, rotation='vertical')
plt.title('Neflix Shows & US Movies Produced by Year (1990-2018)')
plt.xlabel('Year')
plt.ylabel('Number of Productions')
plt.legend(['Movies', 'Netflix'])
plt.grid(True)
plt.show()
