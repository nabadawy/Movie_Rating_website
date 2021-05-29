import scrapy
from items import CastItem, MovieItem
from scrapy.crawler import CrawlerProcess


class ImdbSpider ( scrapy.Spider ) :
    name = 'imdbspider'
    allowed_domains = [ 'elcinema.com' ]
    start_urls = [ 'https://elcinema.com/en/index/work/country/eg?page=1']

    custom_settings = {'FEED_FORMAT' : 'csv' , 'FEED_URI' : 'Cast.csv'}

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
        cast_list = response.css (" .section-title a::attr(href)" ).getall()[0]

        #for href in cast_list :
        yield response.follow ( url = cast_list , callback = self.helper )


    def helper(self, response):
        cast_list = response.css ( ".description a::attr(href)" ).getall ()
        #castRole=[]
        #role= [ x.replace ( '\x0a' , '' ) for x in response.css ( ".section-title::text" ).getall ()]
        #number = response.css ( ".section-title span::text" ).getall ()
        #number = [x.replace ( '(' , '' ) for x in number]
        #number = [x.replace ( ')' , '' ) for x in number]
        #number =[int(i) for i in number]
        #i=0
        #for r in role:
            #li =[r]* number[i]
         #   li = li +[r]* number[i]
          #  li.extend([r+1]*number[i+1])
            #castRole.append(li)
           # i=i+1
        #i=0
        for href in cast_list :
            #role =
            yield response.follow ( url = href , callback = self.parse_Cast)
            #i=i+1

    def parse_Cast(self , response) :
        item = CastItem()
        try:
            string =  response.css (" .jumbo .left::text" ).getall()[0]
            F_Name , V , S_name= string.partition(" ")

        except IndexError:
            item [ 'FirstName' ] = 'null'
            item [ 'SecondName' ] = 'null'
        try:
            item ['FirstName'] =  F_Name
        except IndexError:
            item [ 'FirstName' ] = 'null'
        try:
            item['SecondName'] = S_name
        except IndexError:
            item [ 'SecondName' ] = 'null'
        try:
            item ['Role'], a, b = [x.replace ( ' ' , '' ) for x in response.xpath ("/html/body/div[3]/div[1]/div[8]/div/div[2]/ul/li[1]/a/text()" ).getall()][0].partition("(")


        except IndexError:
            item [ 'Role' ] = 'null'
        try:
            item ['Biography'] = response.css (".no-margin::text" ).getall()
            if (item ['Biography']== "\n        "):
                item ['Biography'] = "NULL"
        except IndexError:
            item [ 'Biography' ] = 'null'
        try:
            item ['Nationality'] = response.css (".list-title li a::text" ).getall()[0]
        except IndexError:
            item [ 'Nationality' ] = 'null'
        try:
            item ['DateOfBirth']= response.css (".list-title li a::text" ).getall()[1]+ " " +response.css (".list-title li a::text" ).getall()[2]
        except IndexError:
            item [ 'DateOfBirth' ] = 'NULL'

        return item

# Code to make script run like normal Python script
process = CrawlerProcess ()
process.crawl ( ImdbSpider )
process.start ()  # the script will block here untill the crawling is finished
