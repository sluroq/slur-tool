import os
import sys
import time
import webbrowser
import subprocess
from pystyle import Colorate, Colors, Write

def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    usefulsites = [
        {
            "category": "─══════════════════════════☆Internet Protocol Television☆══════════════════════════─",
            1: {
                "url": "https://iptvcat.com/",
                "status": "safe"
            },
            2: {
                "url": "https://drakula.stream/",
                "status": "safe"
            },
            3: {
                "url": "https://iptv-web.app/",
                "status": "safe"
            },
            4: {
                "url": "https://searchtv.net/",
                "status": "safe"
            }
        },
        {
            "category": "─══════════════════════════☆Direct Download Link☆══════════════════════════─",
            5: {
                "url": "https://avxhm.se/",
                "status": "untrusted"
            },
            6: {
                "url": "https://www.puzo.org/",
                "status": "untrusted"
            },
            7: {
                "url": "https://rmz.cr/",
                "status": "untrusted"
            },
            8: {
                "url": "https://softarchive.is/",
                "status": "untrusted"
            },
            9: {
                "url": "https://scnlog.me/",
                "status": "untrusted"
            },
            10: {
                "url": "https://downturk.net/",
                "status": "untrusted"
            },
            11: {
                "url": "https://downarchive.org/",
                "status": "untrusted"
            },
            12: {
                "url": "https://paidshitforfree.com/",
                "status": "untrusted"
            }
        },
        {
            "category": "─══════════════════════════☆STREAMING☆══════════════════════════─",
            13: {
                "url": "https://m4uhd.cx/",
                "status": "safe"
            },
            14: {
                "url": "https://ww1.new-movies123.co/",
                "status": "safe"
            },
            15: {
                "url": "https://m4ufree.page/",
                "status": "safe"
            },
            16: {
                "url": "https://gomovies-online.cam/",
                "status": "safe"
            },
            17: {
                "url": "https://www.123movies.co/",
                "status": "safe"
            },
            18: {
                "url": "https://hollymoviehd.cc/",
                "status": "safe"
            },
            19: {
                "url": "https://www.epctv.com/",
                "status": "safe"
            },
            20: {
                "url": "https://flixtor.to/",
                "status": "safe"
            }
        },
        {
            "category": "─══════════════════════════☆TORRENTING☆══════════════════════════─",
            21: {
                "url": "https://solidtorrents.to/",
                "status": "untrusted"
            },
            22: {
                "url": "https://www.torrentfunk.com/",
                "status": "untrusted"
            },
            23: {
                "url": "https://www.torrentdownloads.pro/",
                "status": "untrusted"
            },
            24: {
                "url": "https://1337x.to/",
                "status": "untrusted"
            },
            25: {
                "url": "https://thepiratebay.org/index.html",
                "status": "unsafe"
            },
            26: {
                "url": "https://www.torrentdownload.info/",
                "status": "untrusted"
            },
            27: {
                "url": "https://glodls.to/",
                "status": "untrusted"
            }
        },
        {
            "category": "─══════════════════════════☆Windows Applications☆══════════════════════════─",
            28: {
                "url": "https://getintopc.com/",
                "status": "unsafe"
            },
            29: {
                "url": "https://karanpc.com/",
                "status": "unsafe"
            },
            30: {
                "url": "https://filecr.com/",
                "status": "untrusted"
            },
            31: {
                "url": "https://s0ft4pc.com/",
                "status": "unsafe"
            },
            32: {
                "url": "https://mutaz.net/",
                "status": "untrusted"
            },
            33: {
                "url": "https://up4pc.com/",
                "status": "untrusted"
            },
            34: {
                "url": "https://cracksurl.com/",
                "status": "untrusted"
            },
            35: {
                "url": "https://keygenbook.com/",
                "status": "untrusted"
            }
        },
        {
            "category": "─══════════════════════════☆Windows Games☆══════════════════════════─",
            36: {
                "url": "https://gamepciso.com/",
                "status": "untrusted"
            },
            37: {
                "url": "https://www.skidrowcodex.net/",
                "status": "unsafe"
            },
            38: {
                "url": "https://mrpcgamer.net/",
                "status": "unsafe"
            },
            39: {
                "url": "https://gampower.blogspot.com/",
                "status": "untrusted"
            },
            40: {
                "url": "https://gog-games.to/",
                "status": "untrusted"
            },
            41: {
                "url": "https://steamrip.com/",
                "status": "untrusted"
            }
        },
        {
            "category": "─══════════════════════════☆Windows Serial Keys☆══════════════════════════─",
            42: {
                "url": "https://smartserials.com/",
                "status": "safe"
            },
            43: {
                "url": "https://www.crackserialcodes.com/",
                "status": "safe"
            },
            44: {
                "url": "https://www.serialshack.com/",
                "status": "safe"
            },
            45: {
                "url": "https://keygenguru.com/",
                "status": "safe"
            }
        },
        {
            "category": "─══════════════════════════☆Android Applications☆══════════════════════════─",
            46: {
                "url": "https://a2zapk.io/",
                "status": "untrusted"
            },
            47: {
                "url": "https://android-zone.ws/",
                "status": "untrusted"
            },
            48: {
                "url": "https://apkhome.net/",
                "status": "untrusted"
            },
            49: {
                "url": "https://apkmagic.com.ar/",
                "status": "untrusted"
            },
            50: {
                "url": "https://uapk.pro/",
                "status": "untrusted"
            },
            51: {
                "url": "https://apkshub.com/",
                "status": "untrusted"
            }
        },
        {
            "category": "─══════════════════════════☆Downloaders☆══════════════════════════─",
            52: {
                "url": "https://doubledouble.top/",
                "status": "safe"
            },
            53: {
                "url": "https://cobalt.tools/",
                "status": "safe"
            },
            54: {
                "url": "https://www.internetdownloadmanager.com/",
                "status": "untrusted"
            },
            55: {
                "url": "https://altstore.io/",
                "status": "safe"
            },
            56: {
                "url": "https://hakuneko.download/",
                "status": "safe"
            },
            57: {
                "url": "https://docdownloader.com/",
                "status": "safe"
            },
            58: {
                "url": "https://streamlink.github.io/",
                "status": "safe"
            },
            59: {
                "url": "https://www.y2mate.com/",
                "status": "safe"
            },
            60: {
                "url": "https://www.klickaud.org/",
                "status": "safe"
            },
            61: {
                "url": "https://fastdl.app/",
                "status": "safe"
            },
            62: {
                "url": "https://ssstik.io/",
                "status": "safe"
            },
            63: {
                "url": "https://spotify-downloader.com/",
                "status": "safe"
            },
            64: {
                "url": "https://rapidsave.com/",
                "status": "safe"
            },
            65: {
                "url": "https://maulvi.github.io/",
                "status": "safe"
            },
            66: {
                "url": "https://godownloader.com/",
                "status": "safe"
            }
        },
        {
            "category": "─══════════════════════════☆Virus & Sandbox Checker☆══════════════════════════─",
            67: {
                "url": "https://www.virustotal.com/",
                "status": "safe"
            },
            68: {
                "url": "https://hybrid-analysis.com/",
                "status": "safe"
            },
            69: {
                "url": "https://metadefender.opswat.com/",
                "status": "safe"
            },
            70: {
                "url": "https://www.uncoverit.org/",
                "status": "safe"
            },
            71: {
                "url": "https://www.ctx.io/",
                "status": "safe"
            },
            72: {
                "url": "https://any.run/",
                "status": "safe"
            },
            73: {
                "url": "https://www.joesandbox.com/",
                "status": "safe"
            },
            74: {
                "url": "https://tria.ge/",
                "status": "safe"
            },
            75: {
                "url": "https://urlscan.io/",
                "status": "safe"
            },
            76: {
                "url": "https://www.scamadviser.com/",
                "status": "safe"
            },
            77: {
                "url": "https://binisoft.org/",
                "status": "safe"
            },
            78: {
                "url": "https://www.wireshark.org/",
                "status": "safe"
            },
            79: {
                "url": "https://sourceforge.net/projects/systeminformer/",
                "status": "safe"
            }
        },
        {
            "category": "─══════════════════════════☆Leak Checker☆══════════════════════════─",
            80: {
                "url": "https://www.top10vpn.com/tools/do-i-leak/",
                "status": "safe"
            },
            81: {
                "url": "https://iknowwhatyoudownload.com",
                "status": "safe"
            },
            81: {
                "url": "https://browserleaks.com/",
                "status": "safe"
            },
            82: {
                "url": "https://ipleak.net/",
                "status": "safe"
            }
        },
        {
            "category": "─══════════════════════════☆Virtual Private Networks☆══════════════════════════─",
            83: {
                "url": "https://mullvad.net/",
                "status": "safe"
            },
            84: {
                "url": "https://www.privateinternetaccess.com/",
                "status": "untrusted"
            },
            85: {
                "url": "https://riseup.net/",
                "status": "safe"
            },
            86: {
                "url": "https://protonvpn.com/",
                "status": "safe"
            }
        }
    ]

    while True:
        for category_data in usefulsites:
            print(Colorate.Horizontal(Colors.red_to_purple, f"\n{category_data['category']}\n"))
            for key, value in category_data.items():
                if isinstance(value, dict):
                    print(Colorate.Horizontal(Colors.red_to_purple, f"[ {key} ] {value['url']} - Status: {value['status']}"))

        user_input = Write.Input("\nEnter the number to open the website, or type 'x' to go back to slur.$-> ", Colors.red_to_purple, interval=0, hide_cursor=False, input_color=Colors.purple)

        if user_input.lower() == "x":
            current_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
            slur_main_path = os.path.join(parent_dir, "slur.py")

            subprocess.Popen(
                [sys.executable, slur_main_path],   
                cwd=parent_dir 
            )
            time.sleep(1)
            sys.exit(0)

        try:
            site_number = int(user_input)
            found = False
            for category_data in usefulsites:
                if site_number in category_data:
                    website = category_data[site_number]
                    webbrowser.open(website['url'])
                    found = True
                    print(Colorate.Horizontal(Colors.red_to_purple, f"Opening {website['url']}..."))
                    os.system("cls" if os.name == "nt" else "clear")
                    break 
            if not found:
                print(Colorate.Horizontal(Colors.red_to_purple, "Invalid input. Please enter a valid site number."))
        except ValueError:
            print(Colorate.Horizontal(Colors.red_to_purple, "Please enter a valid number."))


if __name__ == "__main__":
    if os.name == 'nt':
        os.system("title Slur - Useful Websites")
    else:
        os.system("printf '\033]0;Slur - Useful Websites\033\\'")

    main()
    os.system("pause")
