BOT_NAME = 'KFCShopSpider'
SPIDER_MODULES = ['KFCShopSpider.spiders']
NEWSPIDER_MODULE = 'KFCShopSpider.spiders'

USER_AGENT = 'KFCShopSpider (+http://www.yourdomain.com)'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 3

SPIDER_MIDDLEWARES = {
     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'http://localhost:8050/'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
