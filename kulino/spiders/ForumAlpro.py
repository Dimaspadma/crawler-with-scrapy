import scrapy

class ForumAlpro(scrapy.Spider):

    name = "alpro"
    start_urls = ["<url login>"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                "username": "<username>",
                "password": "<password>"
            },
            callback=self.after_login
        )
    

    def after_login(self, response):
        url = "<url forum>"
        return scrapy.Request(url, callback=self.parse_login)
    
    def parse_login(self, response):
        for test in response.css('div.mb-3'):

            nimAndName = test.css('a::text').get()
            time = test.css('time::text').get()

            if nimAndName != None:
                if time != None:

                    nimAndName = nimAndName.split('-')
                    time = time.split(',')

                    yield {
                        'name': nimAndName[-1],
                        'nim': nimAndName[0],
                        'hari': time[0],
                        'tanggal': time[1],
                        'jam': time[2]
                    }