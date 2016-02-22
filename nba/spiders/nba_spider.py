import scrapy

from nba.items import NBATeam, Player

class NBASpider(scrapy.Spider):
    name = "nbaspider"
    allowed_domains = ["sports.yahoo.com"]
    start_urls = [
        "https://sports.yahoo.com/nba/teams/bos/stats/",
        "https://sports.yahoo.com/nba/teams/bro/stats/",
        "https://sports.yahoo.com/nba/teams/nyk/stats/",
        "https://sports.yahoo.com/nba/teams/phi/stats/",
        "https://sports.yahoo.com/nba/teams/tor/stats/",
        "https://sports.yahoo.com/nba/teams/chi/stats/",
        "https://sports.yahoo.com/nba/teams/cle/stats/",
        "https://sports.yahoo.com/nba/teams/det/stats/",
        "https://sports.yahoo.com/nba/teams/ind/stats/",
        "https://sports.yahoo.com/nba/teams/mil/stats/",
        "https://sports.yahoo.com/nba/teams/atl/stats/",
        "https://sports.yahoo.com/nba/teams/mia/stats/",
        "https://sports.yahoo.com/nba/teams/orl/stats/",
        "https://sports.yahoo.com/nba/teams/was/stats/",
        "https://sports.yahoo.com/nba/teams/cha/stats/",
        "https://sports.yahoo.com/nba/teams/gsw/stats/",
        "https://sports.yahoo.com/nba/teams/lac/stats/",
        "https://sports.yahoo.com/nba/teams/lal/stats/",
        "https://sports.yahoo.com/nba/teams/pho/stats/",
        "https://sports.yahoo.com/nba/teams/sac/stats/",
        "https://sports.yahoo.com/nba/teams/nor/stats/",
        "https://sports.yahoo.com/nba/teams/dal/stats/",
        "https://sports.yahoo.com/nba/teams/hou/stats/",
        "https://sports.yahoo.com/nba/teams/sas/stats/",
        "https://sports.yahoo.com/nba/teams/mem/stats/",
        "https://sports.yahoo.com/nba/teams/den/stats/",
        "https://sports.yahoo.com/nba/teams/min/stats/",
        "https://sports.yahoo.com/nba/teams/por/stats/",
        "https://sports.yahoo.com/nba/teams/okc/stats/",
        "https://sports.yahoo.com/nba/teams/uth/stats/",
    ]

    def parse(self, response):
        nbateam = NBATeam()
        temp = response.xpath('//meta[@name="keywords"]/@content').extract()
        nbateam['teamname'] = ''.join(temp).split(',')[0]
        nbateam['roster'] = []
        nbateam['ppg_leaders'] = []
        nbateam['reb_leaders'] = []
        nbateam['ast_leaders'] = []
        nbateam['stl_leaders'] = []
        nbateam['blk_leaders'] = []
 
        rows = response.xpath('//table[@summary="Team Stats"]/tbody')
        max_rows = int(float(rows.xpath('count(//table[@summary="Team Stats"]/tbody/tr)').extract()[0]))
        
        i = 0
        while i < max_rows:
            player = Player()
            playername = rows.xpath('tr/th/a/text()').extract()[i]
            player['name'] = playername
            player['reb'] = float(rows.xpath('tr/td[14]/text()').extract()[i])
            player['ast'] = float(rows.xpath('tr/td[15]/text()').extract()[i])
            player['stl'] = float(rows.xpath('tr/td[17]/text()').extract()[i])
            player['blk'] = float(rows.xpath('tr/td[18]/text()').extract()[i])
            player['ppg'] = float(rows.xpath('tr/td[20]/text()').extract()[i])
            nbateam['roster'].append(player)
            #player['gp'] = float(rows.xpath('tr/td[1]/text()').extract()[i])
            #min_sec = rows.xpath('tr/td[2]/text()').extract()[i]
            #3player['mins'] = float(min_sec.split(':')[0] + min_sec.split(':')[1])
            #player['fgm'] = float(rows.xpath('tr/td[3]/text()').extract()[i])
            #player['fga'] = float(rows.xpath('tr/td[4]/text()').extract()[i])
            #player['fgp'] = float(rows.xpath('tr/td[5]/text()').extract()[i])
            #player['threepm'] = float(rows.xpath('tr/td[6]/text()').extract()[i])
            #player['threepa'] = float(rows.xpath('tr/td[7]/text()').extract()[i])
            #player['threepp'] = float(rows.xpath('tr/td[8]/text()').extract()[i])
            #player['ftm'] = float(rows.xpath('tr/td[9]/text()').extract()[i])
            #player['fta'] = float(rows.xpath('tr/td[10]/text()').extract()[i])
            #player['ftp'] = float(rows.xpath('tr/td[11]/text()').extract()[i])
            #player['oreb'] = float(rows.xpath('tr/td[12]/text()').extract()[i])
            #player['dreb'] = float(rows.xpath('tr/td[13]/text()').extract()[i])
            #player['pf'] = float(rows.xpath('tr/td[19]/text()').extract()[i])
            #player['to'] = float(rows.xpath('tr/td[16]/text()').extract()[i]) 
            i += 1
       
        #sort and store ppg leaders
        nbateam['roster'] = sorted(nbateam['roster'], key=lambda player: player['ppg'], reverse=True)
        i = 0
        while i < 4:
            nbateam['ppg_leaders'].append(nbateam['roster'][i]['name'])
            i += 1

        #sort and store reb leaders
        nbateam['roster'] = sorted(nbateam['roster'], key=lambda player: player['reb'], reverse=True)
        i = 0
        while i < 4:
            nbateam['reb_leaders'].append(nbateam['roster'][i]['name'])
            i += 1
        
        #sort and store ast leaders
        nbateam['roster'] = sorted(nbateam['roster'], key=lambda player: player['ast'], reverse=True)
        i = 0
        while i < 4:
            nbateam['ast_leaders'].append(nbateam['roster'][i]['name'])
            i += 1 
        
        #sort and store stl leaders
        nbateam['roster'] = sorted(nbateam['roster'], key=lambda player: player['stl'], reverse=True)
        i = 0
        while i < 4:
            nbateam['stl_leaders'].append(nbateam['roster'][i]['name'])
            i += 1
        
        #sort and store blk leaders
        nbateam['roster'] = sorted(nbateam['roster'], key=lambda player: player['blk'], reverse=True)
        i = 0
        while i < 4:
            nbateam['blk_leaders'].append(nbateam['roster'][i]['name'])
            i += 1
        
        yield nbateam
