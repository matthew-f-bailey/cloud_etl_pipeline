import scrapy
from scrapy.utils.response import open_in_browser

class Top100Spider(scrapy.Spider):
    name = 'top100'
    allowed_domains = ['https://www.billboard.com/charts/hot-100']
    start_urls = ['https://www.billboard.com/charts/hot-100/']  # Start here

    def parse(self, response):
        """
            Parse out billboards top 100 songs
        """

        # Grab all list elements of the top 100
        top = response.css("li.chart-list__element")  # returns a Selector

        # Go through all songs and pull out info relative from the list element
        for top_song in top:

            # Grab attributes relative to current song selector
            name = top_song.css("span.chart-element__information__song::text").get()
            artist = top_song.css("span.chart-element__information__artist::text").get()
            this_week = top_song.css("span.chart-element__rank__number::text").get()
            last_week = top_song.css(".text--last::text").get()
            consecutive = top_song.css(".text--week::text").get()
            peak = top_song.css(".text--peak::text").get()

            # Yield each song as an item
            yield dict(
                name=name,
                artist=artist,
                this_week=this_week,
                last_week=self.clean_weeks(last_week),  # Apply cleaning
                consecutive=self.clean_weeks(consecutive),
                peak=self.clean_weeks(peak)
            )

    def clean_weeks(self, txt):
        """Simple function to clean up misc text pulled in"""
        txt = txt.replace("Last Week", "")
        txt = txt.replace("Weeks on Chart", "")
        txt = txt.replace("Peak Rank", "")
        return txt.strip()
