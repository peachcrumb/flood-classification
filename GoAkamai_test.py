#####################################################################################################
# Script to save a snapshot from available GoAkamai (http://www.goakamai.org/) traffic cameras on Oahu, HI.
# Last Modified:    1/29/2025 Kayla Yamamoto
#                   4/26/2026  Phoebe Chang
#
#####################################################################################################

import ultralytics
from ultralytics import YOLO
import os, urllib, shutil, glob, requests, datetime
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
model = YOLO("./runs/classify/train/weights/best.pt")

try:
    import zoneinfo  # The zoneinfo module is only available in Python 3.9+
except ImportError:
    from backports import zoneinfo  # Use backports.zoneinfo if necessary

key_timezone = 'Pacific/Honolulu'
timestamp = datetime.datetime.now(tz=zoneinfo.ZoneInfo(key=key_timezone))

# url_weather = '' still figuring this one out....
url_parent = 'http://cctv.cdn.goakamai.org/SnapShot/320x240/'
url_child = {
    # freeway
    "TL-0242": "TL-0242.jpg",  
    "TL-0268": "TL-0268.jpg",    
    "TL-0059": "TL-0059.jpg",
    "TL-0060": "TL-0060.jpg",
    "TL-0349": "TL-0349.jpg",
    "TL-0350": "TL-0350.jpg",
    "TL-0234": "TL-0234.jpg",
    "TL-0235": "TL-0235.jpg",
    "TL-0236": "TL-0236.jpg",
    "TL-0237": "TL-0237.jpg",
    "TL-0269": "TL-0269.jpg",
    "TL-0270": "TL-0270.jpg",
    "TL-0271": "TL-0271.jpg",
    "TL-0054": "TL-0054.jpg",
    "TL-0302": "TL-0302.jpg",
    "TL-0154": "TL-0154.jpg",    
    "TL-0151": "TL-0151.jpg",
    "TL-0152": "TL-0152.jpg",    
    "TL-0196": "TL-0196.jpg",
    "TL-0311": "TL-0311.jpg",    
    "TL-0341": "TL-0341.jpg",
    "TL-0024": "TL-0024.jpg",
    "TL-0326": "TL-0326.jpg",
    "TL-0048": "TL-0048.jpg",
    "TL-0045": "TL-0045.jpg",
    "TL-0051": "TL-0051.jpg",
    "TL-0328": "TL-0328.jpg",
    "TL-0322": "TL-0322.jpg",
    "TL-0323": "TL-0323.jpg",
    "TL-0122": "TL-0122.jpg",
    "TL-0300": "TL-0300.jpg",
    "TL-0305": "TL-0305.jpg",
    "TL-0187": "TL-0187.jpg",
    "TL-0063": "TL-0063.jpg",
    "TL-0057": "TL-0057.jpg",
    "TL-0348": "TL-0348.jpg",
    "TL-0232": "TL-0232.jpg",
    "TL-0233": "TL-0233.jpg",
    "TL-0324": "TL-0324.jpg",

    # mililani
    "TL-0283": "TL-0283.jpg",    
    "TL-0282": "TL-0282.jpg",        
    "TL-0277": "TL-0277.jpg", 
    "TL-0279": "TL-0279.jpg",     
    "TL-0281": "TL-0281.jpg", 
    "TL-0278": "TL-0278.jpg",
    "TL-0280": "TL-0280.jpg",    
    "TL-0285": "TL-0285.jpg",       
    "TL-0284": "TL-0284.jpg",
  
    # aiea/pearl
    "TL-0096": "TL-0096.jpg",
    "TL-0155": "TL-0155.jpg",    
    "TL-0206": "TL-0206.jpg",
    "TL-0204": "TL-0204.jpg",
    "TL-0062": "TL-0062.jpg",  
    "TL-0345": "TL-0345.jpg",
    "TL-0195": "TL-0195.jpg",     
    "TL-0097": "TL-0097.jpg",    
    "TL-0207": "TL-0207.jpg",
    "TL-0094": "TL-0094.jpg",
    "TL-0203": "TL-0203.jpg",
    "TL-0205": "TL-0205.jpg",
    "TL-0189": "TL-0189.jpg",
    "TL-0197": "TL-0197.jpg",
    "TL-0209": "TL-0209.jpg",
    "TL-0039": "TL-0039.jpg",
    "TL-0040": "TL-0040.jpg",
    "TL-0042": "TL-0042.jpg",
    "TL-0124": "TL-0124.jpg",
    "TL-0123": "TL-0123.jpg",
    "TL-0044": "TL-0044.jpg",
    "TL-0343": "TL-0343.jpg",
    "TL-0038": "TL-0038.jpg",
    "TL-0327": "TL-0327.jpg",
    "TL-0188": "TL-0188.jpg",
    "TL-0125": "TL-0125.jpg",

    # kapolei
    "TL-0244": "TL-0244.jpg",
    "TL-0247": "TL-0247.jpg",
    "TL-0246": "TL-0246.jpg",
    "TL-0248": "TL-0248.jpg",
    "TL-0264": "TL-0264.jpg",
    "TL-0262": "TL-0262.jpg",
    "TL-0231": "TL-0231.jpg",
    "TL-0255": "TL-0255.jpg",
    "TL-0258": "TL-0258.jpg",
    "TL-0261": "TL-0261.jpg",
    "TL-0265": "TL-0265.jpg",
    "TL-0331": "TL-0331.jpg",
    "TL-0325": "TL-0325.jpg",
    "TL-0320": "TL-0320.jpg",
    "TL-0041": "TL-0041.jpg",

    # kaneohe
    "TL-0065": "TL-0065.jpg",
    "TL-0066": "TL-0066.jpg", 
    "TL-0089": "TL-0089.jpg",
    "TL-0093": "TL-0093.jpg", 
    "TL-0087": "TL-0087.jpg",
    "TL-0090": "TL-0090.jpg",
    "TL-0118": "TL-0118.jpg",
    "TL-0083": "TL-0083.jpg",  
    "TL-0084": "TL-0084.jpg",    
    "TL-0081": "TL-0081.jpg",
    "TL-0082": "TL-0082.jpg",
    "TL-0088": "TL-0088.jpg",
    "TL-0067": "TL-0067.jpg",
    "TL-0068": "TL-0068.jpg",
    "TL-0009": "TL-0009.jpg",

    # hawaii kai
     "TL-0071": "TL-0071.jpg",       
    
    # honolulu
# waikiki
    "TL-0007": "TL-0007.jpg",
    "TL-0008": "TL-0008.jpg",
    "TL-0218": "TL-0218.jpg",
    "TL-0217": "TL-0217.jpg",
    "TL-0116": "TL-0116.jpg",
    "TL-0077": "TL-0077.jpg",
    "TL-0157": "TL-0157.jpg",
    "TL-0078": "TL-0078.jpg",
    "TL-0080": "TL-0080.jpg",
    "TL-0079": "TL-0079.jpg",
    "TL-0222": "TL-0222.jpg",
    "TL-0202": "TL-0202.jpg",
    "TL-0226": "TL-0226.jpg",
    "TL-0198": "TL-0198.jpg",
# manoa
    "TL-0158": "TL-0158.jpg",
# nuuanu
    "TL-0147": "TL-0147.jpg",
    "TL-0148": "TL-0148.jpg",
    "TL-0149": "TL-0149.jpg",
    "TL-0146": "TL-0146.jpg",  
    "TL-0145": "TL-0145.jpg",
    "TL-0161": "TL-0161.jpg",
    "TL-0150": "TL-0150.jpg",
    "TL-0162": "TL-0162.jpg",
    "TL-0131": "TL-0131.jpg",
    "TL-0276": "TL-0276.jpg",
    "TL-0107": "TL-0107.jpg",
    "TL-0113": "TL-0113.jpg",
    "TL-0112": "TL-0112.jpg",
    "TL-0193": "TL-0193.jpg",
    "TL-0015": "TL-0015.jpg",
    "TL-0010": "TL-0010.jpg",
# kalihi
    "TL-0120": "TL-0120.jpg", 
    "TL-0117": "TL-0117.jpg",
    "TL-0119": "TL-0119.jpg",
    "TL-0121": "TL-0121.jpg",
    "TL-0129": "TL-0129.jpg",
    "TL-0130": "TL-0130.jpg",
    "TL-0137": "TL-0137.jpg",
    "TL-0134": "TL-0134.jpg",
    "TL-0141": "TL-0141.jpg",
    "TL-0144": "TL-0144.jpg",
    "TL-0017": "TL-0017.jpg",
    "TL-0018": "TL-0018.jpg",
    "TL-0019": "TL-0019.jpg",
    "TL-0106": "TL-0106.jpg",
    "TL-0109": "TL-0109.jpg",
    "TL-0111": "TL-0111.jpg",
    "TL-0058": "TL-0058.jpg",
    "TL-0314": "TL-0314.jpg",
    "TL-0227": "TL-0227.jpg",
    "TL-0049": "TL-0049.jpg",
    "TL-0228": "TL-0228.jpg",
# ala moana
    "TL-0100": "TL-0100.jpg",
    "TL-0064": "TL-0064.jpg",
    "TL-0099": "TL-0099.jpg",
    "TL-0102": "TL-0102.jpg",
    "TL-0208": "TL-0208.jpg",
    "TL-0101": "TL-0101.jpg",
    "TL-0272": "TL-0272.jpg",
    "TL-0103": "TL-0103.jpg",
    "TL-0114": "TL-0114.jpg",
    "TL-0016": "TL-0016.jpg",
   "TL-0004": "TL-0004.jpg",
    "TL-0006": "TL-0006.jpg",
    "TL-0002": "TL-0002.jpg",
    "TL-0001": "TL-0001.jpg",
    "TL-0005": "TL-0005.jpg",
    "TL-0105": "TL-0105.jpg",
    "TL-0104": "TL-0104.jpg",
    "TL-0110": "TL-0110.jpg",
    "TL-0273": "TL-0273.jpg",

    # maui
    "TL-0804": "TL-0804.jpg",
# wailuku
    "TL-0827": "TL-0827.jpg",
    "TL-0815": "TL-0815.jpg",
    "TL-0816": "TL-0816.jpg",
    "TL-0817": "TL-0817.jpg",
    "TL-0818": "TL-0818.jpg",
    "TL-0823": "TL-0823.jpg",
    "TL-0824": "TL-0824.jpg",
    "TL-0825": "TL-0825.jpg",
# makawao
    "TL-0801": "TL-0801.jpg",
# lahaina
    "TL-0811": "TL-0811.jpg",
    "TL-0820": "TL-0820.jpg",
    "TL-0806": "TL-0806.jpg",
    "TL-0828": "TL-0828.jpg",
# kihei
    "TL-0810": "TL-0810.jpg",
    "TL-0808": "TL-0808.jpg",
    "TL-0826": "TL-0826.jpg",
    "TL-0809": "TL-0809.jpg",
# kahului
    "TL-0814": "TL-0814.jpg",
    "TL-0803": "TL-0803.jpg",
    "TL-0802": "TL-0802.jpg",
    "TL-0807": "TL-0807.jpg",
    "TL-0812": "TL-0812.jpg",
    "TL-0813": "TL-0813.jpg",

    # misc
    "TL-0027": "TL-0027.jpg",
    "TL-0238": "TL-0238.jpg",
    "TL-0346": "TL-0346.jpg",
    "TL-0115": "TL-0115.jpg",    
    "TL-0200": "TL-0200.jpg",   
    "TL-0011": "TL-0011.jpg",
    "TL-0012": "TL-0012.jpg",
    "TL-0013": "TL-0013.jpg",
    "TL-0014": "TL-0014.jpg",
    "TL-0332": "TL-0332.jpg",
    "TL-0306": "TL-0306.jpg",
    "TL-0309": "TL-0309.jpg",
    "TL-0256": "TL-0256.jpg",
    "TL-0307": "TL-0307.jpg",
    "TL-0308": "TL-0308.jpg",
    "TL-0026": "TL-0026.jpg",
    "TL-0029": "TL-0029.jpg",
    "TL-0030": "TL-0030.jpg",
    "TL-0031": "TL-0031.jpg",
    "TL-0032": "TL-0032.jpg",
    "TL-0033": "TL-0033.jpg",
    "TL-0034": "TL-0034.jpg",
    "TL-0243": "TL-0243.jpg",
    "TL-0168": "TL-0168.jpg",
    "TL-0182": "TL-0182.jpg",
    "TL-0175": "TL-0175.jpg",
    "TL-0176": "TL-0176.jpg",
    "TL-0177": "TL-0177.jpg",
    "TL-0173": "TL-0173.jpg",
    "TL-0174": "TL-0174.jpg",
    "TL-0172": "TL-0172.jpg",
    "TL-0178": "TL-0178.jpg",
    "TL-0185": "TL-0185.jpg",
    "TL-0184": "TL-0184.jpg",
    "TL-0183": "TL-0183.jpg",
    "TL-0170": "TL-0170.jpg",
    "TL-0171": "TL-0171.jpg",
    "TL-0181": "TL-0181.jpg",
    "TL-0169": "TL-0169.jpg",
    "TL-0180": "TL-0180.jpg",
    "TL-0167": "TL-0167.jpg",
    "TL-0186": "TL-0186.jpg",
    "TL-0822": "TL-0822.jpg",
    "TL-0241": "TL-0241.jpg",
    "TL-0239": "TL-0239.jpg",
    "TL-0240": "TL-0240.jpg",
    "TL-0069": "TL-0069.jpg",
    "TL-0070": "TL-0070.jpg",
    "TL-0072": "TL-0072.jpg",
    "TL-0073": "TL-0073.jpg",
    "TL-0074": "TL-0074.jpg",
    "TL-0075": "TL-0075.jpg",
    "TL-0076": "TL-0076.jpg",
    "TL-0219": "TL-0219.jpg",
    "TL-0086": "TL-0086.jpg",
    "TL-0342": "TL-0342.jpg",
    "TL-0340": "TL-0340.jpg",    
    "TL-0260": "TL-0260.jpg",
    "TL-0021": "TL-0021.jpg",
    "TL-0098": "TL-0098.jpg",
    "TL-0263": "TL-0263.jpg",
    "TL-0275": "TL-0275.jpg",
    "TL-0209": "TL-0209.jpg",
    "TL-0339": "TL-0339.jpg",
    "TL-0338": "TL-0338.jpg",
    "TL-0819": "TL-0819.jpg",
    "TL-0135": "TL-0135.jpg",
    "TL-0136": "TL-0136.jpg",
    "TL-0138": "TL-0138.jpg",
    "TL-0805": "TL-0805.jpg",
    "TL-0159": "TL-0159.jpg",
    "TL-0160": "TL-0160.jpg",
    "TL-0163": "TL-0163.jpg",
    "TL-0164": "TL-0164.jpg",
    "TL-0165": "TL-0165.jpg",
    "TL-0166": "TL-0166.jpg"
}
newNames = {
    # freeway
    "TL-0242": "kauka-moaniani.jpg",  
    "TL-0268": "kamehameha-waipahu.jpg",    
    "TL-0059": "h1-waikele-eb.jpg",
    "TL-0060": "h1-waikele-wb.jpg",
    "TL-0349": "h1-nwaikele-eb.jpg",
    "TL-0350": "h1-nwaikele-wb.jpg",
    "TL-0234": "lumiaina-paiwa.jpg",
    "TL-0235": "lumiaina-waikele.jpg",
    "TL-0236": "lumiaina-pulelo.jpg",
    "TL-0237": "lumiaina-lumiauau.jpg",
    "TL-0269": "kamehameha-lumiauau.jpg",
    "TL-0270": "kamehameha-lumiaina.jpg",
    "TL-0271": "kamehameha-waipio.jpg",
    "TL-0054": "h1-saltlk-wb.jpg",
    "TL-0302": "h201-alanapunani.jpg",
    "TL-0154": "saltlk-kahuapaani.jpg",    
    "TL-0151": "saltlk-alalilikoi.jpg",
    "TL-0152": "saltlk-alanapunani.jpg",    
    "TL-0196": "kuala-walmart.jpg",
    "TL-0311": "h1-pearlhb-e.jpg",    
    "TL-0341": "h1v-airport.jpg",
    "TL-0024": "farrington-h1ramp.jpg",
    "TL-0326": "h1-kahuapaani.jpg",
    "TL-0048": "h1-liliha.jpg",
    "TL-0045": "h1-kokohead.jpg",
    "TL-0051": "h1-punahou.jpg",
    "TL-0328": "h1-kinau.jpg",
    "TL-0322": "h1-e-honouliuli-i.jpg",
    "TL-0323": "h1-e-honouliuli-ii.jpg",
    "TL-0122": "h201-shafter.jpg",
    "TL-0300": "h201-puuloa.jpg",
    "TL-0305": "h201-redhill.jpg",
    "TL-0187": "h201-kahuapaani.jpg",
    "TL-0063": "h1-ward.jpg",
    "TL-0057": "h1v-eb.jpg",
    "TL-0348": "h1v-keehi.jpg",
    "TL-0232": "h1i-paiwa-eb-ramp.jpg",
    "TL-0233": "h1i-paiwa-wb-ramp.jpg",
    "TL-0324": "h1-kualakai-wb.jpg",

    # mililani
    "TL-0283": "meheula-interchange-s-ii.jpg",    
    "TL-0282": "meheula-interchange-s-i.jpg",        
    "TL-0277": "meheula-makaikai.jpg", 
    "TL-0279": "meheula-kaapeha.jpg",     
    "TL-0281": "meheula-kuaoa.jpg", 
    "TL-0278": "meheula-koolani.jpg",
    "TL-0280": "meheula-lehiwa.jpg",    
    "TL-0285": "meheula-ainamakua.jpg",       
    "TL-0284": "meheula-interchange-n.jpg",
  
    # aiea/pearl
    "TL-0096": "kam-waimano.jpg",
    "TL-0155": "kam-saltlk.jpg",    
    "TL-0206": "kam-ford.jpg",
    "TL-0204": "kam-puuponi.jpg",
    "TL-0062": "h1-waimalu-eb.jpg",  
    "TL-0345": "kamehameha-radford-eb.jpg",
    "TL-0195": "kuala-acacia.jpg",     
    "TL-0097": "kamehameha-halawa-eb.jpg",    
    "TL-0207": "kamehameha-center-wb.jpg",
    "TL-0094": "kam-kaahumanu.jpg",
    "TL-0203": "kam-kaahumanu-ii.jpg",
    "TL-0205": "kam-palimomi.jpg",
    "TL-0189": "kamehameha-honomanu.jpg",
    "TL-0197": "kuala-makolu.jpg",
    "TL-0209": "kuala-kaakepa.jpg",
    "TL-0039": "h1-h2-merge-eb.jpg",
    "TL-0040": "h1-h2-merge-wb.jpg",
    "TL-0042": "h1-kaahumanu-wb.jpg",
    "TL-0124": "moanalua-honomanu.jpg",
    "TL-0123": "moanalua-aieaht.jpg",
    "TL-0044": "h1-kaonohi-wb.jpg",
    "TL-0343": "h1-kaamilo.jpg",
    "TL-0038": "h1-aiea-overpass.jpg",
    "TL-0327": "h1-kaimakani.jpg",
    "TL-0188": "h201-halawa.jpg",
    "TL-0125": "moanalua-kaahumanu.jpg",

    # kapolei
    "TL-0263": "kapolei-kamokila-ii.jpg",    
    "TL-0244": "kapolei-renton.jpg",
    "TL-0247": "kapolei-kamaaha.jpg",
    "TL-0246": "kapolei-kualakai-ii.jpg",
    "TL-0248": "kapolei-maluohi.jpg",
    "TL-0264": "farrington-kualakaip.jpg",
    "TL-0262": "kapolei-kamokila-i.jpg",
    "TL-0231": "kapolei-kalaeloa.jpg",
    "TL-0255": "farrington-kealanani.jpg",
    "TL-0258": "kamokila-oldfarrington.jpg",
    "TL-0261": "kamokila-uluohia.jpg",
    "TL-0265": "kualakai-ramps.jpg",
    "TL-0331": "h1-kualakai-sign.jpg",
    "TL-0325": "h1-kualakai-eb.jpg",
    "TL-0320": "h1-kalaeloa-wb.jpg",
    "TL-0041": "h1-kaahumanu-eb.jpg",

    # kaneohe
    "TL-0086": "kam-lilipuna-haiku.jpg",    
    "TL-0065": "kahekili-haiku.jpg",
    "TL-0066": "kahekili-kahuhipa.jpg", 
    "TL-0089": "kam-mokulele.jpg",
    "TL-0093": "kam-offramp-eb.jpg", 
    "TL-0087": "kam-lilipuna-kahuhipa.jpg",
    "TL-0090": "kam-henry-keaahala.jpg",
    "TL-0118": "likelike-kahekili.jpg",
    "TL-0083": "kam-kaneohe-likelike-ii.jpg",  
    "TL-0084": "kam-keole.jpg",    
    "TL-0081": "kam-halaulani.jpg",
    "TL-0082": "kam-kaneohe-likelike.jpg",
    "TL-0088": "kam-luluku.jpg",
    "TL-0067": "kahekili-keaahala.jpg",
    "TL-0068": "kahekili-kulukeoe.jpg",
    "TL-0009": "haiku-alaloa.jpg",

    # hawaii kai
     "TL-0071": "kal-hawaiikai.jpg",       
    
    # honolulu
# waikiki
    "TL-0007": "alawai-kanekapolei.jpg",
    "TL-0008": "alawai-mccully.jpg",
    "TL-0218": "kalakaua-alawai.jpg",
    "TL-0217": "alawai-kapahulu.jpg",
    "TL-0116": "kuhio-kaiulani.jpg",
    "TL-0077": "kalakaua-kaiulani.jpg",
    "TL-0157": "saratoga-kalia.jpg",
    "TL-0078": "kalakaua-kapahulu.jpg",
    "TL-0080": "kalakaua-lewers.jpg",
    "TL-0079": "kalakaua-kuhio.jpg",
    "TL-0222": "kalakaua-beachwalk.jpg",
    "TL-0202": "kuhio-kapahulu.jpg",
    "TL-0226": "alamoana-hobron.jpg",
    "TL-0198": "alamoana-kahanamoku.jpg",
# manoa
    "TL-0158": "university-dole.jpg",
# nuuanu
    "TL-0147": "pali-laimi.jpg",
    "TL-0148": "pali-waokanaka.jpg",
    "TL-0149": "pali-puiwa.jpg",
    "TL-0146": "pali-jack.jpg",  
    "TL-0145": "pali-offramp.jpg",
    "TL-0161": "vineyard-pali.jpg",
    "TL-0150": "queen-punchbowl.jpg",
    "TL-0162": "vineyard-punchbowl.jpg",
    "TL-0131": "nimitz-alakawa.jpg",
    "TL-0276": "nimitz-nuuanu.jpg",
    "TL-0107": "king-bishop.jpg",
    "TL-0113": "king-punchbowl.jpg",
    "TL-0112": "king-maunakea.jpg",
    "TL-0193": "alakea-hotel.jpg",
    "TL-0015": "beretania-punchbowl.jpg",
    "TL-0010": "beretania-bishop.jpg",
# kalihi
    "TL-0120": "likelike-kulakolea.jpg", 
    "TL-0117": "likelike-anoi.jpg",
    "TL-0119": "likelike-kam-iv.jpg",
    "TL-0121": "likelike-school.jpg",
    "TL-0129": "nimitz-alakawa-i.jpg",
    "TL-0130": "nimitz-alakawa-ii.jpg",
    "TL-0137": "nimitz-pacific-eb.jpg",
    "TL-0134": "nimitz-kalihi.jpg",
    "TL-0141": "nimitz-sandisle.jpg",
    "TL-0144": "nimitz-waiakamilo.jpg",
    "TL-0017": "dillingham-alakawa.jpg",
    "TL-0018": "dillingham-kalihi.jpg",
    "TL-0019": "dillingham-middle.jpg",
    "TL-0106": "king-beretania.jpg",
    "TL-0109": "king-houghtailing.jpg",
    "TL-0111": "king-kalihi.jpg",
    "TL-0058": "h1-vineyard-ramp.jpg",
    "TL-0314": "h1-ola.jpg",
    "TL-0227": "h1-houghtailing.jpg",
    "TL-0049": "h1-middlest.jpg",
    "TL-0228": "h1-middle.jpg",
# ala moana
    "TL-0100": "kapiolani-kalakaua.jpg",
    "TL-0064": "convention-center.jpg",
    "TL-0099": "kapiolani-date.jpg",
    "TL-0102": "kapiolani-mccully.jpg",
    "TL-0208": "kapiolani-atkinson.jpg",
    "TL-0101": "kapiolani-keeamoku.jpg",
    "TL-0272": "kapiolani-pensacola.jpg",
    "TL-0103": "kapiolani-ward.jpg",
    "TL-0114": "king-south-kapiolani.jpg",
    "TL-0016": "beretania-ward.jpg",
    "TL-0004": "alamoana-kamakee.jpg",
    "TL-0006": "alamoana-ward.jpg",
    "TL-0002": "alamoana-atkinson.jpg",
    "TL-0001": "alamoana-alamakai.jpg",
    "TL-0005": "alamoana-piikoi.jpg",
    "TL-0105": "keeamoku-rycroft-ii.jpg",
    "TL-0104": "keeamoku-rycroft-i.jpg",
    "TL-0110": "king-kalakaua.jpg",
    "TL-0273": "king-pensacola.jpg",

    # maui
    "TL-0804": "hana-baldwin.jpg",
# wailuku
    "TL-0827": "main-church.jpg",
    "TL-0815": "kehalani-honoapiilani.jpg",
    "TL-0816": "kuikahi-honoapiilani.jpg",
    "TL-0819": "kuihelani-honoapiilani.jpg",    
    "TL-0817": "pilikana.jpg",
    "TL-0818": "waiko.jpg",
    "TL-0823": "wahinepio.jpg",
    "TL-0824": "kanaloa-kahului.jpg",
    "TL-0825": "waiehu-kahului.jpg",
# makawao
    "TL-0801": "haleakala-kula-old.jpg",
# lahaina
    "TL-0811": "lahaina-kaiheleku.jpg",
    "TL-0820": "hokiokio-honoapiilani.jpg",
    "TL-0806": "honoapiilani-keawe.jpg",
    "TL-0828": "honoapiilani-leialii.jpg",
# kihei
    "TL-0810": "lipoa.jpg",
    "TL-0808": "piilani-nkihei.jpg",
    "TL-0805": "nkihei-honoapiilani.jpg",    
    "TL-0826": "okolani-mikioi.jpg",
    "TL-0809": "piikea.jpg",
# kahului
    "TL-0814": "hana-dairy.jpg",
    "TL-0803": "hana-haleakala.jpg",
    "TL-0802": "hana-cravalho.jpg",
    "TL-0807": "kaahumanu-kahului.jpg",
    "TL-0812": "cravalho-dairy-pakaula.jpg",
    "TL-0813": "kuihelani-cravalho-puunene.jpg",

    # misc
    "TL-0027": "farrington-paiwa.jpg",
    "TL-0238": "kamehameha-kauka.jpg",
    "TL-0346": "kamehameha-radford-wb.jpg",
    "TL-0115": "king-university.jpg",    
    "TL-0200": "alawai-seaside.jpg",   
    "TL-0011": "beretania-keeamoku.jpg",
    "TL-0012": "beretania-mccully.jpg",
    "TL-0013": "beretania-piikoi.jpg",
    "TL-0014": "beretania-punahou.jpg",
    "TL-0332": "farrington-auyong.jpg",
    "TL-0306": "farrington-haleakala.jpg",
    "TL-0309": "farrington-helelua.jpg",
    "TL-0256": "farrington-makakilo-barrette-i.jpg",
    "TL-0307": "farrington-nanakulia.jpg",
    "TL-0308": "farrington-nanakuliv.jpg",
    "TL-0026": "farrington-leoku.jpg",
    "TL-0029": "farrington-waipahu-dpt.jpg",
    "TL-0030": "weaver-aawa.jpg",
    "TL-0031": "weaver-familysvc.jpg",
    "TL-0032": "weaver-geiger.jpg",
    "TL-0033": "weaver-kolowaka.jpg",
    "TL-0034": "weaver-laulaunui.jpg",
    "TL-0243": "h2-interchange-nb-kauka.jpg",
    "TL-0168": "h3-haiku-portal-hb.jpg",
    "TL-0182": "h3-haiku-valley.jpg",
    "TL-0175": "h3-halawa-interchange.jpg",
    "TL-0176": "h3-halawa-portal-hb.jpg",
    "TL-0177": "h3-halawa-portal-kb.jpg",
    "TL-0173": "h3-halawa-approach-kb.jpg",
    "TL-0174": "h3-halawa-valley.jpg",
    "TL-0172": "h3-halawa-escape.jpg",
    "TL-0178": "h3-halekou-interchange.jpg",
    "TL-0185": "h3-rock-tunnel.jpg",
    "TL-0184": "h3-likelike-overpass.jpg",
    "TL-0183": "h3-n-haiku-valley.jpg",
    "TL-0170": "h3-n-halawa-valley.jpg",
    "TL-0171": "h3-n-halawa-interchange.jpg",
    "TL-0181": "h3-s-haiku-valley.jpg",
    "TL-0169": "h3-s-halawa-valley.jpg",
    "TL-0180": "h3-s-halekou.jpg",
    "TL-0167": "h3-viaduct-eb.jpg",
    "TL-0186": "h3-kahuapaani.jpg",
    "TL-0822": "haleakala-makawao.jpg",
    "TL-0241": "kauka-ukee-n.jpg",
    "TL-0239": "kauka-ukee-s.jpg",
    "TL-0240": "kauka-waipio.jpg",
    "TL-0069": "kal-ainakoa.jpg",
    "TL-0070": "kal-ehalemaumau.jpg",
    "TL-0072": "kal-keahole.jpg",
    "TL-0073": "kal-kuliouou.jpg",
    "TL-0074": "kal-laukahi.jpg",
    "TL-0075": "kal-puuikena.jpg",
    "TL-0076": "kal-hind-west.jpg",
    "TL-0219": "kalakaua-alamoana.jpg",
    "TL-0342": "kamehameha-kalaloa-eb.jpg",
    "TL-0340": "kamehameha-pupukea.jpg",    
    "TL-0260": "kamokila-wakea.jpg",
    "TL-0021": "kapahulu-date.jpg",
    "TL-0098": "kapahulu-olu.jpg",
    "TL-0275": "king-victoria.jpg",
    "TL-0339": "kualakai-offramp-wb.jpg",
    "TL-0338": "kuhio-seaside.jpg",
    "TL-0135": "nimitz-ohohia-eb.jpg",
    "TL-0136": "nimitz-ohohia-wb.jpg",
    "TL-0138": "nimitz-pacific-wb.jpg",
    "TL-0159": "vineyard-liliha.jpg",
    "TL-0160": "vineyard-palama.jpg",
    "TL-0163": "waialae-ninth.jpg",
    "TL-0164": "waialae-kokohead.jpg",
    "TL-0165": "waialae-palolo.jpg",
    "TL-0166": "ward-kinau.jpg"
}

path_unavailable = 'UNAVAILABLE.jpg'

def compare_snapshots(imageA, imageB):
    A = list(Image.open(imageA, 'r').convert('RGB').getdata())
    B = list(Image.open(imageB, 'r').convert('RGB').getdata())
    if len(A) != len(B):
        return -1
    
    diff = [A[i][0] != B[i][0] or A[i][1] != B[i][1] or A[i][2] != B[i][2] for i in range(len(A))]
    return sum(diff) / len(diff)

def download_snapshots(url_parent, url_child, path_unavailable, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now(tz=zoneinfo.ZoneInfo(key=key_timezone))

    base_save_path = "./live_cams"
    os.makedirs(base_save_path, exist_ok=True)
    res = 0
    
    for key, elem in url_child.items():
#        key = "livestream-snapshots" + key
        
        # Try the URL without query parameters first
        url = f"{url_parent}{elem}"
        naming = newNames[key]
        filename = f"{os.path.splitext(naming)[0]}-{timestamp.strftime('%Y%m%dT%H%M%S')}.jpg"
        save_path = os.path.join(base_save_path, filename)
        
        n = 0
        req = None
        while n < 10:
            try:
                req = requests.get(url, stream=True, timeout=10)
                if req.status_code == 200:
                    break
                else:
                    n += 1
            except requests.RequestException:
                n += 1
        
        # If the first request fails, try again with the dynamic query parameter
        if req is None or req.status_code != 200:
            query_param = int(datetime.datetime.now().timestamp() * 1000)
            url = f"{url_parent}{elem}?icx={query_param}"
            n = 0
            while n < 10:
                try:
                    req = requests.get(url, stream=True, timeout=10)
                    if req.status_code == 200:
                        break
                except requests.RequestException:
                    n += 1
        
        if req is None or req.status_code != 200:
            print(f'ERROR at download_snapshots: Unable to retrieve {key}')
            continue

        temp_path = save_path + ".tmp"
        
        with open(temp_path, 'wb') as f:
            for chunk in req.iter_content():
                f.write(chunk)
        os.replace(temp_path, save_path)
        
        # png_path = os.path.join(base_save_path, f"{os.path.splitext(elem)[0]}-{timestamp.strftime('%Y%m%dT%H%M%S')}.png")
        # newpng = Image.open(save_path).save(png_path)
        
        current_image = Image.open(save_path)
        result = model.predict(source=save_path, save=True)
        index = result[0].probs.top1
        label = result[0].names[index]
        confidence = result[0].probs.top1conf
        print(f"{label} {confidence}\n")
        
        if path_unavailable is not None:
            print(f"{key}: {label} ({confidence:.2f})")
            if (compare_snapshots(save_path, path_unavailable) == 0) or (os.path.getsize(save_path) <= 11841) or (label != 'flood'):
                os.remove(save_path)
               # os.remove(png_path)
                continue
            else:
                e_data = current_image.getexif()
                e_data[270] = f"{confidence}"
                current_image.save(save_path,exif=e_data)

        
    return res


res = download_snapshots(url_parent, url_child, path_unavailable=path_unavailable, timestamp=timestamp)




