from collections import namedtuple

HomeNamedtuple = namedtuple('HomeNamedtuple',
                            ['top_nav_links',
                             'firestone_logo'])
HomePageConst = HomeNamedtuple(
    top_nav_links='xpath==//*[@id="top-nav"]//div[@class="links"]/a[.="{}"]',
    firestone_logo='xpath==//*[@id="top-nav"]//div[@class="logo-wrapper"]')
