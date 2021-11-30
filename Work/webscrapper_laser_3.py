import requests
from datetime import datetime
import re
import traceback
import laser_temperature




import subprocess, platform

'''boiler Plate'''
if platform.system()=="Windows":
    subprocess.Popen("cls", shell=True).communicate() 
    #I like to use this instead of subprocess.call since for multi-word commands you can just type it data, granted this is just cls and subprocess.call should work fine 
else: #Linux and Mac
    print("\033c", end="")



    '''testing laser string'''
laserhtml = ('<html>\r\n<head>\r\n<title>Scanner</title>\r\n<div align="center">\r\n<table border="2" id="table5" cellspacing="0" bordercolor="#FFFFFF" bgcolor="#99CCFF">\r\n\t\t<td colspan="2" align="center" bgcolor="#6699CC"><b>Version info</b></td>\r\n\t\t<td rowspan="5" bgcolor="#E0E0E0" align="center">\r\n<img src="SC3L.jpg"</p></td></tr><tr>\r\n\t\t<td>Firmware</td>\r\n\t\t<td><b> 5a13.665.X.836</b></td></tr><tr>\r\n\t\t<td>Serial number</td>\r\n\t\t<td><b> 0319761</b></td>\r\n\t\t</tr></td></tr><tr>\r\n\t\t<td>MAC</td>\r\n\t\t<td><b> 00:08:DC:04:E1:11&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; </b></td></tr><tr>\r\n\t\t<td bgcolor="#6699CC" colspan="2">\r\n\t\t<p align="center"><b>Default settings</b></td></tr><tr>\r\n\t\t<td align="left">\r\n\t\t<p>IP-adress</td>\r\n\t\t<td align="left">\r\n\t\t<b> 192.168.001.245</b></td>\r\n\t\t<td rowspan="9" bgcolor="#E0E0E0" align="center"><form action="http://10.10.10.40/Daten_flash">\r\n\t\t\t\t  <div align="center">\r\n\t\t\t\t  <table border="0" cellpadding="4" cellspacing="0" bgcolor="#E0E0E0" height="200">\r\n\t\t\t\t    <tr>\r\n\t\t\t\t      <td align="right">IP-adress</td><td>\r\n\t\t\t\t\t\t<input name="IP" type="text" size="14" value="010.010.010.040" maxlength="30"> Port \r\n\t\t\t\t\t\t<input name="PORT" type="text" size="5" value="01096" maxlength="40"></td></tr> <tr>\r\n\t\t\t\t      <td align="right">SubNetMask</td><td>\r\n\t\t\t\t\t\t<input name="SNM" type="text" size="14" value="255.255.255.000" maxlength="40"></td></tr><tr>\r\n\t\t\t\t      <td align="right">Data rate 10Mbit/s</td>\r\n\t\t\t\t      <td>\r\n\t\t\t\t\t\t<input type="checkbox" name="DATARATE" value="10" 10MBit ></td></tr><tr>\r\n\t\t\t\t      <td align="right">Password</td><td>\r\n\t\t\t\t\t\t<input name="PASSWORD" type="password" size="30" maxlength="25"></td></tr><tr>\r\n\t\t\t\t      <td align="center" colspan="2">\r\n\t\t\t\t\t\t<input type="submit" value=" Change settings"></td></tr>\r\n\t\t\t\t  </table>\r\n</div></form><tr>\r\n<td>Port</td>\r\n<td><b> 01096</b></td></tr><tr>\r\n<td>SubNetMask</td>\r\n<td><b> 255.255.255.000</b></td></tr><tr>\r\n<td bgcolor="#6699CC" colspan="2">\r\n<p align="center"><b>Working settings</b></td></tr><tr><td>\r\n<p align="left">IP-adress</td>\r\n<td><b>010.010.010.040</b></td></tr><tr>\r\n<td align="left">Port</td>\r\n<td align="left"> <b>01096</b></td></tr><tr>\r\n<td align="left">SubNetMask</td>\r\n<td align="left"><b> 255.255.255.000</b></td></tr><tr>\r\n<td align="left">Scanner connected to</td>\r\n<td align="left">\r\n<b> 000.000.000.000</b></td></tr><tr>\r\n<td bgcolor="#99CCFF" align="left">\r\n<p>Data rate</td>\r\n<td bgcolor="#99CCFF" align="left">\r\n<b> 100Mbit/s</b></td></tr><tr>\r\n<td align="left" colspan="2" bgcolor="#6699CC">\r\n<p align="center"><b>Scanner parameter</b></td>\r\n<td rowspan="17" bgcolor="#E0E0E0" align="center"><img src="ScanProfile.bmp"</p></td></tr><tr>\r\n<td align="left">Power on hours count</td>\r\n<td align="left">\r\n<b> 2464 hour 01 min 34 sec</b></td></tr><tr>\r\n<td>Laser on time &gt; 35°C</td>\r\n<td>\r\n<b> 0 hour 00 min 32 sec</b></td></tr><tr>\r\n<td>Power cycles count</td>\r\n<td><b> 461</b></td></tr><tr>\r\n<td>Sensor head temp</td>\r\n<td><b> + 17°C </b></td></tr><tr>\r\n<td height="24">Encoder</td>\r\n<td height="24"><b> - 1</b></td></tr><tr>\r\n<td>Standoff&nbsp; </td>\r\n<td><b> 55 mm</b></td></tr><tr>\r\n<td>Range z</td>\r\n<td><b> 20 mm</b></td></tr><tr>\r\n<td>Range x beginn&nbsp; </td>\r\n<td><b> 10 mm</b></td></tr><tr>\r\n<td>Range x end </td>\r\n<td><b> 13 mm</b></td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr><tr>\r\n<td>&nbsp;</td>\r\n<td>&nbsp;</td></tr></table>\r\n</div>\r\n</html>')
START_TIME = ''


def getTime():
    time = (datetime.now())
    timeTrun = ("%s:%s:%s" % (time.hour, time.minute,time.second))
    return timeTrun


def startTimer():
    start_time = getTime()
    timer = start_time-getTime()
    return timer

def getLaserDataRaw():
    try:
        laserUrl = requests.get("http://10.10.10.40/",timeout=5,headers={"User-Agent":"Mozilla/5.0"})
        htmltext = (laserUrl.text)
    except requests.exceptions.ConnectTimeout as e:
       print(f'Connection Timeout')
       htmltext = laserhtml #offline test string
    except Exception:
        traceback.print_exc()
        
         
    temp = getLaserParams(htmltext)
    return temp


def rawBytesToList(data):
    
    TAG_RE0 = re.compile(r'<[^>]+>')
    TAG_RE1 = re.compile('&.*?;+')
    TAG_RE2 = re.compile('\r\n+')
    TAG_RE3 = re.compile('\t+') # replace multiple tabs with one space
    TAG_RE4 = re.compile(' +') # replace multiple spaces with one space
    
    
    data =  TAG_RE0.sub(' ', data)
    data =  TAG_RE1.sub(' ', data)
    data =  TAG_RE2.sub(' ', data)
    data =  TAG_RE3.sub(' ', data)
    data =  TAG_RE4.sub(' ', data)

    data = data.split()
    #print(repr(data))
    return data    

def getLaserParams(data):
    p_dict = {}
    params = rawBytesToList(data)
    #for i in  range(len(params)): print(f'{i=} {params[i]}') # pint all params
    

    p_dict['Firmware'] = params[4]
    p_dict['Serial'] = params[7]
    p_dict['Connected to'] = params[36]
    p_dict['laser on time'] = ''.join(params[48:52])
    p_dict['Temp'] = params[70]
    return p_dict['Temp'] 
    
    #for k, v in p_dict.items():print(k, v)  # print all dict keys


import time
import csv
FILENAME = 'C:/Users/Alex/Downloads/laser.csv'
header = ['Time', 'Temp' ]


with open(FILENAME, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    
    writer.writerow(header)

    # write the data
    
count = 0
while True:
    #getLaserDataRaw()
    with open(FILENAME, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        data = [getTime(),getLaserDataRaw()]
        print(f'{getTime()} : {getLaserDataRaw()} - {count} minutes passed ')
        writer.writerow(data)
        time.sleep(30) # Delay for 1 minute (60 seconds).
        count+= 0.5
        #print(f'working')



print(f'finished')