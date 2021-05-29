import scrapy
from items import MovieItem
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector


class ImdbSpider ( scrapy.Spider ) :
    name = 'imdbspider'
    allowed_domains = [ 'elcinema.com' ]
    start_urls = [ 'https://elcinema.com/en/index/work/country/eg?page=1']

    custom_settings = {'FEED_FORMAT' : 'csv' , 'FEED_URI' : 'Movie.csv'}

    ### def start_requests(self):
    ### The default implementation generates Request(url, dont_filter=True) for each url in start_urls

    def parse(self , response ) :

        movies = response.css ( "td:nth-child(3)::text" ).getall ()


        movie_list= response.css ( "td a::attr(href)" ).getall ()

        #for x in range(len(movies)):
        new_movie_list = []
        i =0
        for x in range(0,len(movie_list),2) :
            if (movies[i]== "Movie"):
                new_movie_list.append(movie_list[x])
            i=i+1




      #          j =j +1

        #temp_set = set(movie_list)
      #  movie_list= (list(temp_set))
       # print("heeeeeeeeeeeeeeer")
        for href in new_movie_list :
            yield response.follow ( url = href , callback = self.parse_movie )


        #next_page = response.css (".text-center a::attr(href)" ).getall()[3]
        next_page =[]

        for i in range(2,94):
            url = "https://elcinema.com/en/index/work/country/eg?page="+ str(i)
            next_page.append(url)

        #next_page = response.urljoin ( next_page )

       # if (next_page == "https://elciinema.com/en/index/work/country/eg?page=95" ):
          #  next_page = None

        #If next_page have value
        for n in range(0, 92):
        #Recall parse with url https://sanet.st/page-{}/ where {} number of page.
            yield scrapy.Request ( url = next_page[n] , callback = self.parse )

    def parse_movie(self , response) :
        item = MovieItem()

        try:
            item ['Name'] =  [ x.replace ( '\x0a' , '' ) for x in response.css ( ".left::text" ).getall () ][ 24 ]
            item ['Name'] = item ['Name'].replace('        ', '')
            item [ 'Name' ] = item [ 'Name' ].replace ( '      ' , '' )
        except IndexError:
            item [ 'Name' ] = 'NULL'
        try:
            unallowed=['pre-production','Released', 'in-production', 'Unreleased']
            item['Duration'] = response.css (" .list-separator li::text" ).getall()[1]
            if (item['Duration'] in unallowed):
                item [ 'Duration' ] ="NULL"
        except IndexError:
            item [ 'Duration' ] = 'NULL'
        try:
            item ['genre'] = response.css("#jump-here-genre li a::text").getall()[0]

        except IndexError:
            item [ 'genre' ] = 'NULL'
        try:
            item ['discription'] = response.css ( "p::text" ).getall()[0]
            if (item ['discription']== "\n        "):
                item ['discription'] = "NULL"
        except IndexError:
            item [ 'discription' ] = 'NULL'
        try:
            item ['release_Date'] = response.xpath("/html/body/div[3]/div[1]/div[5]/div/div[2]/div[1]/div[2]/ul[2]/li[1]/ul/li/a[1]//text()").getall () [0 ] + " " + response.xpath ( "/html/body / div [ 3 ] / div [ 1 ] / div [ 5 ] / div / div [ 2 ] / div [ 1 ] /div [ 2 ] / ul [ 2 ] / li [ 1 ] / ul / li / a [ 2 ] // text ()" ).getall()[0]
            check = response.css(".inline a::attr(href)").getall()[1]
            if (check == "#jump-here-genre"):
                item [ 'release_Date' ] = "NULL"

        except IndexError:
            item [ 'release_Date' ] = 'NULL'
        try:
            check = response.css ( ".list-title:nth-child(22) li::text" ).getall()[0]

            if (check== 'Box Office:'):
                item [ 'Total_Revenue' ] = [ x.replace ( '\x0a' , '' ) for x in response.css ( ".list-title:nth-child(22) li::text" ).getall()][1]
                item [ 'Total_Revenue' ] = item [ 'Total_Revenue' ].replace('            ', '')
                item [ 'Total_Revenue' ] = item [ 'Total_Revenue' ].replace(',', '')
            else:
                item [ 'Total_Revenue' ] = "Null"
        except IndexError:
            item [ 'Total_Revenue' ] = 'Null'
        try:
            item ['Rating'] = response.selector.xpath ( " /html/body/div[3]/div[1]/div[5]/div/div[2]/div[1]/div[2]/ul[1]/li[5]/ul/li[2]//text()" ).getall()[0]

        except IndexError:
            item [ 'Rating' ] = 'NULL'
        return item


# Code to make script run like normal Python script
process = CrawlerProcess ()
process.crawl ( ImdbSpider )
process.start ()  # the script will block here untill the crawling is finished
