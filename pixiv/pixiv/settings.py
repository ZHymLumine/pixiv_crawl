# -*- coding: utf-8 -*-

# Scrapy settings for pixiv project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pixiv'

SPIDER_MODULES = ['pixiv.spiders']
NEWSPIDER_MODULE = 'pixiv.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'pixiv (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'authority': 'pixon.ads-pixiv.net',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'sec-fetch-dest': 'iframe',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'referer': 'https://www.pixiv.net/',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'cookie': '__cfduid=db2cca33a66556f2f1627e7e83913fe751585996012; first_visit_datetime_pc=2020-04-04+19%3A26%3A52; p_ab_id=6; p_ab_id_2=3; p_ab_d_id=1223147675; yuid_b=NCYXVhE; _ga=GA1.2.777937962.1585996016; device_token=b626d1f7e0adada66ba03e25d0cc1c00; c_type=18; a_type=0; b_type=1; login_ever=yes; adr_id=u58UsYD6EHUVRMTgPjzmCGn0dptoLtZ79PLKsA8m6qSVevsZ; __gads=ID=635b064008b55b51:T=1585996044:S=ALNI_MZGVjONoCK_KhaKr9qT1a30xpmTLg; ki_r=; howto_recent_view_history=19395244%2C58647282; ki_t=1585996042824%3B1586168909379%3B1586169905226%3B3%3B20; __utmz=235335808.1586665805.25.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; __utma=235335808.777937962.1585996016.1586744022.1586766858.27; categorized_tags=3ze0RLmk59~6sZKldb07K~BU9SQkS-zU~IVwLyT8B6k~OEXgaiEbRa~OT-C6ubi9i~RcahSSzeRf~WcTW9TCOx9~b8b4-hqot7~fgp2llLuiV~jfnUZgnpFl~kP7msdIeEU~y8GNntYHsi; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=52518258=1^9=p_ab_id=6=1^10=p_ab_id_2=3=1^11=lang=zh=1; is_sensei_service_user=1; _fbp=fb.1.1586998654842.1752023768; _gid=GA1.2.66411078.1586998938; login_bc=1; PHPSESSID=50161662_nWRby9QKCO9BnlLCk4IxvDkjdsVPTkgQ; privacy_policy_agreement=1; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~jH0uD88V6F~tgP8r-gOe_~azESOjmQSV~PTyxATIsK0~aBenX0jTxW~TDYz37gvjg~HY55MqmzzQ~RybylJRnhJ~uS78oFkK_-~y3NlVImyly~SoxapNkN85~oLPD5rNe0R~U3ZDkVtpIO~VTeFUlRxgl~d2oWv_4U1L~ua2BSn-Kwj~pzzjRSV6ZO~XDEWeW9f9i~w8ffkPoJ_S~Bd2L9ZBE8q~LtW-gO6CmS~RcahSSzeRf~OT4SuGenFI~o3o9P--kXx~MhuNMsFpmN~1m8UkUR-IC~EUwzYuPRbU~_pwIgrV8TB~CrFcrMFJzz~qtVr8SCFs5~9hikV84Xs8~X_1kwTzaXt~IyYDgWWer9~esJeKDeN4O~WrCjn6vS7j~6293srEnwa~BOHDnbK1si~H-yV-irFdF~gpglyfLkWs~o7hvUrSGDN~l-qtJXtway~YKuOuDnoxv~QNQ6n5w-QV~J72UWRuuEM~sQC4pGQx9E~AAddtShcPw~cE75kmXk5v~doKLu5a3ct~jfnUZgnpFl~vCSJmv5Z4r~K8esoIs2eW~cbmDKjZf9z~WcTW9TCOx9~fAH-uXqd9x~F5CBR92p_Q~YxYKMgmcme~7WfWkHyQ76~uQc8gGWflJ~wdLGoQWcnW~FPCeANM2Bm~fImt-tQjtm~Nbvc4l7O_x~BMJ4L2soDq~Ww2eYJNQdI~-bBI1XQYRK~MSNRmMUDgC~gXqeZLizjg~RKAHEY3QDd~2X0EUPFeD0~AYK00_a66q~38QHnJb19N~_KZJJXoWbu~SQrOhemtkw~HPBicvCzd6~7GWZV7Vdul~oJAJo4VO5E~v3nOtgG77A~fg8EOt4owo~nQRrj5c6w_~eVxus64GZU~7lt5DImm6I~lxfrUKMf9f~UX647z2Emo~KRYxrx_nx-~QxkezdmKix~n7YxiukgPF~BU9SQkS-zU~y8GNntYHsi~wKl4cqK7Gl~t6fkfIQnjP~lvb9wvOmP1~AAEyK1fN5m~-sp-9oh8uv~HNYzgdz6U7~H7qKdacf1z~XoXIjxuZvN~fgp2llLuiV~xJNxXv4Q5F'


}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pixiv.middlewares.PixivSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pixiv.middlewares.PixivDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pixiv.pipelines.PixivPipeline': 300,
}
IMAGES_STORE = 'D:/CrawlerPictures/pixiv_users_pictures_scrapy'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
