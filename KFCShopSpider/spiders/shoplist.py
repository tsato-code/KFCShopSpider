import scrapy
from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest
from ..items import KFCShopspiderItem

class KFCShopSpider(CrawlSpider):
    name = "KFCShopSpider"
    allowed_domains = ["kfc.co.jp"]

    start_urls = []
    shop_url_home ='http://www.kfc.co.jp/search/fuken.html?t=attr_con&kencode='
    # 47都道府県の検索結果ページを起点にする。
    for i in range(1,48):
        prfct_id = '{0:02d}'.format(i)
        url = shop_url_home + prfct_id
        start_urls.append(url)

    # レンダリング済みのresponseを取得します。
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                args={'wait': 0.5},
        )

    def parse(self, response):
        # 各店舗情報(=list要素)まで指定する。
        stores = response.xpath('//ul[@id="outShop"]/li')
        for store in stores:
            item = KFCShopspiderItem()
            # 相対パスで記述する。
            item['name']        = store.xpath('./span[@class="scShopName"]/text()[1]').extract()
            item['address']     = store.xpath('./span[@class="scAddress"]/text()[1]').extract()
            item['map_url']     = store.xpath('./ul/li[2]/div/a/@href').extract()
            item['DriveThrough']= store.xpath('./span[@class="scIcon"]/img[contains(./@src,"check04")]/@alt').extract()
            item['Parking']     = store.xpath('./span[@class="scIcon"]/img[contains(./@src,"check05")]/@alt').extract()
            item['Delivery']    = store.xpath('./span[@class="scIcon"]/img[contains(./@src,"check02")]/@alt').extract()
            item['Wlan']        = store.xpath('./span[@class="scIcon"]/img[contains(./@src,"check03")]/@alt').extract()
            yield item

        # 各検索結果の'次へ'のlink先を取得してpaeseメソッドをcallする。
        next_page= response.xpath('//li[@class="next"]/a/@href')
        if next_page:
            # '次へ'が店舗リストの上下に2つあるので、1つ目の要素だけ取得
            url = response.urljoin(next_page[0].extract())
            yield SplashRequest(url, self.parse)