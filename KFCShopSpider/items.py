import scrapy

class KFCShopspiderItem(scrapy.Item):
    name = scrapy.Field()
    address = scrapy.Field()
    map_url = scrapy.Field()
    DriveThrough = scrapy.Field()
    Parking = scrapy.Field()
    Delivery = scrapy.Field()
    Wlan = scrapy.Field()
    pass