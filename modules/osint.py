import os
import sys
import time
import requests
import subprocess
from pystyle import Colors, Colorate, Write

#OSINT MADE BY SLUROQ

class LoadModules:
    @staticmethod
    def username_lookup():
        os.system("cls" if os.name == "nt" else "clear")

        username = Write.Input("Enter username: ", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)
        
        os.system("cls" if os.name == "nt" else "clear")
        
        social_sites = {
            "sites": [
                {"sitename": "Twitter", "url": "https://x.com/{}"},
                {"sitename": "Instagram", "url": "https://www.instagram.com/{}"},
                {"sitename": "Facebook", "url": "https://www.facebook.com/{}"},
                {"sitename": "LinkedIn", "url": "https://www.linkedin.com/in/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "GitHub", "url": "https://github.com/{}"},
                {"sitename": "Medium", "url": "https://medium.com/@{}"},
                {"sitename": "Quora", "url": "https://www.quora.com/profile/{}"},
                {"sitename": "Pinterest", "url": "https://www.pinterest.com/{}"},
                {"sitename": "TikTok", "url": "https://www.tiktok.com/@{}"},
                {"sitename": "Snapchat", "url": "https://www.snapchat.com/add/{}"},
                {"sitename": "Tumblr", "url": "https://{}.tumblr.com"},
                {"sitename": "Discord", "url": "https://discord.com/users/{}"},
                {"sitename": "Steam", "url": "https://steamcommunity.com/id/{}"},
                {"sitename": "Twitch", "url": "https://www.twitch.tv/{}"},
                {"sitename": "YouTube", "url": "https://www.youtube.com/user/{}"},
                {"sitename": "Vimeo", "url": "https://vimeo.com/{}"},
                {"sitename": "SoundCloud", "url": "https://soundcloud.com/{}"},
                {"sitename": "Spotify", "url": "https://open.spotify.com/user/{}"},
                {"sitename": "DeviantArt", "url": "https://www.deviantart.com/{}"},
                {"sitename": "Flickr", "url": "https://www.flickr.com/people/{}"},
                {"sitename": "Behance", "url": "https://www.behance.net/{}"},
                {"sitename": "Dribbble", "url": "https://dribbble.com/{}"},
                {"sitename": "GitLab", "url": "https://gitlab.com/{}"},
                {"sitename": "Bitbucket", "url": "https://bitbucket.org/{}"},
                {"sitename": "StackOverflow", "url": "https://stackoverflow.com/users/{}"},
                {"sitename": "HackerRank", "url": "https://www.hackerrank.com/{}"},
                {"sitename": "LeetCode", "url": "https://leetcode.com/{}"},
                {"sitename": "CodePen", "url": "https://codepen.io/{}"},
                {"sitename": "Patreon", "url": "https://www.patreon.com/{}"},
                {"sitename": "BuyMeACoffee", "url": "https://www.buymeacoffee.com/{}"},
                {"sitename": "Ko-fi", "url": "https://ko-fi.com/{}"},
                {"sitename": "Etsy", "url": "https://www.etsy.com/shop/{}"},
                {"sitename": "eBay", "url": "https://www.ebay.com/usr/{}"},
                {"sitename": "Amazon", "url": "https://www.amazon.com/hz/wishlist/ls/{}"},
                {"sitename": "Shopify", "url": "https://{}.myshopify.com"},
                {"sitename": "Tinder", "url": "https://tinder.com/@{}"},
                {"sitename": "Bumble", "url": "https://bumble.com/app/@{}"},
                {"sitename": "OkCupid", "url": "https://www.okcupid.com/profile/{}"},
                {"sitename": "Bitcointalk", "url": "https://bitcointalk.org/index.php?action=profile;user={}"},
                {"sitename": "Blockchain", "url": "https://www.blockchain.com/btc/address/{}"},
                {"sitename": "Coinbase", "url": "https://www.coinbase.com/{}"},
                {"sitename": "Binance", "url": "https://www.binance.com/en/user/{}"},
                {"sitename": "Kraken", "url": "https://www.kraken.com/u/{}"},
                {"sitename": "Pornhub", "url": "https://www.pornhub.com/users/{}"},
                {"sitename": "OnlyFans", "url": "https://onlyfans.com/{}"},
                {"sitename": "Chaturbate", "url": "https://chaturbate.com/{}"},
                {"sitename": "MyFreeCams", "url": "https://profiles.myfreecams.com/{}"},
                {"sitename": "Fiverr", "url": "https://www.fiverr.com/{}"},
                {"sitename": "Upwork", "url": "https://www.upwork.com/freelancers/{}"},
                {"sitename": "Freelancer", "url": "https://www.freelancer.com/u/{}"},
                {"sitename": "Trello", "url": "https://trello.com/{}"},
                {"sitename": "Slack", "url": "https://{}.slack.com"},
                {"sitename": "WordPress", "url": "https://{}.wordpress.com"},
                {"sitename": "Blogger", "url": "https://{}.blogspot.com"},
                {"sitename": "About.me", "url": "https://about.me/{}"},
                {"sitename": "Gravatar", "url": "https://en.gravatar.com/{}"},
                {"sitename": "TripAdvisor", "url": "https://www.tripadvisor.com/members/{}"},
                {"sitename": "Yelp", "url": "https://www.yelp.com/user_details?userid={}"} ,
                {"sitename": "Goodreads", "url": "https://www.goodreads.com/user/show/{}"},
                {"sitename": "Last.fm", "url": "https://www.last.fm/user/{}"},
                {"sitename": "Mixcloud", "url": "https://www.mixcloud.com/{}"},
                {"sitename": "ReverbNation", "url": "https://www.reverbnation.com/{}"},
                {"sitename": "Bandcamp", "url": "https://bandcamp.com/{}"},
                {"sitename": "Discogs", "url": "https://www.discogs.com/user/{}"},
                {"sitename": "Chess.com", "url": "https://www.chess.com/member/{}"},
                {"sitename": "Lichess", "url": "https://lichess.org/@/{}"},
                {"sitename": "Keybase", "url": "https://keybase.io/{}"},
                {"sitename": "Mastodon", "url": "https://mastodon.social/@{}"},
                {"sitename": "Letterboxd", "url": "https://letterboxd.com/{}"},
                {"sitename": "Strava", "url": "https://www.strava.com/athletes/{}"},
                {"sitename": "Runkeeper", "url": "https://runkeeper.com/user/{}"},
                {"sitename": "Duolingo", "url": "https://www.duolingo.com/profile/{}"},
                {"sitename": "Codecademy", "url": "https://www.codecademy.com/profiles/{}"},
                {"sitename": "Coursera", "url": "https://www.coursera.org/user/{}"},
                {"sitename": "Udemy", "url": "https://www.udemy.com/user/{}"},
                {"sitename": "KhanAcademy", "url": "https://www.khanacademy.org/profile/{}"},
                {"sitename": "Instructables", "url": "https://www.instructables.com/member/{}"},
                {"sitename": "Thingiverse", "url": "https://www.thingiverse.com/{}"},
                {"sitename": "Hackaday", "url": "https://hackaday.io/{}"},
                {"sitename": "ProductHunt", "url": "https://www.producthunt.com/@{}"},
                {"sitename": "AngelList", "url": "https://angel.co/u/{}"},
                {"sitename": "Crunchbase", "url": "https://www.crunchbase.com/person/{}"},
                {"sitename": "Dailymotion", "url": "https://www.dailymotion.com/{}"},
                {"sitename": "Rumble", "url": "https://rumble.com/user/{}"},
                {"sitename": "Newgrounds", "url": "https://www.newgrounds.com/portal/view/{}"},
                {"sitename": "Kongregate", "url": "https://www.kongregate.com/accounts/{}"},
                {"sitename": "ArmorGames", "url": "https://armorgames.com/user/{}"},
                {"sitename": " itch.io", "url": "https://itch.io/profile/{}"},
                {"sitename": "GameJolt", "url": "https://gamejolt.com/@{}"},
                {"sitename": "Roblox", "url": "https://www.roblox.com/user.aspx?username={}"} ,
                {"sitename": "Xbox", "url": "https://xbox.com/en-US/profiles/{}"},
                {"sitename": "PlayStation", "url": "https://psnprofiles.com/{}"},
                {"sitename": "EpicGames", "url": "https://www.epicgames.com/id/{}"},
                {"sitename": "Origin", "url": "https://www.origin.com/usa/en-us/profile/user/{}"},
                {"sitename": "Battle.net", "url": "https://us.battle.net/account/{}"},
                {"sitename": "GOG", "url": "https://www.gog.com/u/{}"},
                {"sitename": "Weebly", "url": "https://{}.weebly.com"},
                {"sitename": "Wix", "url": "https://{}.wixsite.com/mysite"},
                {"sitename": "Squarespace", "url": "https://{}.squarespace.com"},
                {"sitename": "Carbonmade", "url": "https://{}.carbonmade.com"},
                {"sitename": "Portfolium", "url": "https://portfolium.com/{}"},
                {"sitename": "Coroflot", "url": "https://www.coroflot.com/{}"},
                {"sitename": "ArtStation", "url": "https://www.artstation.com/{}"},
                {"sitename": "Society6", "url": "https://society6.com/{}"},
                {"sitename": "Redbubble", "url": "https://www.redbubble.com/people/{}"},
                {"sitename": "Teespring", "url": "https://teespring.com/stores/{}"},
                {"sitename": "Zazzle", "url": "https://www.zazzle.com/store/{}"},
                {"sitename": "CafePress", "url": "https://www.cafepress.com/{}"},
                {"sitename": "Threadless", "url": "https://www.threadless.com/@{}"},
                {"sitename": "Kickstarter", "url": "https://www.kickstarter.com/profile/{}"},
                {"sitename": "Indiegogo", "url": "https://www.indiegogo.com/individuals/{}"},
                {"sitename": "GoFundMe", "url": "https://www.gofundme.com/f/{}"},
                {"sitename": "VSCO", "url": "https://vsco.co/{}"},
                {"sitename": "500px", "url": "https://500px.com/{}"},
                {"sitename": "SmugMug", "url": "https://{}.smugmug.com"},
                {"sitename": "EyeEm", "url": "https://www.eyeem.com/u/{}"},
                {"sitename": "Imgur", "url": "https://imgur.com/user/{}"},
                {"sitename": "Photobucket", "url": "https://photobucket.com/user/{}"},
                {"sitename": "Meetup", "url": "https://www.meetup.com/members/{}"},
                {"sitename": "Eventbrite", "url": "https://www.eventbrite.com/o/{}"},
                {"sitename": "Nextdoor", "url": "https://nextdoor.com/profile/{}"},
                {"sitename": "Couchsurfing", "url": "https://www.couchsurfing.com/people/{}"},
                {"sitename": "Foursquare", "url": "https://foursquare.com/{}"},
                {"sitename": "Swarm", "url": "https://www.swarmapp.com/{}"},
                {"sitename": "Trakt", "url": "https://trakt.tv/users/{}"},
                {"sitename": "TVTime", "url": "https://www.tvtime.com/en/user/{}"},
                {"sitename": "Letterboxd", "url": "https://letterboxd.com/{}"},
                {"sitename": "MyAnimeList", "url": "https://myanimelist.net/profile/{}"},
                {"sitename": "AniList", "url": "https://anilist.co/user/{}"},
                {"sitename": "Crunchyroll", "url": "https://www.crunchyroll.com/user/{}"},
                {"sitename": "Funimation", "url": "https://www.funimation.com/en/profile/{}"},
                {"sitename": "Redditgifts", "url": "https://www.redditgifts.com/profiles/view/{}"},
                {"sitename": "HackerNews", "url": "https://news.ycombinator.com/user?id={}"},
                {"sitename": "Lobsters", "url": "https://lobste.rs/u/{}"},
                {"sitename": "Tildes", "url": "https://tildes.net/~user/{}"},
                {"sitename": "Voat", "url": "https://voat.co/u/{}"},
                {"sitename": "4chan", "url": "https://boards.4chan.org/u/{}"},
                {"sitename": "8kun", "url": "https://8kun.top/u/{}"},
                {"sitename": "Gab", "url": "https://gab.com/{}"},
                {"sitename": "Parler", "url": "https://parler.com/profile/{}"},
                {"sitename": "Gettr", "url": "https://www.gettr.com/user/{}"},
                {"sitename": "TruthSocial", "url": "https://truthsocial.com/@{}"},
                {"sitename": "Minds", "url": "https://www.minds.com/{}"},
                {"sitename": "MeWe", "url": "https://mewe.com/i/{}"},
                {"sitename": "Odysee", "url": "https://odysee.com/@{}"},
                {"sitename": "Bitchute", "url": "https://www.bitchute.com/channel/{}"},
                {"sitename": "PeerTube", "url": "https://peertube.social/accounts/{}"},
                {"sitename": "Diaspora", "url": "https://diasp.org/u/{}"},
                {"sitename": "Friendica", "url": "https://friendi.ca/{}"},
                {"sitename": "Hubzilla", "url": "https://hubzilla.org/channel/{}"},
                {"sitename": "Plurk", "url": "https://www.plurk.com/{}"},
                {"sitename": "Weibo", "url": "https://weibo.com/{}"},
                {"sitename": "VK", "url": "https://vk.com/{}"},
                {"sitename": "Odnoklassniki", "url": "https://ok.ru/{}"},
                {"sitename": "QQ", "url": "https://user.qzone.qq.com/{}"},
                {"sitename": "Douban", "url": "https://www.douban.com/people/{}"},
                {"sitename": "Renren", "url": "https://www.renren.com/{}"},
                {"sitename": "BaiduTieba", "url": "https://tieba.baidu.com/home/main?un={}"},
                {"sitename": "Zhihu", "url": "https://www.zhihu.com/people/{}"},
                {"sitename": "Bilibili", "url": "https://space.bilibili.com/{}"},
                {"sitename": "Niconico", "url": "https://www.nicovideo.jp/user/{}"},
                {"sitename": "Misskey", "url": "https://misskey.io/@{}"},
                {"sitename": "Pixiv", "url": "https://www.pixiv.net/en/users/{}"},
                {"sitename": "DeviantArt", "url": "https://www.deviantart.com/{}"},
                {"sitename": "ArtStation", "url": "https://www.artstation.com/{}"},
                {"sitename": "FurAffinity", "url": "https://www.furaffinity.net/user/{}"},
                {"sitename": "Inkbunny", "url": "https://inkbunny.net/{}"},
                {"sitename": "SoFurry", "url": "https://www.sofurry.com/user/{}"},
                {"sitename": "Weasyl", "url": "https://www.weasyl.com/~{}"},
                {"sitename": "E621", "url": "https://e621.net/user/{}"},
                {"sitename": "HentaiFoundry", "url": "https://www.hentai-foundry.com/user/{}"},
                {"sitename": "Rule34", "url": "https://rule34.xxx/index.php?page=account&s=profile&uname={}"},
                {"sitename": "Patreon", "url": "https://www.patreon.com/{}"},
                {"sitename": "Substack", "url": "https://{}.substack.com"},
                {"sitename": "Ghost", "url": "https://{}.ghost.io"},
                {"sitename": "Hashnode", "url": "https://{}.hashnode.dev"},
                {"sitename": "Dev.to", "url": "https://dev.to/{}"},
                {"sitename": "Overclock.net", "url": "https://www.overclock.net/members/{}.html"},
                {"sitename": "Tom'sHardware", "url": "https://forums.tomshardware.com/members/{}.html"},
                {"sitename": "AnandTech", "url": "https://forums.anandtech.com/members/{}.html"},
                {"sitename": "HardForum", "url": "https://hardforum.com/members/{}"},
                {"sitename": "LinusTechTips", "url": "https://linustechtips.com/profile/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "Voat", "url": "https://voat.co/u/{}"},
                {"sitename": "SomethingAwful", "url": "https://forums.somethingawful.com/member/{}"},
                {"sitename": "GameFAQs", "url": "https://gamefaqs.gamespot.com/community/{}"},
                {"sitename": "NeoGAF", "url": "https://www.neogaf.com/members/{}"},
                {"sitename": "Resetera", "url": "https://www.resetera.com/members/{}"},
                {"sitename": "IGN", "url": "https://www.ign.com/users/{}"},
                {"sitename": "Polygon", "url": "https://www.polygon.com/users/{}"},
                {"sitename": "Kotaku", "url": "https://kotaku.com/{}"},
                {"sitename": "Eurogamer", "url": "https://www.eurogamer.net/profiles/{}"},
                {"sitename": "Destructoid", "url": "https://www.destructoid.com/author/{}"},
                {"sitename": "RockPaperShotgun", "url": "https://www.rockpapershotgun.com/author/{}"},
                {"sitename": "PCGamer", "url": "https://www.pcgamer.com/author/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "HackerNews", "url": "https://news.ycombinator.com/user?id={}"},
                {"sitename": "ProductHunt", "url": "https://www.producthunt.com/@{}"},
                {"sitename": "AngelList", "url": "https://angel.co/u/{}"},
                {"sitename": "Crunchbase", "url": "https://www.crunchbase.com/person/{}"},
                {"sitename": "SlideShare", "url": "https://www.slideshare.net/{}"},
                {"sitename": "Scribd", "url": "https://www.scribd.com/user/{}"},
                {"sitename": "Academia.edu", "url": "https://www.academia.edu/people/{}"},
                {"sitename": "ResearchGate", "url": "https://www.researchgate.net/profile/{}"},
                {"sitename": "ORCID", "url": "https://orcid.org/{}"},
                {"sitename": "Goodreads", "url": "https://www.goodreads.com/user/show/{}"},
                {"sitename": "LibraryThing", "url": "https://www.librarything.com/profile/{}"},
                {"sitename": "BookCrossing", "url": "https://www.bookcrossing.com/mybookshelf/{}"},
                {"sitename": "Anobii", "url": "https://www.anobii.com/{}"},
                {"sitename": "Wattpad", "url": "https://www.wattpad.com/user/{}"},
                {"sitename": "Fanfiction.net", "url": "https://www.fanfiction.net/u/{}"},
                {"sitename": "ArchiveOfOurOwn", "url": "https://archiveofourown.org/users/{}"},
                {"sitename": "Quotev", "url": "https://www.quotev.com/{}"},
                {"sitename": "FictionPress", "url": "https://www.fictionpress.com/u/{}"},
                {"sitename": "LiveJournal", "url": "https://{}.livejournal.com"},
                {"sitename": "Dreamwidth", "url": "https://{}.dreamwidth.org"},
                {"sitename": "Bloglovin", "url": "https://www.bloglovin.com/@{}"},
                {"sitename": "Typepad", "url": "https://{}.typepad.com"},
                {"sitename": "Xanga", "url": "https://xanga.com/{}"},
                {"sitename": "Skyrock", "url": "https://skyrock.com/{}"},
                {"sitename": "GaiaOnline", "url": "https://www.gaiaonline.com/profiles/{}"},
                {"sitename": "Neopets", "url": "https://www.neopets.com/userlookup.phtml?user={}"},
                {"sitename": "ClubPenguin", "url": "https://www.clubpenguin.com/player/{}"},
                {"sitename": "Habbo", "url": "https://www.habbo.com/profile/{}"},
                {"sitename": "IMVU", "url": "https://avatars.imvu.com/{}"},
                {"sitename": "SecondLife", "url": "https://my.secondlife.com/{}"},
                {"sitename": "VRChat", "url": "https://vrchat.com/home/user/{}"},
                {"sitename": "Amino", "url": "https://aminoapps.com/u/{}"},
                {"sitename": "WeHeartIt", "url": "https://weheartit.com/{}"},
                {"sitename": "Polyvore", "url": "https://www.polyvore.com/cgi/profile?id={}"},
                {"sitename": "Lookbook", "url": "https://lookbook.nu/{}"},
                {"sitename": "Chictopia", "url": "https://www.chictopia.com/{}"},
                {"sitename": "StyleBistro", "url": "https://www.stylebistro.com/{}"},
                {"sitename": "FetLife", "url": "https://fetlife.com/users/{}"},
                {"sitename": "AdultFriendFinder", "url": "https://adultfriendfinder.com/p/member/{}"},
                {"sitename": "AshleyMadison", "url": "https://www.ashleymadison.com/profile/{}"},
                {"sitename": "SeekingArrangement", "url": "https://www.seeking.com/member/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "Tumblr", "url": "https://{}.tumblr.com"},
                {"sitename": "WordPress", "url": "https://{}.wordpress.com"},
                {"sitename": "Blogger", "url": "https://{}.blogspot.com"},
                {"sitename": "Weebly", "url": "https://{}.weebly.com"},
                {"sitename": "Wix", "url": "https://{}.wixsite.com/mysite"},
                {"sitename": "Squarespace", "url": "https://{}.squarespace.com"},
                {"sitename": "TripAdvisor", "url": "https://www.tripadvisor.com/members/{}"},
                {"sitename": "Yelp", "url": "https://www.yelp.com/user_details?userid={}"},
                {"sitename": "Foursquare", "url": "https://foursquare.com/{}"},
                {"sitename": "Swarm", "url": "https://www.swarmapp.com/{}"},
                {"sitename": "Untappd", "url": "https://untappd.com/user/{}"},
                {"sitename": "RateBeer", "url": "https://www.ratebeer.com/user/{}"},
                {"sitename": "BeerAdvocate", "url": "https://www.beeradvocate.com/user/profile/{}"},
                {"sitename": "Vivino", "url": "https://www.vivino.com/users/{}"},
                {"sitename": "Mix", "url": "https://mix.com/{}"},
                {"sitename": "StumbleUpon", "url": "https://www.stumbleupon.com/stumbler/{}"},
                {"sitename": "Delicious", "url": "https://del.icio.us/{}"},
                {"sitename": "Digg", "url": "https://digg.com/@{}"},
                {"sitename": "Slashdot", "url": "https://slashdot.org/~{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "Fark", "url": "https://www.fark.com/users/{}"},
                {"sitename": "Metafilter", "url": "https://www.metafilter.com/user/{}"},
                {"sitename": "Kuro5hin", "url": "https://www.kuro5hin.org/user/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "Etsy", "url": "https://www.etsy.com/shop/{}"},
                {"sitename": "eBay", "url": "https://www.ebay.com/usr/{}"},
                {"sitename": "Amazon", "url": "https://www.amazon.com/hz/wishlist/ls/{}"},
                {"sitename": "Shopify", "url": "https://{}.myshopify.com"},
                {"sitename": "Depop", "url": "https://www.depop.com/{}"},
                {"sitename": "Poshmark", "url": "https://poshmark.com/closet/{}"},
                {"sitename": "Mercari", "url": "https://www.mercari.com/u/{}"},
                {"sitename": "Gumroad", "url": "https://gumroad.com/{}"},
                {"sitename": "BigCartel", "url": "https://{}.bigcartel.com"},
                {"sitename": "Storenvy", "url": "https://www.storenvy.com/stores/{}"},
                {"sitename": "Tindie", "url": "https://www.tindie.com/stores/{}"},
                {"sitename": "Craigslist", "url": "https://accounts.craigslist.org/u/{}"},
                {"sitename": "Kijiji", "url": "https://www.kijiji.ca/p/{}"},
                {"sitename": "Gumtree", "url": "https://www.gumtree.com/p/{}"},
                {"sitename": "Letgo", "url": "https://www.letgo.com/en-us/u/{}"},
                {"sitename": "OfferUp", "url": "https://offerup.com/profile/{}"},
                {"sitename": "Airbnb", "url": "https://www.airbnb.com/users/show/{}"},
                {"sitename": "Vrbo", "url": "https://www.vrbo.com/traveler/{}"},
                {"sitename": "Booking.com", "url": "https://www.booking.com/profile/{}"},
                {"sitename": "Expedia", "url": "https://www.expedia.com/user/{}"},
                {"sitename": "TripIt", "url": "https://www.tripit.com/people/{}"},
                {"sitename": "Wanderu", "url": "https://www.wanderu.com/en-us/profile/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "Bitcointalk", "url": "https://bitcointalk.org/index.php?action=profile;user={}"},
                {"sitename": "Blockchain", "url": "https://www.blockchain.com/btc/address/{}"},
                {"sitename": "Coinbase", "url": "https://www.coinbase.com/{}"},
                {"sitename": "Binance", "url": "https://www.binance.com/en/user/{}"},
                {"sitename": "Kraken", "url": "https://www.kraken.com/u/{}"},
                {"sitename": "Bitfinex", "url": "https://www.bitfinex.com/u/{}"},
                {"sitename": "Kucoin", "url": "https://www.kucoin.com/ucenter/{}"},
                {"sitename": "Gemini", "url": "https://www.gemini.com/profile/{}"},
                {"sitename": "Crypto.com", "url": "https://crypto.com/exchange/user/{}"},
                {"sitename": "Huobi", "url": "https://www.huobi.com/en-us/user/{}"},
                {"sitename": "OKEx", "url": "https://www.okex.com/users/{}"},
                {"sitename": "Bittrex", "url": "https://bittrex.com/Account/Profile/{}"},
                {"sitename": "Poloniex", "url": "https://poloniex.com/profile/{}"},
                {"sitename": "CoinMarketCap", "url": "https://coinmarketcap.com/community/profile/{}"},
                {"sitename": "TradingView", "url": "https://www.tradingview.com/u/{}"},
                {"sitename": "LocalBitcoins", "url": "https://localbitcoins.com/accounts/profile/{}"},
                {"sitename": "Paxful", "url": "https://paxful.com/user/{}"},
                {"sitename": "Bisq", "url": "https://bisq.network/u/{}"},
                {"sitename": "Etherscan", "url": "https://etherscan.io/address/{}"},
                {"sitename": "Polygonscan", "url": "https://polygonscan.com/address/{}"},
                {"sitename": "BscScan", "url": "https://bscscan.com/address/{}"},
                {"sitename": "Solscan", "url": "https://solscan.io/account/{}"},
                {"sitename": "CardanoScan", "url": "https://cardanoscan.io/address/{}"},
                {"sitename": "Reddit", "url": "https://www.reddit.com/user/{}"},
                {"sitename": "Pornhub", "url": "https://www.pornhub.com/users/{}"},
                {"sitename": "OnlyFans", "url": "https://onlyfans.com/{}"},
                {"sitename": "Chaturbate", "url": "https://chaturbate.com/{}"},
                {"sitename": "MyFreeCams", "url": "https://profiles.myfreecams.com/{}"},
                {"sitename": "LiveJasmin", "url": "https://www.livejasmin.com/en/profile/{}"},
                {"sitename": "BongaCams", "url": "https://bongacams.com/profile/{}"},
                {"sitename": "Stripchat", "url": "https://stripchat.com/{}"},
                {"sitename": "Camsoda", "url": "https://www.camsoda.com/{}"},
                {"sitename": "XHamster", "url": "https://xhamster.com/users/{}"},
                {"sitename": "YouPorn", "url": "https://www.youporn.com/us/profile/{}"},
                {"sitename": "RedTube", "url": "https://www.redtube.com/users/{}"},
                {"sitename": "ManyVids", "url": "https://www.manyvids.com/Profile/{}"},
                {"sitename": "Clips4Sale", "url": "https://www.clips4sale.com/studio/{}"},
                {"sitename": "IWantClips", "url": "https://www.iwantclips.com/store/{}"},
                {"sitename": "FanCentro", "url": "https://fancentro.com/{}"},
                {"sitename": "JustForFans", "url": "https://justfor.fans/{}"},
                {"sitename": "AVNStars", "url": "https://stars.avn.com/{}"}
            ]
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        
        for site in social_sites["sites"]:
            profile_url = site["url"].format(username)
            try:
                r = requests.get(profile_url, headers=headers, timeout=3)
                if r.status_code == 200:
                    print(Colorate.Horizontal(Colors.red_to_purple, f"[+] {site['sitename']}: {profile_url}"))
                elif r.status_code == 404:
                    print(Colorate.Horizontal(Colors.red_to_purple, f"[-] {site['sitename']}")) 
            except requests.RequestException as e: pass

        Write.Input("\nPress Enter to go back.", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)
        os.system("cls" if os.name == "nt" else "clear")
                
        
    @staticmethod
    def ip_lookup():
        os.system("cls" if os.name == "nt" else "clear")
        ip = Write.Input("Enter IP: ", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)
        
        try:
            r = requests.get(f"https://ipwhois.app/json/{ip}").json()
            
            if not r.get("success", True):
                os.system("cls" if os.name == "nt" else "clear")
                print(Colorate.Horizontal(Colors.red_to_purple, f"[!] Error: {r.get('message', 'Unknown error')}"))
                time.sleep(2)
                return
                
            os.system("cls" if os.name == "nt" else "clear")
            
            print(Colorate.Vertical(Colors.red_to_purple, f"""IP Address: {r.get('ip')}  
Continent: {r.get('continent')}
Country: {r.get('country')}
Country Phone: {r.get('country_phone')}
Region: {r.get('region')}
City: {r.get('city')}
Lat: {r.get('latitude')}
Lon: {r.get('longitude')}
ISP: {r.get('isp')}
"""))
            Write.Input("\nPress Enter to go back.", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)
            os.system("cls" if os.name == "nt" else "clear")
            
        except Exception as error:
            print(Colorate.Horizontal(Colors.red_to_purple, f"[!] Error occurred: {error}"))
            time.sleep(2)
            return
            
    
    @staticmethod
    def phonenumber_lookup():
        os.system("cls" if os.name == "nt" else "clear")

        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone, number_type
        
        phone_number = Write.Input("Enter Phone Number with (+): ", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)

        os.system("cls" if os.name == "nt" else "clear")

        try:
            parsed_number = phonenumbers.parse(phone_number)

            is_possible = phonenumbers.is_possible_number(parsed_number)
            is_valid = phonenumbers.is_valid_number(parsed_number)
            number_format_international = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            number_format_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

            region = geocoder.description_for_number(parsed_number, "en")
            provider = carrier.name_for_number(parsed_number, "en")
            time_zones = timezone.time_zones_for_number(parsed_number)

            print(Colorate.Horizontal(Colors.red_to_purple, f"Phone Number: {phone_number}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"Valid: {'Yes' if is_valid else 'No'}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"Possible: {'Yes' if is_possible else 'No'}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"International Format: {number_format_international}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"National Format: {number_format_national}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"Region: {region}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"Carrier: {provider if provider else 'N/A'}"))
            print(Colorate.Horizontal(Colors.red_to_purple, f"Time Zone(s): {', '.join(time_zones)}"))
            
            Write.Input("\nPress Enter to go back.", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)
            os.system("cls" if os.name == "nt" else "clear")

        except phonenumbers.NumberParseException as e:
            print(Colorate.Horizontal(Colors.red_to_purple, f"[!] Error: {e}"))
            return
    
def main():
    os.system("cls" if os.name == "nt" else "clear")
    if os.name == 'nt':
        os.system("title Slur - OSINT")
    else:
        os.system("printf '\033]0;Slur - OSINT\033\\'")

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        modules = """[ 1 ] Username Lookup - Not always correct! 
[ 2 ] IP Lookup
[ 3 ] Phone Number Lookup
[ x ] Go back to Slur
"""

        colored = Colorate.Vertical(Colors.red_to_purple, modules)
        print(colored)

        userinput = Write.Input(f"\n{os.getlogin()}$OSINT-> ", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)

        if userinput == "1":
            LoadModules.username_lookup()  
        elif userinput == "2":
            LoadModules.ip_lookup()
        elif userinput == "3":
            LoadModules.phonenumber_lookup()
        elif userinput.lower() == "x":
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
            slur_main_path = os.path.join(parent_dir, "slur.py")

            subprocess.Popen(
                [sys.executable, slur_main_path],
                cwd=parent_dir 
            )
            time.sleep(1)
            sys.exit(0)
        else:
            os.system("cls" if os.name == "nt" else "clear")
            main()

if __name__ == "__main__":
    main()
