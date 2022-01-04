
# APi updated on 29/07/2021 

from flask import Flask, request,jsonify,render_template
import requests
import json
import time
import os
import re
import subprocess


url = "http://localhost/cgi-bin/luci/rpc/auth"

payload = json.dumps({
  "id": 1,
  "method": "login",
  "params": [
    "root",
    "openwrt"
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

x = response.text
token = json.loads(x)
token_no = token['result']
rpc_url = "http://localhost/cgi-bin/luci/rpc/sys?auth=" + token_no


#>>>>>>>>>>>>>>>>>>>>>>>>>2nd Ip>>>>>>>>>>>>>>>>>>>>>>>>>>>
try:
  url2 = "http://10.147.17.116/cgi-bin/luci/rpc/auth"

  payload = json.dumps({
    "id": 1,
    "method": "login",
    "params": [
      "root",
      "openwrt"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url2, headers=headers, data=payload)

  x = response.text
  token = json.loads(x)
  token_no = token['result']

  rpc_url2 = "http://10.147.17.116/cgi-bin/luci/rpc/sys?auth=" + token_no
except:
  pass

#>>>>>>>>>>>>>>>>>>>>>>>>>2nd Ip Ends>>>>>>>>>>>>>>>>>>>?


app = Flask(__name__)

@app.route('/dashboard')
@app.route('/wan')
@app.route('/lan')
@app.route('/speedboost')
@app.route('/speedtest')
@app.route('/wirelesssettings')
@app.route('/vpnsettings')
@app.route('/networkstorage')
@app.route('/parentalcontrol')
@app.route('/loadbalancer')
@app.route('/payments')
@app.route('/')
def my_index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])

def api():
    return {
        "id": 1,
        "title": "ARCA Router",
        "completed": True

    }

# >>>>>>>>>>>>>DashBoard>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# For Internet DATA

@app.route('/dongles')

def dongle_con():

    url = rpc_url
    count = 0
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth1"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth2"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth3"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth4"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth5"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth6"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.wlan0"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      count = count + 1
    else:
      count = count  
    return {
      "id":1,
      "result": count,
      "error": "null"
    }



# For LAN Connected(device connected)

@app.route('/devicecon')

def device_con():

    try:
      url = rpc_url2
    except:
      url = rpc_url
      
    payload = json.dumps({ 
        "id": 1, 
        "method": "exec", 
        "params":[ 
		      "cat /tmp/dhcp.leases " 

	      ] 

      })
    headers = {
        'Content-Type': 'application/json',
      }

    response = requests.request("POST", url, headers=headers, data=payload)

    x =response.text
    data_res = json.loads(x)

    x =data_res['result']

    y=x.split("=")
  
    data=y[0]

    z=data.split(" ")
    pattern = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    newlist = list(filter(pattern.match, z))
    count=len(newlist)
    if count>0:
        status = True
    else:
        status = False
    return {
        "id":2,
        "result": count,
        "status":status,
        "error": "null"
      }
    


@app.route('/linestatus')

def con_line():

    url = rpc_url

    payload = json.dumps({ 

  "id": 1, 

  "method": "exec", 

  "params":[ 

		"uci show system.custom.internet " 

	] 

})
    headers = {
      'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    x =response.text
    data_res = json.loads(x)

    x=data_res['result'].split(".")
    y = x[2]
    z = y.split("=")
    linestatus =(z[1])
    
    if linestatus == "'0'\n" :
        status = False
    else:
        status = True
    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)

# For Model and Versions

@app.route('/version')
def kernal_version():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "cat /app/api/version.json"
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'Cookie': 'sysauth=31b76816f5935be36094fa92db1744c2'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


    x=(response.text)
    data = json.loads(x)
    data = data['result']
    res = json.loads(data)
    fresult = {
        "id":3,
        "result":res,
        "error": None
    }
    return(fresult)


#>>>>>>>>>>OverVIEW>>>>>>>>>>>>>>>

#////VPN Status///////////

@app.route('/vpnstatus')

def vpn_status():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.vpn.vpn"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    x=(response.text)
    data = json.loads(x)
    
    x=data['result'].split(".")
    y = x[2]
    z = y.split("=")
    vpnstatus =(z[1])
    
    if vpnstatus == "'0'\n" :
        status = False
    else:
        status = True

    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)

#>>>>>VPN Status Ends>>>>>>>>>

#/////Parental Control//////
@app.route('/parentstatus')

def parent_status():

    url = rpc_url

    payload = json.dumps({ 

  "id": 1, 

  "method": "exec", 

  "params":[ 

		"uci show system.pc.parental " 

	] 

})
    headers = {
      'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    x =response.text
    data_res = json.loads(x)

    x=data_res['result'].split(".")
    y = x[2]
    z = y.split("=")
    pstatus =(z[1])
    
    if pstatus == "'0'\n" :
        status = False
    else:
        status = True
    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)


#>>>>Parental Control Ends>>>>>


#////SpeedBoost Status////////////
@app.route('/speedbooststatus')

def speedboost_status():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.custom.speedboost"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    x=(response.text)
    data = json.loads(x)
    
    x=data['result'].split(".")
    y = x[2]
    z = y.split("=")
    speedbooststatus =(z[1])
    
    if speedbooststatus == "'0'\n" :
        status = False
    else:
        status = True

    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)

#>>>>Speed boost status ends>>>>>>>



#>>>>OVerView Ends>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>DASH BOARD PAGE OVER>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>SpeedTest Page>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# For Download Speed Test

@app.route('/downloadtest')

def download_test():

  start_timer = time.time()


  url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/wlan0/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          wlan0 = 0
  else:
          wlan0 = float(dresult)
   
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth1/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth1 = 0
  else:
          eth1 = float(dresult)
    
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth3/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth3 = 0
  else:
          eth3 = float(dresult)

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth2/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth2new = 0
  else:
          eth2new = float(dresult)
    
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth4/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth4 = 0
  else:
          eth4 = float(dresult)
    
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth5/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth5 = 0
  else:
          eth5 = float(dresult)
  #Eth6>>>>>>>>
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth6/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth6 = 0
  else:
          eth6 = float(dresult)

  start_download_time=time.time()
  os.system("wget  -O /dev/null http://65.0.164.107/5MB.zip 2>&1   |grep -o '[0-9.]\+ [KM]*B/s'")
  end_download_time = time.time()
  if(end_download_time-start_download_time>60):
      print("Speed is too Slow Try it again")
  else:
      stop_timer=time.time()
    
  diff_time= stop_timer - start_timer

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/wlan0/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          wlan02 = 0
  else:
          wlan02 = float(dresult)
  

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth1/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth12 = 0
  else:
          eth12 = float(dresult)
    
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth3/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth32 = 0
  else:
          eth32 = float(dresult)

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth2/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth22new = 0
  else:
          eth22new = float(dresult)
  
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth4/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth42 = 0
  else:
          eth42 = float(dresult)
    
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth5/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth52 = 0
  else:
          eth52 = float(dresult)
  #Eth6>>>>>>>>>>>>
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /sys/class/net/eth6/statistics/rx_bytes"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = response.text
  data = json.loads(x)
  data = json.loads(x)
  dresult= data['result']
  if dresult == '':
          eth62 = 0
  else:
          eth62 = float(dresult)
  
  wlan0_diff_bytes = wlan02 - wlan0
  eth3_diff_bytes = eth32 - eth3
  eth1_diff_bytes = eth12 - eth1
  eth2_diff_bytes = eth22new -eth2new
  eth4_diff_bytes = eth42 - eth4
  eth5_diff_bytes = eth52 - eth5
  eth6_diff_bytes = eth62 - eth6
  
  speed_wlan0 = ((wlan0_diff_bytes * 8)/1000000)/diff_time
  speed_wlan0=round(speed_wlan0,2)


  speed_eth3 = ((eth3_diff_bytes * 8)/1000000)/diff_time
  speed_eth3=round(speed_eth3,2)


  speed_eth1 = ((eth1_diff_bytes * 8)/1000000)/diff_time
  speed_eth1=round(speed_eth1,2)


  speed_eth2= ((eth2_diff_bytes *8)/1000000)/diff_time
  speed_eth2=round(speed_eth2,2)


  speed_eth4 = ((eth4_diff_bytes *8)/1000000)/diff_time
  speed_eth4 = round(speed_eth4,2)

  speed_eth5 = ((eth5_diff_bytes * 8)/1000000)/diff_time
  speed_eth5=round(speed_eth5,2)
  #eth6>>>>
  speed_eth6 = ((eth6_diff_bytes * 8)/1000000)/diff_time
  speed_eth6=round(speed_eth6,2)
  
  

  #aggregate speed calculation

  payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.custom.speedboost"
      ]
    })
  headers = {
      'Content-Type': 'application/json'
    }
  response = requests.request("POST", url, headers=headers, data=payload)
    
  x=(response.text)
  data = json.loads(x)
    
  x=data['result'].split(".")
  y = x[2]
  z = y.split("=")
  speedbooststatus =(z[1])
  agg_speed=0
  try:  
    if speedbooststatus == "'1'\n" :
        agg_speed = (speed_eth1 + speed_eth2 + speed_eth3 + speed_eth4 + speed_eth5 + speed_eth6 + speed_wlan0)
    else:
        try:
          proc = subprocess.Popen(["wget  -O /dev/null http://65.0.164.107/5MB.zip 2>&1   |grep -o '[0-9.]\+ [KM]*B/s'"], stdout=subprocess.PIPE, shell=True)
          (out, err) = proc.communicate()
          x = out.decode("utf-8").split()
          y = float(x[0])
          z = x[1]
          if z == "MB/s":
            agg_speed = round(y*8,2)
          else :
            agg_speed = round((y/1000)*8,2)
            agg_speed = max(speed_eth1,speed_eth2,speed_eth3,speed_eth4,speed_eth5,speed_eth6,speed_wlan0)

        except:
          pass
          agg_speed = max(speed_eth1,speed_eth2,speed_eth3,speed_eth4,speed_eth5,speed_eth6,speed_wlan0)
  except:
    pass
  
  speed_final = {
    "id":1,
    "result":[{"eth4":speed_eth4,"eth3":speed_eth3,"eth1":speed_eth1,"wlan0":speed_wlan0,"eth2":speed_eth2,"eth5":speed_eth5,"eth6":speed_eth6,"eth7":0,"aggregate":agg_speed}],
    "error":None
  }

  return(speed_final)


# For Upload Speed

@app.route('/uploadtest')

def upload_test():

  

  speed_final = {
    "id":2,
    "result":[{"eth4":0,"eth3":0,"eth1":0,"wlan0":0,"eth2":0,"eth5":0,"eth6":0,"eth7":0,"aggregate":0}],
    "error":None
  }

  return(speed_final)

#>>>>>>>>>>>>>> SPEEDTEST PAGE ENDS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>>>>> WIRELESS PAGE STARTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/edithotspot', methods=['POST'])
def edithotspot():
  data = request.get_json()
  ssid=data['ssid']
  security=data['security']
  hotspotpassword=data['hotspotpassword']
  #print(ssid)
  #print(security)
  #print(hotspotpassword)
  #print(data)
  return(data)


@app.route('/wifipassword', methods=['POST'])
def wifipass():
  data2 = request.json()
  #networkname=data['networkName']
  #security=data['securityMode']
  #password=data['password']
  #print(networkname)
  #print(security)
  #print(password)
  print(type(data2))
  return(data2)

#>>>>>>>>>>>>>>>>>>>>> WIRELESS PAGE ENDS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>>For VPN SETTINGS PAGE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/addvpn', methods=['POST'])
def add_vpn():
  data = request.get_json()
  
  #print(data)
  return(data)



@app.route('/editupload', methods=['POST'])
def edit_upload():
  try:
    data = request.files['card1']
    y = data.filename
    y = y.split(".")
    y = y[1]
    if(y=='ovpn'):
      data.filename = "vpn1.ovpn"
      data.save(data.filename)
      status = "Upload Successfull"
    else:
      status = "Invalid File"
  except:
    data = request.files['card2']
    y = data.filename
    y = y.split(".")
    y = y[1]
    if(y=='ovpn'):
      data.filename = "vpn2.ovpn"
      data.save(data.filename)
      status = "Upload Successfull"
    else:
      status = "Invalid File"
  result = {
    "id":1,
    "result":status,
    "error":None
  } 
  return(result)

@app.route('/vpnon')
def vpn_start():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.vpn.vpn='1'; uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

  
    if response.status_code == 200 :
      data = "Vpn started"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)



@app.route('/vpnoff')
def vpn_stop():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.vpn.vpn='0'; uci set system.vpn.vpn2=0;uci set system.vpn.vpn1=0; uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "Vpn Paused"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)

@app.route('/vpn1ip')
def vpn1_ip():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "ifconfig  2>/dev/null tun0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == '':
      ip = "VPN OFF"
    else:
      ip = y.split('\n')
      ip = ip[0]
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.vpn.vpn1"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == "system.vpn.vpn1='1'\n":
      status = True
    else:
      status = False
      ip = "---"
    #>>>>>>>>>>>>>name,type>>>>>>>>>>>>
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.vpn.vpn1_name;uci show system.vpn.vpn1_type"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y= y.split("\n")
    #name
    name = y[0]
    name = name.split("=")
    name = name[1]
    name = name.split("'")
    name = name[1]
    #type
    type = y[1]
    type = type.split("=")
    type = type[1]
    type = type.split("'")
    type = type[1]

    
    result = {
      "id":1,
      "error":None,
      "result":{"type":type,"ip":ip,"status":status,"name":name}
    }
    return(result)

@app.route('/vpn2ip')
def vpn2_ip():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "ifconfig  2>/dev/null tun0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == '':
      ip = "VPN OFF"
    else:
      ip = y.split('\n')
      ip = ip[0]
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.vpn.vpn2"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == "system.vpn.vpn2='1'\n":
      status = True
    else:
      status = False
      ip = "---"
    #>>>>>>>>>>>>>name,type>>>>>>>>>>>>
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.vpn.vpn2_name;uci show system.vpn.vpn2_type"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y= y.split("\n")
    #name
    name = y[0]
    name = name.split("=")
    name = name[1]
    name = name.split("'")
    name = name[1]
    #type
    type = y[1]
    type = type.split("=")
    print(type)
    type = type[1]
    type = type.split("'")
    type = type[1]

    
    result = {
      "id":1,
      "error":None,
      "result":{"type":type,"ip":ip,"status":status,"name":name}
    }
    return(result)

@app.route('/vpn1connect')
def vpn1_connect():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.vpn.vpn1=1;uci set system.vpn.vpn2=0;uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.status_code)
    result= {
      "id":1,
      "error":None,
      "result":x
    }
    return(result)

@app.route('/vpn2connect')
def vpn2_connect():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.vpn.vpn2=1;uci set system.vpn.vpn1=0;uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.status_code)
    result= {
      "id":1,
      "error":None,
      "result":x
    }
    return(result)

@app.route('/vpn1disconnect')
def vpn1_disconnect():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.vpn.vpn1=0;uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.status_code)
    result= {
      "id":1,
      "error":None,
      "result":x
    }
    return(result)

@app.route('/vpn2disconnect')
def vpn2_disconnect():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.vpn.vpn2=0;uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.status_code)
    result= {
      "id":1,
      "error":None,
      "result":x
    }
    return(result)


@app.route('/getvpn2')
def get_vpn2():
  url = rpc_url
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.vpn.vpn2_name;uci show system.vpn.vpn2_username"
        ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y=y.split("\n")
  vpn2_name = y[0].split("=")
  vpn2_name = vpn2_name[1].split("'")
  vpn2_name = vpn2_name[1]

  username = y[1].split("=")
  username = username[1].split("'")
  username = username[1]

  
  result = {
  "id":1,
  "result":{"vpn1_name":vpn2_name,"username":username},
  "error":None
    }
  return(result)

@app.route('/getvpn1')
def get_vpn1():
  url = rpc_url
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.vpn.vpn1_name;uci show system.vpn.vpn1_username"
        ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y=y.split("\n")
  vpn1_name = y[0].split("=")
  vpn1_name = vpn1_name[1].split("'")
  vpn1_name = vpn1_name[1]

  username = y[1].split("=")
  username = username[1].split("'")
  username = username[1]

  
  result = {
  "id":1,
  "result":{"vpn1_name":vpn1_name,"username":username},
  "error":None
    }
  return(result)

@app.route('/editvpn', methods=['POST'])
def edit_vpn():
  data = request.get_json()
  print(data)
  networkname = data["networkName"]
  username = data["username"]
  cardno = data["cardno"]
  print(cardno)
  url = rpc_url
  if cardno == 1:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
           "uci set system.vpn.vpn1_name="+networkname+";uci set system.vpn.vpn1_username="+username
          ]
    })
    headers = {
      'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
           "uci set system.vpn.vpn2_name="+networkname+";uci set system.vpn.vpn2_username="+username
          ]
    })
    headers = {
      'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)


  return("Saved")

  
#>>>>>>>>>>>>>>VPN SETTINGS PAGE OVER>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




#>>>>>>>>>>>>>FOR SPEED CONTROL PAGE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@app.route('/speedbooston')
def speedboost_on():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.custom.speedboost='1';uci set system.custom.loadbalancing='0'; uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "SpeedBoost On"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/speedboostoff')
def speedboost_off():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.custom.speedboost='0'; uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "SpeedBoost Off"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)
    
#>>>>>>>>>>>>>>>>>>>>>>>> SPEED CONTROL PAGE OVER>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>> LOAD BALANCING PAGE STARTS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/loadbalancingon')
def loadbalancing_on():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.custom.loadbalancing='1'; uci set system.custom.speedboost='0'; uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "load balancing on"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/loadbalancingoff')
def loadbalancing_off():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.custom.loadbalancing='0'; uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "load balancing off"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)

@app.route('/loadbalancingstatus')

def loadbalancing_status():
    url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.custom.loadbalancing"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    x=(response.text)
    data = json.loads(x)
    
    x=data['result'].split(".")
    y = x[2]
    z = y.split("=")
    loadbalancingstatus =(z[1])
    
    if loadbalancingstatus == "'0'\n" :
        status = False
    else:
        status = True

    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)
    
@app.route('/lbon')
def lb_on():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set system.custom.static_load=0;uci commit"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
      status = "Dynamic On"
    else:
      status = response.status_code
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)


@app.route('/lboff')
def lb_off():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set system.custom.static_load=1;uci commit"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
      status = "Static On"
    else:
      status = response.status_code
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)


@app.route('/lbstatus')
def lb_status():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.custom.static_load"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x= response.text
    x = (response.text)
    data = json.loads(x)
    x=data['result']
    y_new= x.split("=")
    y1=y_new[1].split("\n")
    lb_status=(y1[0])
    if lb_status== "'1'":
      status = False
    else:
      status = True
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)

@app.route('/getloadbalance')

def get_loadbalance():
  url = rpc_url
  list1=[]
  #>>>>>>>>wan1>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth1;uci show network.wan.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth1;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan.enabled;uci show mwan3.wan_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wan1",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>wan2>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth2;uci show network.wan2.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth2"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan2.enabled;uci show mwan3.wan2_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan2.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wan2",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>>wan3>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth3;uci show network.wan3.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth3;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan3.enabled;uci show mwan3.wan3_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan3.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wan3",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>wan4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth4;uci show network.wan4.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth4;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan4.enabled;uci show mwan3.wan4_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan4.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wan4",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>>>wan5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth5;uci show network.wan5.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth5;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan5.enabled;uci show mwan3.wan5_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan5.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      weight = incoming_data[1]
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wan5",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>wan6>>>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth6;uci show network.wan6.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth6;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan6.enabled;uci show mwan6.wan_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan6.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wan6",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>>>>wan7>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.wlan0;uci show network.wwan.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.wlan0;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")

      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wwan.enabled;uci show mwan3.wwan_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wwan.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = [y1,"wwan",status,weight]
      list1.append(result)
  else:
    list1
  jsonObj = json.dumps(list1)
  return(jsonObj)

@app.route('/setloadbalance', methods=['POST'])
def set_loadbalance():
  url = rpc_url
  data = request.get_json()
  list1 = []
  for i in range (len(data)):
    if(data[i]["checked"]) == True:
        list1.append(data[i])

  wan_name =[]
  wan_weight=[]
  total = 0
  for i in range (len(list1)):
    wan_name.append(list1[i]["interfaceName"])
    wan_weight.append(list1[i]["weight"])
    total = total + int(wan_weight[i])
  if (total == 100):
     for i in range (len(wan_name)):
         if (wan_name[i])=="wan1":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wan_m1_w1.weight="+str(wan_weight[i])+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
         if(wan_name[i])=="wan2":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wan2_m1_w1.weight="+wan_weight[i]+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
         if(wan_name[i])=="wan3":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wan3_m1_w1.weight="+wan_weight[i]+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
         if(wan_name[i])=="wan4":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wan4_m1_w1.weight="+wan_weight[i]+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
         if(wan_name[i])== "wan5":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wan5_m1_w1.weight="+wan_weight[i]+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
         if(wan_name[i])== "wan6":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wan6_m1_w1.weight="+wan_weight[i]+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
         if (wan_name[i])=="wwan":
              payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3.wwan_m1_w1.weight="+str(int(wan_weight[i]))+";uci commit"
               ]
              })
              headers = {
                'Content-Type': 'application/json',
             }
              response = requests.request("POST", url, headers=headers, data=payload)
              x = "Success"
  else:
    x = "failed"
  result = {
    "result":x
  }
  return(result)


@app.route('/setlbinterface', methods=['POST'])
def set_lbinterface():
  url = rpc_url
  data = request.get_json()
  checkedlist = []
  uncheckedlist = []
  for i in range (len(data)):
    if(data[i]["checked"]) == True:
        checkedlist.append(data[i])
    else:
        uncheckedlist.append(data[i])
  wan_name_enable = []
  for i in range (len(checkedlist)):
    wan_name_enable.append(checkedlist[i]["interfaceName"])
  for i in range (len(wan_name_enable)):
    print(wan_name_enable)
    if wan_name_enable[i] == "wan1":
      wan_name_enable[i] = "wan"
    if wan_name_enable[i] == "wwan":
      wan_name_enable[i] = "wwan"
    payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3."+wan_name_enable[i]+".enabled=1;uci commit"
               ]
              })
    headers = {
                'Content-Type': 'application/json',
             }
    response = requests.request("POST", url, headers=headers, data=payload)

  wan_name_disable=[]
  for i in range (len(uncheckedlist)):
    wan_name_disable.append(uncheckedlist[i]["interfaceName"])

  
  for i in range (len(wan_name_disable)):
    print(wan_name_disable[i])
    if wan_name_disable[i] == "wan1":
      wan_name_disable[i] = "wan"
    if wan_name_disable[i] == "wwan":
      wan_name_disable[i] = "wwan"
    payload = json.dumps({
              "id":1,
              "method": "exec",
              "params": [
                "uci set mwan3."+wan_name_disable[i]+".enabled=0;uci commit"
               ]
              })
    headers = {
                'Content-Type': 'application/json',
             }
    response = requests.request("POST", url, headers=headers, data=payload)
  
  return("done...")


#>>>>>>>>>>>>>>>>>>>>>>>>LOAD BALANCING PAGE ENDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>> WAN PAGE Starts>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>wan1
@app.route('/wan1ip')
def wan1_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth1;uci show system.wan_ip.eth1;cat /sys/class/net/eth1/address;uci show network.wan.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    print(y)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
        y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    if mac == 'network.wan.proto':
      mac = ''
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]
    f_result = {
    "result":{"customName":customName,"ip":ip,"proto":proto,"mac":mac}
    }   
    return(f_result) 

@app.route('/wan1ipstatus')

def wan1ip_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth1;uci show network.wan.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    buttonstat_initial = y.split("\n")
    buttonstat = buttonstat_initial[1].split("=")
    buttonstat = buttonstat[1]
    new_buttonstat= buttonstat.replace("'", "")
    if(new_buttonstat == '0'):
      buttonStatus = True
    else:
      buttonStatus = False
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      status = True
    else:
      status = False
    result = {
    "id":"1",
    "result":{"status":status,"buttonStatus":buttonStatus},
    "error":None
    }
    return(result)


#Disconnect on card
@app.route('/disconnectwan1')
def disconnect_wan1():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan.disabled='1';uci commit;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/connectwan1')

def connect_wan1():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan.disabled='0';uci commit;/etc/init.d/network restart"
      
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/editwan1network', methods=['POST'])
def edit_wan1():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  string1 = "uci set network.wan.username="
  string2 = "uci set network.wan.password="

  url = rpc_url
  if contype == 'PPPoE':

    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci set network.wan.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
      status = "connected"
    else:
      status = "failed"
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci del network.wan.username;uci del network.wan.password;uci set network.wan.proto='dhcp';uci set network.wan.metric='1';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
       status = "connected"
    else:
       status = "failed"
  result = {
       'status':status
     }

  return(result)



#>>Wan1 ends



#>>Wan2 Starts

@app.route('/wan2ip')
def wan2_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth2;uci show system.wan_ip.eth2;cat /sys/class/net/eth2/address;uci show network.wan2.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    print(y)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
        y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    if mac == 'network.wan2.proto':
      mac = ''
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]
    f_result = {
    "result":{"customName":customName,"ip":ip,"proto":proto,"mac":mac}
    }   
    return(f_result) 

@app.route('/wan2ipstatus')

def wan2ip_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth2;uci show network.wan2.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    buttonstat_initial = y.split("\n")
    buttonstat = buttonstat_initial[1].split("=")
    buttonstat = buttonstat[1]
    new_buttonstat= buttonstat.replace("'", "")
    if(new_buttonstat == '0'):
      buttonStatus = True
    else:
      buttonStatus = False
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      status = True
    else:
      status = False
    result = {
    "id":"1",
    "result":{"status":status,"buttonStatus":buttonStatus},
    "error":None
    }
    return(result)


#wan2 discoonect
@app.route('/disconnectwan2')
def disconnect_wan2():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan2.disabled='1';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/connectwan2')
def connect_wan2():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan2.disabled='0';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/editwan2network', methods=['POST'])
def edit_wan2():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  string1 = "uci set network.wan2.username="
  string2 = "uci set network.wan2.password="

  url = rpc_url
  if contype == 'PPPoE':

    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci set network.wan2.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
      status = "connected"
    else:
      status = "failed"
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci del network.wan2.username;uci del network.wan2.password;uci set network.wan2.proto='dhcp';uci set network.wan2.metric='2';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
       status = "connected"
    else:
       status = "failed"
  result = {
       'status':status
     }

  return(result)

#>>Wan2 Ends

#>>Wan3 Starts

@app.route('/wan3ip')
def wan3_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth3;uci show system.wan_ip.eth3;cat /sys/class/net/eth3/address;uci show network.wan3.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    print(y)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
        y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    if mac == 'network.wan3.proto':
      mac = ''
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]
    f_result = {
    "result":{"customName":customName,"ip":ip,"proto":proto,"mac":mac}
    }   
    return(f_result) 

@app.route('/wan3ipstatus')

def wan3ip_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth3;uci show network.wan3.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    buttonstat_initial = y.split("\n")
    buttonstat = buttonstat_initial[1].split("=")
    buttonstat = buttonstat[1]
    new_buttonstat= buttonstat.replace("'", "")
    if(new_buttonstat == '0'):
      buttonStatus = True
    else:
      buttonStatus = False
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      status = True
    else:
      status = False
    result = {
    "id":"1",
    "result":{"status":status,"buttonStatus":buttonStatus},
    "error":None
    }
    return(result)



#wan3 discon
@app.route('/disconnectwan3')
def disconnect_wan3():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan3.disabled='1';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/connectwan3')
def connect_wan3():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan3.disabled='0';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)



@app.route('/editwan3network', methods=['POST'])
def edit_wan3():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  #network.wan.username='username';uci set network.wan.password='password';uci commit;/etc/init.d/network restart
  string1 = "uci set network.wan3.username="
  string2 = "uci set network.wan3.password="

  url = rpc_url
  if contype == 'PPPoE':

    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci set network.wan3.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
          #"uci set network.wan.proto='pppoe';uci set network.wan.username='username';uci set network.wan.password='password';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
      status = "connected"
    else:
      status = "failed"
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci del network.wan3.username;uci del network.wan3.password;uci set network.wan3.proto='dhcp';uci set network.wan3.metric='3';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
       status = "connected"
    else:
       status = "failed"
  result = {
       'status':status
     }

  return(result)

#>>Wan3 Ends

#>>Wan4 Starts

@app.route('/wan4ip')
def wan4_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth4;uci show system.wan_ip.eth4;cat /sys/class/net/eth4/address;uci show network.wan4.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    print(y)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
        y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    if mac == 'network.wan4.proto':
      mac = ''
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]
    f_result = {
    "result":{"customName":customName,"ip":ip,"proto":proto,"mac":mac}
    }   
    return(f_result) 

@app.route('/wan4ipstatus')

def wan4ip_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth4;uci show network.wan4.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    buttonstat_initial = y.split("\n")
    buttonstat = buttonstat_initial[1].split("=")
    buttonstat = buttonstat[1]
    new_buttonstat= buttonstat.replace("'", "")
    if(new_buttonstat == '0'):
      buttonStatus = True
    else:
      buttonStatus = False
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      status = True
    else:
      status = False
    result = {
    "id":"1",
    "result":{"status":status,"buttonStatus":buttonStatus},
    "error":None
    }
    return(result)

#wan4 discon


@app.route('/disconnectwan4')
def disconnect_wan4():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan4.disabled='1';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/connectwan4')
def connect_wan4():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan4.disabled='0';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/editwan4network', methods=['POST'])
def edit_wan4():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  #network.wan.username='username';uci set network.wan.password='password';uci commit;/etc/init.d/network restart
  string1 = "uci set network.wan4.username="
  string2 = "uci set network.wan4.password="

  url = rpc_url
  if contype == 'PPPoE':

    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci set network.wan4.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
      status = "connected"
    else:
      status = "failed"
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci del network.wan4.username;uci del network.wan4.password;uci set network.wan4.proto='dhcp';uci set network.wan4.metric='4';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
       status = "connected"
    else:
       status = "failed"
  result = {
       'status':status
     }

  return(result)

#>>Wan4 Ends

#>>WAN5 Starts

@app.route('/wan5ip')
def wan5_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth5;uci show system.wan_ip.eth5;cat /sys/class/net/eth5/address;uci show network.wan5.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    print(y)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
        y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    if mac == 'network.wan5.proto':
      mac = ''
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]
    f_result = {
    "result":{"customName":customName,"ip":ip,"proto":proto,"mac":mac}
    }   
    return(f_result) 

@app.route('/wan5ipstatus')

def wan5ip_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth5;uci show network.wan5.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    buttonstat_initial = y.split("\n")
    buttonstat = buttonstat_initial[1].split("=")
    buttonstat = buttonstat[1]
    new_buttonstat= buttonstat.replace("'", "")
    if(new_buttonstat == '0'):
      buttonStatus = True
    else:
      buttonStatus = False
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      status = True
    else:
      status = False
    result = {
    "id":"1",
    "result":{"status":status,"buttonStatus":buttonStatus},
    "error":None
    }
    return(result)



@app.route('/disconnectwan5')


def disconnect_wan5():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan5.disabled='1';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/connectwan5')
def connect_wan5():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan5.disabled='0';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)



@app.route('/editwan5network', methods=['POST'])
def edit_wan5():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  string1 = "uci set network.wan5.username="
  string2 = "uci set network.wan5.password="

  url = rpc_url
  if contype == 'PPPoE':

    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci set network.wan5.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
      status = "connected"
    else:
      status = "failed"
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci del network.wan5.username;uci del network.wan5.password;uci set network.wan5.proto='dhcp';uci set network.wan5.metric='5';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
       status = "connected"
    else:
       status = "failed"
  result = {
       'status':status
     }

  return(result)

#>>WAN5 Ends

#>>WAN6 Starts

@app.route('/wan6ip')
def wan6_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth6;uci show system.wan_ip.eth6;cat /sys/class/net/eth6/address;uci show network.wan6.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    print(y)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
        y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    if mac == 'network.wan6.proto':
      mac = ''
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]
    f_result = {
    "result":{"customName":customName,"ip":ip,"proto":proto,"mac":mac}
    }   
    return(f_result) 

@app.route('/wan6ipstatus')

def wan6ip_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth6;uci show network.wan6.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    buttonstat_initial = y.split("\n")
    buttonstat = buttonstat_initial[1].split("=")
    buttonstat = buttonstat[1]
    new_buttonstat= buttonstat.replace("'", "")
    if(new_buttonstat == '0'):
      buttonStatus = True
    else:
      buttonStatus = False
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    if c_name== "'1'":
      status = True
    else:
      status = False
    result = {
    "id":"1",
    "result":{"status":status,"buttonStatus":buttonStatus},
    "error":None
    }
    return(result)


@app.route('/disconnectwan6')
def disconnect_wan6():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan6.disabled='1';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/connectwan6')

def connect_wan6():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network.wan6.disabled='0';uci commit;/etc/init.d/network restart"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)



@app.route('/editwan6network', methods=['POST'])

def edit_wan6():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  string1 = "uci set network.wan6.username="
  string2 = "uci set network.wan6.password="

  url = rpc_url
  if contype == 'PPPoE':

    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci set network.wan6.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
        
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
      status = "connected"
    else:
      status = "failed"
  else:
    payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci del network.wan6.username;uci del network.wan6.password;uci set network.wan6.proto='dhcp';uci set network.wan6.metric='6';uci commit"
          ]
      })
    headers = {
      'Content-Type': 'application/json',
      }
    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code)==200:
       status = "connected"
    else:
       status = "failed"
  result = {
       'status':status
     }

  return(result)

#>>WAN6 Ends

# >>>>>>>>>>>Wireless Wan Interface >>>>>>>>>>>

@app.route('/wifion')
def wirelessnetwork_on():
  url = rpc_url
  payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.radio0.disabled='0'; uci commit; wifi up radio0;/etc/init.d/network restart"
      ]
    })
  headers = {
      'Content-Type': 'application/json'
    }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  if response.status_code == 200 :
    data = "wifi on"
  else:
    data = response.status_code
  result = {
        "id":1,
        "result":data,
        "error": None
    }
  return(result)


@app.route('/wifioff')
def wirelessnetwork_off():
  url = rpc_url
  payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.radio0.disabled='1'; uci commit; wifi down radio0;/etc/init.d/network restart"
      ]
    })
  headers = {
      'Content-Type': 'application/json'
    }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  if response.status_code == 200 :
    data = "wifi off"
  else:
    data = response.status_code
  result = {
        "id":1,
        "result":data,
        "error": None
    }
  return(result)

@app.route('/wifistatus')
def wifistatus():
  url = rpc_url
  payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show wireless.radio0.disabled"
      ]
    })
  headers = {
      'Content-Type': 'application/json'
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x= response.text
  data = json.loads(x)
  y=data['result']
  if(y == "wireless.radio0.disabled='0'\n"):
    status= True
  else:
    status = False
  
  result = {
    "id":1,
    "result":status,
    "error":None
  }
  return(result)


@app.route('/wwanip')
def wwan_ip():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.wlan0;uci show system.wan_ip.wlan0;cat /sys/class/net/wlan0/address;uci show network.wlan0.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName7= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip7 = ip_initial[1]
    mac7 = y3[1]
    try:
      proto_initial = y_new[3].split("\n")
      proto_initial = proto_initial[0].split("'")
      proto7 = proto_initial[1]
    except:
      proto7=""
    
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet1.ssid"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    try:
      ssid = y.split("=")
      ssid = ssid[1].split("\n")
      ssid = ssid[0].split("'")
      ssid = ssid[1]
    except:
      ssid = ""

    
    result = {
      "result":{"cutomeName":customName7,"ip":ip7,"mac":mac7,"proto":proto7,"ssid":ssid}

    }
    return(result)


@app.route('/wwanipstatus')
def wwan_status():

    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.wlan0"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    print(c_name)
    if c_name== "'1'":
      status = True
    else:
      status = False
    data_dummy = {
    "id":"1",
    "result":{"status":status},
    "error":None
    }
    return(data_dummy)



# For Wi-Fi form

@app.route('/add_network', methods=['POST'])
def add_network():
  data = request.get_json()
  name=data['networkName']
  security=data['securityMode']
  password=data['password']
  url = rpc_url


  if security == 'WPA/WPA2 PSK':
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='psk2';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
    ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
  elif security == "mixed WPA/WPA2 PSK":
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='psk-mixed';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
  else:
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='none';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
  
  return(response.status_code)


@app.route('/scanwwan')

def scan():
  
  url = rpc_url
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "iwinfo wlan0 scan | grep 'ESSID\|Encryption' | awk '{ print $2,$3}'"
        ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  incoming_data = y.split("\n")
  del incoming_data[-1]
  for i in range(len(incoming_data)):
    incoming_data[i]=incoming_data[i].strip('" "')
  result1 = [incoming_data[i] for i in range(len(incoming_data)) if i%2 !=0]
  result2 = [incoming_data[i] for i in range(len(incoming_data)) if i%2 ==0]
  res = {}
  for key in result2:
      for value in result1:
        res[key] = value
        result1.remove(value)
        break
  list1 = [(k, v) for k, v in res.items()]
  
  jsonObj = json.dumps(list1) 
  
  return(jsonObj)
  


@app.route('/scanwwantest')
def scan_test():
  
  url = rpc_url
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "iwinfo wlan0 scan | grep 'ESSID\|Encryption' | awk '{ print $2,$3}'"
        ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  incoming_data = y.split("\n")
  del incoming_data[-1]
  for i in range(len(incoming_data)):
    incoming_data[i]=incoming_data[i].strip('" "')
  

    result1 = [incoming_data[i] for i in range(len(incoming_data)) if i%2 !=0]
    result2 = [incoming_data[i] for i in range(len(incoming_data)) if i%2 ==0]

  result = {
    "security":result1,
    "name":result2
  }
  return(result)


@app.route('/addwwan', methods=['POST'])
def add_wwan():
  data = request.get_json()
  print(data)
  name=data['networkName']
  security=data['securityMode']
  password=data['password']
  print(data)

  url = rpc_url


  if security == 'WPA2 PSK':
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='psk2';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";uci commit;wifi up radio0"
    ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "id":1,
      "result":response.status_code,
      "error":None
    }

  elif security == "mixed WPA/WPA2":
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='psk-mixed';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "id":1,
      "result":response.status_code,
      "error":None
    }
  else:
    password = ""
    print(password)
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='none';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "id":1,
      "result":response.status_code,
      "error":None
    }
  
  return(result)



#>>>>>>>> Wireless Interface Ends Here >>>>>>>>>>>>>>>>>>

#>>>>>>>>>> Wan Ends    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>LAN PAGE STARTS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>SET LAN>>>>>>>>>>>>>>>>>>>

@app.route('/getlan', methods=['GET'])
def get_lan():
  try:
    url = rpc_url2
  except:
    url = rpc_url
  payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
          "uci show network.lan.ipaddr;uci show network.lan.netmask;cat /sys/class/net/eth0/address;uci show dhcp.lan.start;uci show dhcp.lan.limit;uci show dhcp.lan.dynamicdhcp;uci show network.lan.gateway"
           
          ]
      })
  headers = {
      'Content-Type': 'application/json',
      }
  response = requests.request("POST", url, headers=headers, data=payload)


  #print(response.text)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  
  res=(y.split("\n"))
  
  #ip
  try:
    # to filter ip
    ip_initial=((res[0].split("=")))
    ip_final= ip_initial[1].split("'")
    ip = ip_final[1]
  except:
    ip = '---'
  
  try:
    # to filter netmask
    net_initial=((res[1].split("=")))
    net_final= net_initial[1].split("'")
    subnet = net_final[1]
  except:
    subnet = '---'
  
  try:
    #to filter mac
    mac_final=(res[2])
    mac= mac_final
  except:
    mac='---'
  
  try:
    # to filter ippool1
    ippool1_initial=((res[3].split("=")))
    ippool1_final= ippool1_initial[1].split("'")
    ippool1 = ippool1_final[1]
  except:
    ippool1 = '---'
  
  try:
    # to filter ippool2
    ippool2_initial=((res[4].split("=")))
    ippool2_final= ippool2_initial[1].split("'")
    ippool2 = ippool2_final[1]
  except:
    ippool1 = '---'
  
  try:
    # to filter dhcp
    dhcp_initial=((res[5].split("=")))
    dhcp_final= dhcp_initial[1].split("'")
    dhcp = dhcp_final[1]
    if(int(dhcp) == 1):
      dhcp = "enable"
    else:
      dhcp = "disable"
  except:
    dhcp = '---'
  
  try:
    # to filter gateway
    gatway_initial=((res[6].split("=")))
    gateway_final= gatway_initial[1].split("'")
    gateway = gateway_final[1]
  except:
    gateway = ''
  result = {
  "id":1,
  "result":{"macAddress":mac,"ipAddress":ip,"subnetAddress":subnet,"gateway":gateway,"ipPool1":ippool1,"ipPool2":ippool2,"dhcp":dhcp},
  "error":None
    }
  return(result)


#>>>>>>>SET LAN Ends>>>>>>>>>>>>>>

#>>>>>>>>add LAN>>>>>>>>>>>>>>>>>>>
@app.route('/addlan', methods=['POST'])

def addlan():
  data = request.get_json()
  mac=data['mac']
  ip=data['ip']
  subnet=data['subnet']
  gateway=data['gateway']
  ippool1=data['ippool1']
  ippool2=data['ippool2']
  dhcp =data['dhcp']
  print(data)
  string1 = "uci set network.lan.ipaddr="+ip
  string2 = "uci set network.lan.netmask="+subnet
  string3 = "uci set dhcp.lan.start="+ippool1+";uci set dhcp.lan.limit="+ippool2
  string4 = "uci set network.lan.gateway="+gateway
  if dhcp == 'enable':
    string5 = "uci set dhcp.lan.dynamicdhcp='1'"
  else:
    string5 = "uci set dhcp.lan.dynamicdhcp='0'"
  string6 = "uci commit"
  
  try:
    url = rpc_url2
  
    payload = json.dumps({
          "id":1,
          "method": "exec",
          "params": [
             #"uci set network.lan.ipaddr="+ip+";uci set network.lan.netmask="+subnet+";uci set dhcp.lan.start='100';uci set dhcp.lan.limit='200';uci set network.lan.gateway="+gateway+";uci commit"
            string1+";"+string2+";"+string3+";"+string4+";"+string5+";"+string6
           ]
        })
    headers = {
        'Content-Type': 'application/json',
       }
    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
    return(result)
  except:
    pass
  return("failed to save")


# @app.route('/clientlist')
# def client_test():



#   url = rpc_url

#   payload = json.dumps({
#     "id":1,
#     "method": "exec",
#     "params": [
#       "cat /tmp/dhcp.leases"
#     ]
#   })
#   headers = {
#     'Content-Type': 'application/json',
#   }

#   response = requests.request("POST", url, headers=headers, data=payload)
#   x = (response.text)
#   data = json.loads(x)
#   y=data['result']
  
#   data_rem_starline = y.split("*\n")

#   data_space1 = data_rem_starline[0].split(" ")
#   data_space2 = data_rem_starline[1].split(" ")

#   data_space1 = data_rem_starline[0].split(" ")
#   data_space2 = data_rem_starline[1].split(" ")
  
  
  

#   data_dum = {
#       "id":1,
#       "result":[{"id":data_space1[0],"clientName":data_space1[3],"macAddress":data_space1[1],"assignedIP":data_space1[2]},{"id":data_space2[0],"clientName":data_space2[3],"macAddress":data_space2[1],"assignedIP":data_space2[2]}]
      
#   }
#   return(data_dum)

#>>>>>>>>>>>>>>>>>>> Lan Page Ends >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>>>>>>>>>>>>>>>>>For Parental Control>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Parental Control

@app.route('/parentalon')
def parental_on():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental='1';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)

  return(response.text)


@app.route('/parentaloff')
def parental_off():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental='0';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)

  return(response.text)




@app.route('/ualevelon')
def ualevel_on():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental_ua='1';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)

  return(response.text)

@app.route('/ualeveloff')
def ualevel_off():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental_ua='0';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  return(response.text)

@app.route('/ualevelstatus')
def ualevel_status():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.pc.parental_ua"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    x=data['result']
    y_new= x.split("=")
    y1=y_new[1].split("\n")
    u_status=(y1[0])
    if u_status== "'1'":
      status = True
    else:
      status = False
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)


@app.route('/ulevelon')
def ulevel_on():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental_u='1';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  return(response.text)


@app.route('/uleveloff')
def ulevel_off():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental_u='0';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  return(response.text)


@app.route('/ulevelstatus')
def ulevel_status():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.pc.parental_u"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    x=data['result']
    y_new= x.split("=")
    y1=y_new[1].split("\n")
    u_status=(y1[0])
    if u_status== "'1'":
      status = True
    else:
      status = False
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)



@app.route('/alevelon')
def alevel_on():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental_a='1';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  return(response.text)


@app.route('/aleveloff')
def alevel_off():
  url = rpc_url
  payload = json.dumps({
    "method": "exec",
    "id":1,
    "params": [
      "uci set system.pc.parental_a='0';system.pc.parental_change='1';uci commit"
    ]
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.status_code)
  return(response.text)

@app.route('/alevelstatus')
def alevel_status():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.pc.parental_a"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    x=data['result']
    y_new= x.split("=")
    y1=y_new[1].split("\n")
    u_status=(y1[0])
    if u_status== "'1'":
      status = True
    else:
      status = False
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)


@app.route('/dnsreport')
def dns_report():
  url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "sh /root/adblock_report.sh"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  incoming_data = data['result']
  print(incoming_data)

  incoming_data = incoming_data.split("\n",15)
  data_list=[]
  for value in incoming_data:
    data = value.split(" ")
    # #print(data)
    data_list.append(data)
    
  json_string = json.dumps(data_list)
  return(json_string)


@app.route('/editblacklist')

def edit_blacklist():

  url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /etc/adblock/adblock.blacklist"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)

  x=data['result']

  print(type(x))
  y = x.split("\n")
  del y[-1]
  

  result = {
    "id":1,
    "result":y,
    "error":None
  }
  return(result)


@app.route('/editwhitelist')

def edit_whitelist():

  url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /etc/adblock/adblock.whitelist"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)

  data = json.loads(x)

  x=data['result']

  print(type(x))
  y = x.split("\n")
  del y[-1]
  

  result = {
    "id":1,
    "result":y,
    "error":None
  }
  return(result)



@app.route('/savewhitelist',methods=['POST'])

def save_whitelist():
    
  data = request.get_data()
  data_new=data.decode('UTF-8')
  print(data_new)
  
  script = 'echo '+data_new+'>>/etc/adblock/adblock.whitelist'
  print(script)



  url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [script]
  })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)

  return("x")



@app.route('/saveblacklist', methods=['POST'])

def save_blacklist():
    
  data = request.get_data()
  data_new=data.decode('UTF-8')
  print(data_new)
  url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "echo "+data_new+">>/etc/adblock/adblock.blacklist"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  return("data")


@app.route('/deletewhitelist', methods=['POST'])
def delete_whitelist():
  url = rpc_url
  data = request.get_data()
  data_new=data.decode('UTF-8')
  #run script to  copy blacklist file from dh location
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cp /etc/adblock/adblock.whitelist /app/api/adw.txt"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  a_file = open("adw.txt", "r")

  lines = a_file.readlines()
  a_file.close()

  new_file = open("adw.txt", "w")
  for line in lines:
    if line.strip("\n") != data_new:

        new_file.write(line)

  new_file.close()
  #run scipt to copy to dh location
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cp /app/api/adw.txt  /etc/adblock/adblock.whitelist"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return("deleted")


@app.route('/deleteblacklist', methods=['POST'])
def delete_blacklist():
  url = rpc_url
  data = request.get_data()
  data_new=data.decode('UTF-8')
  #run script to  copy blacklist file from dh location
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cp /etc/adblock/adblock.blacklist /app/api/adb.txt"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  a_file = open("adb.txt", "r")

  lines = a_file.readlines()
  a_file.close()

  new_file = open("adb.txt", "w")
  for line in lines:
    if line.strip("\n") != data_new:

        new_file.write(line)

  new_file.close()
  #run scipt to copy to dh location
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cp /app/api/adb.txt  /etc/adblock/adblock.blacklist"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return("deleted")

#>>>>>>>>>>>>>>>>>>>>>>> PARENTAL CONTROL ENDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>To TEST>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/test')
def test_test():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth1;uci show system.wan_ip.eth1;cat /sys/class/net/eth1/address;uci show network.wan.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip = ip_initial[1]
    mac = y3[1]
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto = proto_initial[1]

    #wan2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth2;uci show system.wan_ip.eth2;cat /sys/class/net/eth2/address;uci show network.wan2.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName2= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip2 = ip_initial[1]
    mac2 = y3[1]
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto2 = proto_initial[1]

    #wan 3
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth3;uci show system.wan_ip.eth3;cat /sys/class/net/eth3/address;uci show network.wan3.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName3= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip3 = ip_initial[1]
    mac3 = y3[1]
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto3 = proto_initial[1]

    #mac 4
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth4;uci show system.wan_ip.eth4;cat /sys/class/net/eth4/address;uci show network.wan4.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName4= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip4 = ip_initial[1]
    mac4 = y3[1]
    proto_initial = y_new[3].split("\n")
    proto_initial = proto_initial[0].split("'")
    proto4 = proto_initial[1]


    #mac 5
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth5;uci show system.wan_ip.eth5;cat /sys/class/net/eth5/address;uci show network.wan5.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName5= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip5 = ip_initial[1]
    mac5 = y3[1]
    try:
      proto_initial = y_new[3].split("\n")
      proto_initial = proto_initial[0].split("'")
      proto5 = proto_initial[1]
    except:
      proto5=""


#mac 6
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.eth6;uci show system.wan_ip.eth6;cat /sys/class/net/eth6/address;uci show network.wan6.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName6= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip6 = ip_initial[1]
    mac6 = y3[1]
    try:
      proto_initial = y_new[3].split("\n")
      proto_initial = proto_initial[0].split("'")
      proto6 = proto_initial[1]
    except:
      proto6=""


  #Wi-fi 7
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_name.wlan0;uci show system.wan_ip.wlan0;cat /sys/class/net/wlan0/address;uci show network.wlan0.proto"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    y_new= y.split("=")
    y1=y_new[1].split("\n")
    c_name=y1[0]
    c_name = c_name.split("'")
    customName7= c_name[1]
    y2 = y_new[2]
    y3= y2.split("\n")
    ip_initial = y3[0].split("'")
    ip7 = ip_initial[1]
    mac7 = y3[1]
    try:
      proto_initial = y_new[3].split("\n")
      proto_initial = proto_initial[0].split("'")
      proto7 = proto_initial[1]
    except:
      proto7=""
    f_result = [{
    "id":1,
    "result":{"customName":customName,"ip":ip,"mac":mac,"proto":proto},
    "error":"null"
    },
    {
      "id":2,
      "result":{"cutomeName":customName2,"ip":ip2,"mac":mac2,"proto":proto2},
      "error":"null"
    },
    {
      "id":3,
      "result":{"cutomeName":customName3,"ip":ip3,"mac":mac3,"proto":proto3},
      "error":"null"
    },
    {
      "id":4,
      "result":{"cutomeName":customName4,"ip":ip4,"mac":mac4,"proto":proto4},
      "error":"null"
    },
    {
      "id":5,
      "result":{"cutomeName":customName5,"ip":ip5,"mac":mac5,"proto":proto5},
      "error":"null"
    },
    {
      "id":6,
      "result":{"cutomeName":customName6,"ip":ip6,"mac":mac6,"proto":proto6},
      "error":"null"
     },
    {
      "id":7,
      "result":{"cutomeName":customName7,"ip":ip7,"mac":mac7,"proto":proto7},
      "error":"null"
    }]
    
    return(jsonify(f_result))


@app.route('/test2')
def client_test():

  try:
    url = rpc_url2
  except:
    url = rpc_url

  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /tmp/dhcp.leases | awk '{ print $2,$3}' | wc -l"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  rows=data['result']
  rows=int(rows)
  
  
  payload = json.dumps({
    "id":1,
    "method": "exec",
    "params": [
      "cat /tmp/dhcp.leases | awk '{ print $2,$3,$4}'"
    ]
  })
  headers = {
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  incoming_data = data['result']
  

  incoming_data = incoming_data.split("\n",rows)
  data_list=[]
  for value in incoming_data:
    data = value.split(" ")

    data_list.append(data)

  z= data_list
  z_new = data_list.pop()
  json_string = json.dumps(z)
  return(json_string)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Network Storage>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/nason')
def nas_on():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set system.nas.nas=1;uci set system.nas.nas_change=1;uci commit"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
      status = "Enabled"
    else:
      status = response.status_code
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)

@app.route('/nasoff')
def nas_off():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set system.nas.nas=0;uci set system.nas.nas_change=1;uci commit"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
      status = "disabled"
    else:
      status = response.status_code
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)

@app.route('/nasstatus')
def nas_status():
    url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.nas.nas"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    x=data['result']
    y_new= x.split("=")
    y1=y_new[1].split("\n")
    nas_status=(y1[0])
    if nas_status== "'1'":
      status = True
    else:
      status = False
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)

@app.route('/addnas', methods=['POST'])
def addnas():
  data = request.get_json()
  username =data['userName']
  password =data['password']
  print(username)
  print(password)
  print(data)
  url=rpc_url
  payload = json.dumps({
        "id":1,
        "method": "exec",
        "params": [
           #--->Add Script Here""
          ]
      })
  headers = {
      'Content-Type': 'application/json',
      }
  response = requests.request("POST", url, headers=headers, data=payload)
  result = {
    "result":response.status_code
  }


  return(result)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Network Ends>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Wireless Settings>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/wifinet1')
def wifi_net1():
    try:
      url = rpc_url2
    except:
      url = rpc_url
    

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet1.ssid;uci show wireless.wifinet1.encryption"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y=="":
        customName = "Unavailable"
        security =  "Unavailable"
    else:
        y_new= y.split("=")
        #cutomName
        y_name= y_new[1].split("\n")
        customName_edit = y_name[0]
        name_list = customName_edit.split("'")
        customName=name_list[1]
        #ip
        y_sec =y_new[2].split("\n")
        sec_edit = y_sec[0]
        sec_list = sec_edit.split("'")
        security=sec_list[1]

    f_result = {
    "result":{"ssidName":customName,"security":security}
    }   
    
    return(f_result)

@app.route('/wifinet2')
def wifi_net2():
    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet2.ssid;uci show wireless.wifinet2.encryption"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y=="":
        customName = "Unavailable"
        security =  "Unavailable"
    else:
        y_new= y.split("=")
        #cutomName
        y_name= y_new[1].split("\n")
        customName_edit = y_name[0]
        name_list = customName_edit.split("'")
        customName=name_list[1]
        #ip
        y_sec =y_new[2].split("\n")
        sec_edit = y_sec[0]
        sec_list = sec_edit.split("'")
        security=sec_list[1]

    f_result = {
    "result":{"ssidName":customName,"security":security}
    }   
    
    return(f_result)


@app.route('/wifinet3')
def wifi_net3():
    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet3.ssid;uci show wireless.wifinet3.encryption"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y=="":
        customName = "Unavailable"
        security =  "Unavailable"
    else:
        y_new= y.split("=")
        #cutomName
        y_name= y_new[1].split("\n")
        customName_edit = y_name[0]
        name_list = customName_edit.split("'")
        customName=name_list[1]
        #ip
        y_sec =y_new[2].split("\n")
        sec_edit = y_sec[0]
        sec_list = sec_edit.split("'")
        security=sec_list[1]

    f_result = {
    "result":{"ssidName":customName,"security":security}
    }   
    
    return(f_result)

@app.route('/wifinet4')
def wifi_net4():
    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet4.ssid;uci show wireless.wifinet4.encryption"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
  }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y=="":
        customName = "Unavailable"
        security =  "Unavailable"
    else:
        y_new= y.split("=")
        #cutomName
        y_name= y_new[1].split("\n")
        customName_edit = y_name[0]
        name_list = customName_edit.split("'")
        customName=name_list[1]
        #ip
        y_sec =y_new[2].split("\n")
        sec_edit = y_sec[0]
        sec_list = sec_edit.split("'")
        security=sec_list[1]

    f_result = {
    "result":{"ssidName":customName,"security":security}
    }   
    
    return(f_result)

@app.route('/wifinet1status')
def wifinet1_status():

    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet1.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == "":
        status=False
    else:
        y_new= y.split("=")
        y1=y_new[1].split("\n")
        c_name=y1[0]
        if c_name== "'0'":
             status = True
        else:
             status = False
    data_dummy = {
    "id":"1",
    "result":{"status":status},
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet2status')
def wifinet2_status():

    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet2.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == "":
        status=False
    else:
        y_new= y.split("=")
        y1=y_new[1].split("\n")
        c_name=y1[0]
        if c_name== "'0'":
             status = True
        else:
             status = False
    data_dummy = {
    "id":"1",
    "result":{"status":status},
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet3status')
def wifinet3_status():

    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet3.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == "":
        status=False
    else:
        y_new= y.split("=")
        y1=y_new[1].split("\n")
        c_name=y1[0]
        if c_name== "'0'":
             status = True
        else:
             status = False
    data_dummy = {
    "id":"1",
    "result":{"status":status},
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet4status')
def wifinet4_status():

    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show wireless.wifinet4.disabled"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.text)
    data = json.loads(x)
    y=data['result']
    if y == "":
        status=False
    else:
        y_new= y.split("=")
        y1=y_new[1].split("\n")
        c_name=y1[0]
        if c_name== "'0'":
             status = True
        else:
             status = False
    data_dummy = {
    "id":"1",
    "result":{"status":status},
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet1disconnect')
def disconnect_wifi1():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet1.disabled=1;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet2disconnect')
def disconnect_wifi2():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet2.disabled=1;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet3disconnect')
def disconnect_wifi3():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet3.disabled=1;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet4disconnect')
def disconnect_wifi4():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet4.disabled=1;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/wifinet1connect')
def connect_wifi1():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet1.disabled=0;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet2connect')
def connect_wifi2():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet2.disabled=0;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet3connect')
def connect_wifi3():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet3.disabled=0;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet4connect')
def connect_wifi4():

    url = rpc_url2

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set wireless.wifinet4.disabled=0;uci commit;wifi up radio0;/etc/init.d/network restart"
        
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    data_dummy = {
    "id":"1",
    "result":response.status_code,
    "error":None
    }
    return(data_dummy)


@app.route('/wifinet1addnetwork', methods=['POST'])

def add_network1():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  url = rpc_url2
  print(data)


  if security == 'WPA/WPA2':
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='psk2';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"uci commit;wifi up radio0;/etc/init.d/network restart"
    ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  elif security == "mixed WPA/WPA2":
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='psk-mixed';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  else:
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet1.encryption='none';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }

  return(result)



@app.route('/wifinet2addnetwork', methods=['POST'])

def add_network2():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  url = rpc_url2


  if security == 'WPA/WPA2':
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet2.encryption='psk2';uci set wireless.wifinet2.ssid="+name+";"+"uci set wireless.wifinet2.key="+password+";"+"uci commit;/etc/init.d/network restart"
    ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  elif security == "mixed WPA/WPA2":
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet2.encryption='psk-mixed';uci set wireless.wifinet2.ssid="+name+";"+"uci set wireless.wifinet2.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  else:
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet2.encryption='none';uci set wireless.wifinet2.ssid="+name+";"+"uci set wireless.wifinet2.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  
  return(result)

@app.route('/wifinet3addnetwork', methods=['POST'])

def add_network3():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  url = rpc_url2


  if security == 'WPA/WPA2':
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet3.encryption='psk2';uci set wireless.wifinet3.ssid="+name+";"+"uci set wireless.wifinet3.key="+password+";"+"uci commit;/etc/init.d/network restart"
    ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  elif security == "mixed WPA/WPA2":
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet3.encryption='psk-mixed';uci set wireless.wifinet3.ssid="+name+";"+"uci set wireless.wifinet3.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  else:
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet3.encryption='none';uci set wireless.wifinet3.ssid="+name+";"+"uci set wireless.wifinet3.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  
  return(result)

@app.route('/wifinet4addnetwork', methods=['POST'])

def add_network4():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  url = rpc_url2


  if security == 'WPA/WPA2':
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet4.encryption='psk2';uci set wireless.wifinet4.ssid="+name+";"+"uci set wireless.wifinet4.key="+password+";"+"uci commit;/etc/init.d/network restart"
    ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  elif security == "mixed WPA/WPA2":
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet4.encryption='psk-mixed';uci set wireless.wifinet4.ssid="+name+";"+"uci set wireless.wifinet4.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  else:
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set wireless.wifinet4.encryption='none';uci set wireless.wifinet4.ssid="+name+";"+"uci set wireless.wifinet4.key="+password+";"+"uci commit"
      ]
      })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = {
      "result":response.status_code
    }
  
  return(result)


@app.route('/wirelesson')

def wireless_on():
    url = rpc_url2
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.custom.wireless_set=1;uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "wireless On"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)

@app.route('/wirelessoff')

def wireless_off():
    url = rpc_url2
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci set system.custom.wireless_set=0;uci commit"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    if response.status_code == 200 :
      data = "wireless On"
    else:
      data = response.status_code
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)

@app.route('/wirelessstatus')
def wireless_status():
    try:
      url = rpc_url2
    except:
      pass
      url = rpc_url
    payload = json.dumps({
      "method": "exec",
      "id":1,
      "params": [
        "uci show system.custom.wireless_set"
      ]
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    x=(response.text)
    data = json.loads(x)
    print(data['result'])
    x=data['result'].split(".")
    y = x[2]
    z = y.split("=")
    wireless_stat =(z[1])
    
    if wireless_stat == "'0'\n" :
        status = False
    else:
        status = True

    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)

#>>>>>>>>>>>>>>>Speed Boost>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/getspeedboost')
def get_speedboost():
  url = rpc_url
  list1=[]
  #>>>>>>>>wan1>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth1;uci show network.wan.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")

  if new_stat == 'on':
    status = True
  else:
    status = False

  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth1;"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan.enabled;uci show mwan3.wan_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wan1",status,toggle_stat,weight]
      }
      list1.append(result)
  else:
    list1

  #>>>>>>>>>>>wan2>>>>>>>>>>>>>>

  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth2;uci show network.wan2.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")
  if new_stat == 'on':
    status = True
  else:
    status = False
  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth2"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan2.enabled;uci show mwan3.wan2_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan2.enabled='1'":
        toggle_stat = True
      else:
        toggle_stat = False
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wan2",status,toggle_stat,weight]
      }
      list1.append(result)
      
  else:
    list1


  #>>>>>wan3>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth3;uci show network.wan3.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")
  if new_stat == 'on':
    status = True
  else:
    status = False
  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth3"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan3.enabled;uci show mwan3.wan3_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan3.enabled='1'":
        toggle_stat = 1
      else:
        toggle_stat = 0
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wan3",status,toggle_stat,weight]
      }
      list1.append(result)
      
  else:
    list1
#>>>>>>>>>wan4>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth4;uci show network.wan4.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")
  if new_stat == 'on':
    status = True
  else:
    status = False
  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth4"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan4.enabled;uci show mwan3.wan4_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan4.enabled='1'":
        toggle_stat = 1
      else:
        toggle_stat = 0
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wan4",status,toggle_stat,weight]
      }
      list1.append(result)
      
  else:
    list1

#>>>>>>>>>>>wan5>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth5;uci show network.wan5.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")
  if new_stat == 'on':
    status = True
  else:
    status = False
  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth5"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }
      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan5.enabled;uci show mwan3.wan5_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan5.enabled='1'":
        toggle_stat = 1
      else:
        toggle_stat = 0
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wan5",status,toggle_stat,weight]
      }
      list1.append(result)
      
  else:
    list1
#>>>>>>>>>>>wan6>>>>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.eth6;uci show network.wan6.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")
  if new_stat == 'on':
    status = True
  else:
    status = False
  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.eth6"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wan6.enabled;uci show mwan3.wan6_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wan6.enabled='1'":
        toggle_stat = 1
      else:
        toggle_stat = 0
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wan6",status,toggle_stat,weight]
      }
      list1.append(result)
      
  else:
    list1
#>>>>>>>>>>>>>>>wwan>>>>>>>>>>>>>>>>>>>>>>>>>>
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show system.wan_internet.wlan0;uci show network.wwan.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }

  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.text)
  data = json.loads(x)
  y=data['result']
  y_stat = (y.split("\n"))
  y_stat = (y.split("\n"))
  stat=y_stat[1].split("=")
  new_stat = stat[1].replace("'", "")
  if new_stat == 'on':
    status = True
  else:
    status = False
  y_new= y.split("=")
  y1=y_new[1].split("\n")
  c_name=y1[0]
  if c_name== "'1'":
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show system.wan_name.wlan0"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      y = y.split("=")
      y1 = y[1].strip("''\n")
      payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
         "uci show mwan3.wwan.enabled;uci show mwan3.wwan_m1_w1.weight"
        ]
      })
      headers = {
        'Content-Type': 'application/json',
      }

      response = requests.request("POST", url, headers=headers, data=payload)
      x = (response.text)
      data = json.loads(x)
      y=data['result']
      incoming_data = y.split("\n")
      if incoming_data[0] == "mwan3.wwan.enabled='1'":
        toggle_stat = 1
      else:
        toggle_stat = 0
      try:
        weight = incoming_data[1]
        weight=weight.split("=")
        weight = weight[1]
        weight = weight.split("'")
        weight = weight[1]
        weight = int(weight)
      except:
        weight = 0
      result = {
       "interface": [y1,"wwan",status,toggle_stat,weight]
      }
      list1.append(result)
      
  else:
    list1
  result = {
    "id":1,
    "result":list1,
    "error":None
  }

  return(result)


@app.route('/setspeedboost', methods=['POST'])

def set_speedboost():
  data = request.get_json()
  print(data)
  interface=data['interface']
  if interface == 'wan1':
    interface='wan'
  if interface == 'wwan':
    interface='wwan'
  isp = data['isp']
  statustype = data['statusType']
  print(data)
  url = rpc_url
  if statustype == True:

    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network."+interface+".multipath=on;uci commit"
        ]
      })
    headers = {
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.status_code)
    if x == 200:
      result = {
      "id":1,
      "result":"Enabled",
      "error":None
      }
  else:
    payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci set network."+interface+".multipath=off;uci commit"
        ]
    })
    headers = {
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    x = (response.status_code)
    if x == 200:
      result = {
      "id":1,
      "result":"disabled",
      "error":None
      }

  
  return(result)

# @app.route('/setdisablespeedboost', methods=['POST'])
# @cross_origin(supports_credentials=True)
# def set_disable():
#   data = request.get_json()
#   #interface=data['ssid']
#   print(data)
#   url = rpc_url
#   payload = json.dumps({
#       "id":1,
#       "method": "exec",
#       "params": [
#         "uci set network."+interface+".multipath=off;uci commit"
#         ]
#     })
#   headers = {
#     'Content-Type': 'application/json',
#     }
#   response = requests.request("POST", url, headers=headers, data=payload)
#   x = (response.status_code)
#   if x == 200:
#     result = {
#       "id":1,
#       "result":"disabled",
#       "error":None
#     }
  
#   return(result)


@app.route('/getwan1statusspeedboost')
def get_wan1statusspeedboost():
  url = rpc_url
  payload = json.dumps({
      "id":1,
      "method": "exec",
      "params": [
        "uci show network.wan.multipath"
        ]
    })
  headers = {
    'Content-Type': 'application/json',
    }
  response = requests.request("POST", url, headers=headers, data=payload)
  x = (response.status_code)
  
  
  return("result")




if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host='0.0.0.0',port='5001')