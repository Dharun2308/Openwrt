import subprocess
from flask import Flask, request,jsonify,render_template,session,redirect,url_for,flash
from flask.sessions import SecureCookieSession, SessionInterface
import requests
import json
import time
import os
import re
import subprocess
from datetime import timedelta,datetime
import sqlite3 as sql
from cryptography.fernet import Fernet
import uuid


def run_uci(x):
    proc = subprocess.Popen([x], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return(out.decode("utf-8"))

def vpn1_path():
	file1 = open("/app/api/vpn1.ovpn", "r")
	list_of_lines = file1.readlines()
	x = list_of_lines.index("auth-user-pass\n")
	list_of_lines[x]= "auth-user-pass /etc/openvpn/vpn1.auth\n"
	file1 = open("/app/api/vpn1.ovpn", "w")
	file1.writelines(list_of_lines)
	file1.close()


def vpn2_path():
	file1 = open("/app/api/vpn2.ovpn", "r")
	list_of_lines = file1.readlines()
	x = list_of_lines.index("auth-user-pass\n")
	list_of_lines[x]= "auth-user-pass /etc/openvpn/vpn1.auth\n"
	file1 = open("/app/api/vpn2.ovpn", "w")
	file1.writelines(list_of_lines)
	file1.close()


def save_username_vpn1(username,password):
	f= open("/etc/openvpn/vpn1.auth","w+")
	f.write(username + "\n")
	f.write(password)
	f.close()

def save_username_vpn2(username,password):
	f= open("/etc/openvpn/vpn2.auth","w+")
	f.write(username + "\n")
	f.write(password)
	f.close()


x=(os.path.exists('/app/api/key.key'))

if x == False:
    key = Fernet.generate_key()
    id = "arcauser"
    password = "usEr@arca3"
    file = open('/app/api/key.key','wb')
    file.write(key)
    file.close()
    conn = sql.connect('/app/api/router.db')
    fernet = Fernet(key)
    encid = fernet.encrypt(id.encode())
    encpassword = fernet.encrypt(password.encode())
    try:
      conn.execute('CREATE TABLE users (id text, password text)')
      print ("Table created successfully")
      conn.close()
      with sql.connect("/app/api/router.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (id, password) VALUES (?,?)",(encid,encpassword))
                con.commit()
      print("Done")
    except:
      pass

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

app.secret_key='ODE5MTAzNTIwW'

@app.route('/login',methods=['GET','POST'])

def login():
    if request.method=='POST':

        app.permanent_session_lifetime = timedelta(seconds=5)
        data = request.get_json()
        session['username']=data['username']
        session['password']=data['password']
        file = open('/app/api/key.key', 'rb')
        key = file.read()
        fernet = Fernet(key)
        con = sql.connect("/app/api/router.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from users")
        rows = cur.fetchall()
        id_data=[] 
        for r in rows:
          id_data.append(r[0])
          id_data.append(r[1])

        decid = fernet.decrypt(id_data[0]).decode()
        decpassword = fernet.decrypt(id_data[1]).decode()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if(session['username']==decid and session['password']==decpassword):
          session.modified = True
          app.permanent_session_lifetime = timedelta(seconds=1)
          #token_id=uuid.uuid1()
          #session['id']=token_id
          #print(session['id'])
          result = {
            "data":True,
            "user":session['username'],
            "current_time":current_time,
          }
          return(result)

          #return render_template('index.html')
    result = {
      "data":False,
    }
    return(result)



@app.route('/logout')

def logout():
    session.pop('username',None)
    #return redirect(url_for('index'))
    result = {
      "data":False,
      "result":"Logged out"
    }
    return(result)


@app.route('/timeout')

def time_out():
    login=False
    if 'username' in session:
        login=True
    return ("login")



@app.route('/')

def index():
    login=False
    if 'username' in session:
        login=True
    return render_template('login_home.html',login=login)

##>>>>>>>>>>>>>>>>>>>Dashboard>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/api', methods=['GET'])

def api():
    return {
        "id": 1,
        "title": "ARCA Router",
        "completed": True

    }

@app.route('/dongles')

def dongle_con():
    x = "uci show system.wan_internet.eth1;uci show system.wan_internet.eth2;uci show system.wan_internet.eth3;uci show system.wan_internet.eth4;uci show system.wan_internet.eth5;uci show system.wan_internet.eth6;uci show system.wan_internet.wlan0"
    response=run_uci(x)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>edit response here>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    data = response.split("\n")

    eth1_data=data[0]
    eth1_data = eth1_data.split("=")
    eth1_data = eth1_data[1]
    eth1_data = eth1_data.split("'")
    eth1_data = int(eth1_data[1])
    
    eth2_data=data[1]
    eth2_data = eth2_data.split("=")
    eth2_data = eth2_data[1]
    eth2_data = eth2_data.split("'")
    eth2_data = int(eth2_data[1])
    
    eth3_data=data[2]
    eth3_data = eth3_data.split("=")
    eth3_data = eth3_data[1]
    eth3_data = eth3_data.split("'")
    eth3_data = int(eth3_data[1])

    eth4_data=data[3]
    eth4_data = eth4_data.split("=")
    eth4_data = eth4_data[1]
    eth4_data = eth4_data.split("'")
    eth4_data = int(eth4_data[1])

    eth5_data=data[4]
    eth5_data = eth5_data.split("=")
    eth5_data = eth5_data[1]
    eth5_data = eth5_data.split("'")
    eth5_data = int(eth5_data[1])

    eth6_data=data[5]
    eth6_data = eth6_data.split("=")
    eth6_data = eth6_data[1]
    eth6_data = eth6_data.split("'")
    eth6_data = int(eth6_data[1])

    wlan0_data=data[6]
    wlan0_data = wlan0_data.split("=")
    wlan0_data = wlan0_data[1]
    wlan0_data = wlan0_data.split("'")
    wlan0_data = int(wlan0_data[1])  
    count = eth1_data+ eth2_data+ eth3_data+ eth4_data+ eth5_data+ eth6_data+wlan0_data
    return {
      "id":1,
      "result": count,
      "error": "null"
    }
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Pending DeviceCon(MI Router)

@app.route('/devicecon')

def device_con():
    uci = "cat /tmp/dhcp.leases "
    x = run_uci(uci)
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
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


@app.route('/linestatus')

def con_line():
    x = "uci show system.custom.internet"
    response=run_uci(x)
    data = response.split("=")
    data = data[1].split("'")
    data=int(data[1])
    if data == 1:
    	status = True
    else:
    	status = False
    result = {

        "id": 1,

        "result": status,

        "error" : None

    }
    return(result)


@app.route('/version')

def kernal_version():
    x = "cat /app/api/version.json"
    response=run_uci(x)
    res = json.loads(response)

   
    fresult = {

        "id":3,

        "result":res,

        "error": None

    }

    return(fresult)
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>Overview>>>>>>>>>>>>>>>>>>>>
@app.route('/vpnstatus')

def vpn_status():
    x = "uci show system.vpn.vpn"
    response = run_uci(x)
    data = response.split("=")
    data = data[1]
    data = data.split("\n")
    data= data[0]
    data = data.split("'")
    vpnstatus = int(data[1])
    if vpnstatus == 0 :
        status = False
    else:
        status = True
    result = {
        "id": 1,
        "result": status,
        "error" : None
    }

    return(result)

@app.route('/parentstatus')

def parent_status():
    x = "uci show system.pc.parental"
    response = run_uci(x)
    data = response.split("=")
    data = data[1]
    data = data.split("\n")
    data= data[0]
    data = data.split("'")
    parent_status = int(data[1])
    if parent_status == 0 :
        status = False
    else:
        status = True
    result = {
        "id": 1,
        "result": status,
        "error" : None
    }

    return(result)


@app.route('/speedbooststatus')



def speedboost_status():
    x = "uci show system.custom.speedboost"
    response = run_uci(x)
    data = response.split("=")
    data = data[1]
    data = data.split("\n")
    data= data[0]
    data = data.split("'")
    speedbooststatus = int(data[1])
    if speedbooststatus == 0 :
        status = False
    else:
        status = True
    result = {
        "id": 1,
        "result": status,
        "error" : None
    }
    return(result)

#>>>>>>>>>>>>>VPN Page>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/editupload', methods=['POST'])

def edit_upload():
  x = "cp /app/api/vpn1.ovpn /etc/openvpn/vpn1.ovpn"
  a = "cp /app/api/vpn2.ovpn /etc/openvpn/vpn2.ovpn"
  try:
    data = request.files['card1']
    y = data.filename
    y = y.split(".")
    y = y[1]
    if(y=='ovpn'):
      data.filename = "vpn1.ovpn"
      data.save(data.filename)
      status = "Upload Successfull"
      #code for updating file vpn1
      vpn1_path()
      run_uci(x)
    else:
      status = "Invalid File"
  except:
    data2 = request.files['card2']
    y = data2.filename
    y = y.split(".")
    y = y[1]
    if(y=='ovpn'):
      data2.filename = "vpn2.ovpn"
      data2.save(data2.filename)
      status = "Upload Successfull"
      #code for updating file vpn2
      vpn2_path()
      run_uci(a)
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
    x = "uci set system.vpn.vpn='1'; uci commit"
    response = run_uci(x)
    data = "Vpn started"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/vpnoff')
def vpn_stop():
    x = "uci set system.vpn.vpn='0'; uci set system.vpn.vpn2=0;uci set system.vpn.vpn1=0; uci commit"
    response = run_uci(x)
    data = "Vpn Paused"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/vpn1ip')
def vpn1_ip():
    x = "ifconfig  2>/dev/null tun0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
    z = "uci show system.vpn.vpn1"
    name_type = "uci show system.vpn.vpn1_name;uci show system.vpn.vpn1_type"
    response = run_uci(x)
    print(response)
    if response != "":
      ip = response
      print(ip)
    else:
      ip = '---'
    response = run_uci(z)
    if response == "system.vpn.vpn1='1'\n":
      status = True
    else:
      status = False
      ip = "---"
    response = run_uci(name_type)
    data = response.split("\n")
    name = data[0]
    name = name.split("=")
    name = name[1]
    name = name.split("'")
    name = name[1]
    type = data[1]
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
    x = "ifconfig  2>/dev/null tun0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
    z = "uci show system.vpn.vpn2"
    name_type = "uci show system.vpn.vpn2_name;uci show system.vpn.vpn2_type"
    response = run_uci(x)
    if response != "":
      ip = response
    else:
      ip = '---'
    response = run_uci(z)
    if response == "system.vpn.vpn2='1'\n":
      status = True
    else:
      status = False
      ip = "---"
    response = run_uci(name_type)
    data = response.split("\n")
    name = data[0]
    name = name.split("=")
    name = name[1]
    name = name.split("'")
    name = name[1]
    type = data[1]
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

@app.route('/vpn1connect')
def vpn1_connect():
    x = "uci set system.vpn.vpn1=1;uci set system.vpn.vpn2=0;uci commit"
    response = run_uci(x)
    result= {
      "id":1,
      "error":None,
      "result":"200 Ok"
    }
    return(result)

@app.route('/vpn2connect')
def vpn2_connect():
    x = "uci set system.vpn.vpn2=1;uci set system.vpn.vpn1=0;uci commit"
    response = run_uci(x)
    result= {
      "id":1,
      "error":None,
      "result":"200 Ok"
    }
    return(result)


@app.route('/vpn1disconnect')
def vpn1_disconnect():
    x = "uci set system.vpn.vpn1=0;uci commit"
    response = run_uci(x)
    result= {
      "id":1,
      "error":None,
      "result":"200 OK"
    }
    return(result)


@app.route('/vpn2disconnect')
def vpn2_disconnect():
    x = "uci set system.vpn.vpn2=0;uci commit"
    response = run_uci(x)
    result= {
      "id":1,
      "error":None,
      "result":"200 ok"
    }
    return(result)

@app.route('/getvpn1')
def get_vpn1():
    x = "uci show system.vpn.vpn1_name;uci show system.vpn.vpn1_username"
    y = run_uci(x)
    y=y.split("\n")
    try:
        vpn1_name = y[0].split("=")
        vpn1_name = vpn1_name[1].split("'")
        vpn1_name = vpn1_name[1]
    except:
        vpn1_name=""
        pass
    try:
        username = y[1].split("=")
        username = username[1].split("'")
        username = username[1]
    except:
        username=""
        pass

    result = {
    "id":1,
    "result":{"vpn1_name":vpn1_name,"username":username},
    "error":None
    }
    return(result)


@app.route('/getvpn2')
def get_vpn2():
    x = "uci show system.vpn.vpn2_name;uci show system.vpn.vpn2_username"
    y = run_uci(x)
    y=y.split("\n")
    try:
        vpn2_name = y[0].split("=")
        vpn2_name = vpn2_name[1].split("'")
        vpn2_name = vpn2_name[1]
    except:
        vpn2_name=""
        pass
    try:
        username = y[1].split("=")
        username = username[1].split("'")
        username = username[1]
    except:
        username=""
        pass

    result = {
    "id":1,
    "result":{"vpn2_name":vpn2_name,"username":username},
    "error":None
    }
    return(result)

@app.route('/editvpn', methods=['POST'])
def edit_vpn():
  data = request.get_json()
  networkname = data["networkName"]
  username = data["username"]
  password = data["password"]
  cardno = data["cardno"]
  uci1 = "uci set system.vpn.vpn1_name="+networkname+";uci set system.vpn.vpn1_username="+username
  uci2 = "uci set system.vpn.vpn2_name="+networkname+";uci set system.vpn.vpn2_username="+username
  if cardno == 1:
      response = run_uci(uci1)
      save_username_vpn1(username,password)
  else:
      response = run_uci(uci2)
      save_username_vpn2(username,password)
  return("Saved")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Speed Boost>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

@app.route('/speedbooston')
def speedboost_on():
    uci = "uci set system.custom.speedboost='1';uci set system.custom.loadbalancing='0'; uci commit"
    response = run_uci(uci)
    data = "SpeedBoost On"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/speedboostoff')
def speedboost_off():
    uci = "uci set system.custom.speedboost='0'; uci commit"
    response = run_uci(uci)
    data = "SpeedBoost Off"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Load Balancing>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/loadbalancingon')
def loadbalancing_on():
    uci = "uci set system.custom.loadbalancing='1'; uci set system.custom.speedboost='0'; uci commit"
    response = run_uci(uci)
    data = "load balancing on"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/loadbalancingoff')
def loadbalancing_off():
    uci = "uci set system.custom.loadbalancing='0'; uci commit"
    response = run_uci(uci)
    data = "load balancing off"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)


@app.route('/loadbalancingstatus')
def loadbalancing_status():
    uci = "uci show system.custom.loadbalancing"
    response = run_uci(uci)
    x=response.split(".")
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
    uci = "uci set system.custom.static_load=0;uci commit"
    response = run_uci(uci)
    status = "Dynamic On"
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)


@app.route('/lboff')
def lb_off():
    uci = "uci set system.custom.static_load=1;uci commit"
    response = run_uci(uci)
    status = "Static On"
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)


@app.route('/lbstatus')
def lb_status():
    uci = "uci show system.custom.static_load"
    response = run_uci(uci)
    y_new= response.split("=")
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
  uci1 = "uci show system.wan_internet.eth1;uci show network.wan.multipath"
  y = run_uci(uci1)
  list1=[]
  #>>>>>>>>wan1>>>>>>>>>
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
      uci11 = "uci show system.wan_name.eth1;"
      y = run_uci(uci11)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci111 = "uci show mwan3.wan.enabled;uci show mwan3.wan_m1_w1.weight"
      y = run_uci(uci111)
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
      result = [y1,"WAN 1",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>wan2>>>>>>>>>>>>>>>>>>
  uci2 = "uci show system.wan_internet.eth2;uci show network.wan2.multipath"
  y = run_uci(uci2)
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
      uci21 = "uci show system.wan_name.eth2"
      y = run_uci(uci21)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci211 = "uci show mwan3.wan2.enabled;uci show mwan3.wan2_m1_w1.weight"
      y = run_uci(uci211)
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
      result = [y1,"WAN 2",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>>wan3>>>>>>>>>>>>>>>
  uci3 =  "uci show system.wan_internet.eth3;uci show network.wan3.multipath"
  y = run_uci(uci3)
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
      uci31 = "uci show system.wan_name.eth3;"
      y = run_uci(uci31)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci311 = "uci show mwan3.wan3.enabled;uci show mwan3.wan3_m1_w1.weight"
      y = run_uci(uci311)
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
      result = [y1,"WAN 3",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>wan4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  uci4 = "uci show system.wan_internet.eth4;uci show network.wan4.multipath"
  y = run_uci(uci4)
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
      uci41 = "uci show system.wan_name.eth4;"
      y = run_uci(uci41)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci411 = "uci show mwan3.wan4.enabled;uci show mwan3.wan4_m1_w1.weight"
      y = run_uci(uci411)
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
      result = [y1,"WAN 4",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>>>wan5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  uci5 = "uci show system.wan_internet.eth5;uci show network.wan5.multipath"
  y = run_uci(uci5)
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
      uci51 = "uci show system.wan_name.eth5;"
      y = run_uci(uci51)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci511 = "uci show mwan3.wan5.enabled;uci show mwan3.wan5_m1_w1.weight"
      y = run_uci(uci511)
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
      result = [y1,"WAN 5",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>wan6>>>>>>>>>>>>>>>>>>>>>>>>
  uci6 = "uci show system.wan_internet.eth6;uci show network.wan6.multipath"
  y = run_uci(uci6)
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
      uci61 = "uci show system.wan_name.eth6;"
      y = run_uci(uci61)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci611 = "uci show mwan3.wan6.enabled;uci show mwan6.wan_m1_w1.weight"
      y =run_uci(uci611)
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
      result = [y1,"WAN 6",status,weight]
      list1.append(result)
  else:
    list1
#>>>>>>>>>>>>>>>>>>>>>wan7>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  uci7 = "uci show system.wan_internet.wlan0;uci show network.wwan.multipath"
  y = run_uci(uci7)
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
      uci71 = "uci show system.wan_name.wlan0;"
      y = run_uci(uci71)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci711 = "uci show mwan3.wwan.enabled;uci show mwan3.wwan_m1_w1.weight"
      y = run_uci(uci711)
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
      result = [y1,"WWAN",status,weight]
      list1.append(result)
  else:
    list1
  jsonObj = json.dumps(list1)
  return(jsonObj)



@app.route('/setloadbalance', methods=['POST'])
def set_loadbalance():
  data = request.get_json()
  print(data)
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
              uci1 = "uci set mwan3.wan_m1_w1.weight="+str(wan_weight[i])+";uci commit"
              y = run_uci(uci1)
              x = "Success"
         if(wan_name[i])=="wan2":
              uci2 = "uci set mwan3.wan2_m1_w1.weight="+str(wan_weight[i])+";uci commit"
              y = run_uci(uci2)
              x = "Success"
         if(wan_name[i])=="wan3":
              uci3 = "uci set mwan3.wan3_m1_w1.weight="+str(wan_weight[i])+";uci commit"
              y = run_uci(uci3)
              x = "Success"
         if(wan_name[i])=="wan4":
              uci4 = "uci set mwan3.wan4_m1_w1.weight="+str(wan_weight[i])+";uci commit"
              y = run_uci(uci4)
              x = "Success"
         if(wan_name[i])== "wan5":
              uci5 = "uci set mwan3.wan5_m1_w1.weight="+str(wan_weight[i])+";uci commit"
              y = run_uci(uci5)
              x = "Success"
         if(wan_name[i])== "wan6":
              uci6 = "uci set mwan3.wan6_m1_w1.weight="+str(wan_weight[i])+";uci commit"
              y = run_uci(uci6)
              x = "Success"
         if (wan_name[i])=="wwan":
              uci7 = "uci set mwan3.wwan_m1_w1.weight="+str(int(wan_weight[i]))+";uci commit"
              y = run_uci(uci7)
              x = "Success"
  else:
    x = "failed"
  result = {
    "result":x
  }
  return(result)


@app.route('/setlbinterface', methods=['POST'])
def set_lbinterface():
  data = request.get_json()
  checkedlist = []
  uncheckedlist = []
  print(data)
  for i in range (len(data)):
    if(data[i]["checked"]) == True:
        checkedlist.append(data[i])
    else:
        uncheckedlist.append(data[i])
  wan_name_enable = []
  for i in range (len(checkedlist)):
    wan_name_enable.append(checkedlist[i]["interfaceName"])
  for i in range (len(wan_name_enable)):
    if wan_name_enable[i] == "wan1":
      wan_name_enable[i] = "wan"
    if wan_name_enable[i] == "wwan":
      wan_name_enable[i] = "wwan"
    
    uci1 = "uci set mwan3."+wan_name_enable[i]+".enabled=1;uci commit"
    y = run_uci(uci1)

  wan_name_disable=[]
  for i in range (len(uncheckedlist)):
    wan_name_disable.append(uncheckedlist[i]["interfaceName"])


  for i in range (len(wan_name_disable)):
    print(wan_name_disable[i])
    if wan_name_disable[i] == "wan1":
      wan_name_disable[i] = "wan"
    if wan_name_disable[i] == "wwan":
      wan_name_disable[i] = "wwan"
    
    uci2 = "uci set mwan3."+wan_name_disable[i]+".enabled=0;uci commit"
    y = run_uci(uci2)
  return("200 Ok")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WAN PAGE STARTS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/wan1ip')
def wan1_ip():
    uci = "uci show system.wan_name.eth1;uci show system.wan_ip.eth1;cat /sys/class/net/eth1/address;uci show network.wan.proto"
    x = run_uci(uci)
    if x=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
    else:
        y=x
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
    mac = mac.upper()
    if mac == 'network.wan.proto'.upper():
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
    uci = "uci show system.wan_internet.eth1;uci show network.wan.disabled"
    y = run_uci(uci)
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


@app.route('/disconnectwan1')
def disconnect_wan1():
    uci = "uci set network.wan.disabled='1';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)



@app.route('/connectwan1')
def connect_wan1():
    uci = "uci set network.wan.disabled='0';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
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
  uci = "uci set network.wan.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
  if contype == 'PPPoE':
    y = run_uci(uci)
    status = "connected"
  else:
    uci2 = "uci del network.wan.username;uci del network.wan.password;uci set network.wan.proto='dhcp';uci set network.wan.metric='1';uci commit"
    y = run_uci(uci2)
    status = "connected"
  result = {
       'status':status
     }
  return(result)


@app.route('/wan2ip')
def wan2_ip():
    uci = "uci show system.wan_name.eth2;uci show system.wan_ip.eth2;cat /sys/class/net/eth2/address;uci show network.wan2.proto"
    x = run_uci(uci)
    y = x
    if x=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
    else:
        y=x
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
    mac = mac.upper()
    if mac == 'network.wan2.proto'.upper():
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
    uci = "uci show system.wan_internet.eth2;uci show network.wan2.disabled"
    y = run_uci(uci)
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


@app.route('/disconnectwan2')
def disconnect_wan2():
    uci = "uci set network.wan2.disabled='1';uci commit;/etc/init.d/network restart"
    y = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/connectwan2')
def connect_wan2():
    uci = "uci set network.wan2.disabled='0';uci commit;/etc/init.d/network restart"
    y = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
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
  uci1 = "uci set network.wan2.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
  if contype == 'PPPoE':
    y = run_uci(uci1)
    status = "connected"
  else:
    uci2 = "uci del network.wan2.username;uci del network.wan2.password;uci set network.wan2.proto='dhcp';uci set network.wan2.metric='2';uci commit"
    y = run_uci(uci2)
    status = "connected"
  result = {
       'status':status
     }
  return(result)


@app.route('/wan3ip')
def wan3_ip():
    uci = "uci show system.wan_name.eth3;uci show system.wan_ip.eth3;cat /sys/class/net/eth3/address;uci show network.wan3.proto"
    x = run_uci(uci)
    y = x
    if x=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"

    else:
        y=x
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
    mac = mac.upper()
    if mac == 'network.wan3.proto'.upper():
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
    uci = "uci show system.wan_internet.eth3;uci show network.wan3.disabled"
    y = run_uci(uci)
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


@app.route('/disconnectwan3')
def disconnect_wan3():
    uci = "uci set network.wan3.disabled='1';uci commit;/etc/init.d/network restart"
    y = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/connectwan3')
def connect_wan3():
    uci = "uci set network.wan3.disabled='0';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/editwan3network', methods=['POST'])
def edit_wan3():
  data = request.get_json()
  contype =data['conType']
  username=data['username']
  password=data['password']
  string1 = "uci set network.wan3.username="
  string2 = "uci set network.wan3.password="
  uci1 = "uci set network.wan3.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
  if contype == 'PPPoE':
    y = run_uci(uci1)
    status = "connected"
  else:
    uci2 = "uci del network.wan3.username;uci del network.wan3.password;uci set network.wan3.proto='dhcp';uci set network.wan3.metric='3';uci commit"
    y = run_uci(uci2)
    status = "connected"
  result = {
       'status':status
     }
  return(result)


@app.route('/wan4ip')
def wan4_ip():
    uci = "uci show system.wan_name.eth4;uci show system.wan_ip.eth4;cat /sys/class/net/eth4/address;uci show network.wan4.proto"
    x = run_uci(uci)
    y = x
    if x=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"

    else:
        y=x
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
    mac = mac.upper()
    if mac == 'network.wan4.proto'.upper():
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
    uci = "uci show system.wan_internet.eth4;uci show network.wan4.disabled"
    y = run_uci(uci)
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


@app.route('/disconnectwan4')
def disconnect_wan4():
    uci = "uci set network.wan4.disabled='1';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)



@app.route('/connectwan4')
def connect_wan4():
    uci = "uci set network.wan4.disabled='0';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
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
  uci1 = "uci set network.wan4.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
  if contype == 'PPPoE':
    y = run_uci(uci1)
    status = "connected"
  else:
    uci2 = "uci del network.wan4.username;uci del network.wan4.password;uci set network.wan4.proto='dhcp';uci set network.wan4.metric='4';uci commit"
    y = run_uci(uci2)
    status = "connected"
  result = {
       'status':status
     }
  return(result)


@app.route('/wan5ip')
def wan5_ip():
    uci = "uci show system.wan_name.eth5;uci show system.wan_ip.eth5;cat /sys/class/net/eth5/address;uci show network.wan5.proto"
    x = run_uci(uci)
    y = x
    if x=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
    else:
        y=x
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
    mac = mac.upper()
    if mac == 'network.wan5.proto'.upper():
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
    uci = "uci show system.wan_internet.eth5;uci show network.wan5.disabled"
    y = run_uci(uci)
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
    uci = "uci set network.wan5.disabled='1';uci commit;/etc/init.d/network restart"
    y = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/connectwan5')
def connect_wan5():
    uci = "uci set network.wan5.disabled='0';uci commit;/etc/init.d/network restart"
    y = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
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
  uci1 = "uci set network.wan5.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
  if contype == 'PPPoE':
    response = run_uci(uci1)
    status = "connected"
  else:
    uci2 = "uci del network.wan5.username;uci del network.wan5.password;uci set network.wan5.proto='dhcp';uci set network.wan5.metric='5';uci commit"
    response = run_uci(uci2)
    status = "connected"
  result = {
       'status':status
     }
  return(result)


@app.route('/wan6ip')
def wan6_ip():
    uci = "uci show system.wan_name.eth6;uci show system.wan_ip.eth6;cat /sys/class/net/eth6/address;uci show network.wan6.proto"
    y = run_uci(uci)
    if y=="":
        customName = "Unavailable"
        ip =  "Unavailable"
        proto= "Unavailable"
        mac = "Unavailable"
        
    else:
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
        mac = mac.upper()
        if mac == 'network.wan6.proto'.upper():
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
    uci = "uci show system.wan_internet.eth6;uci show network.wan6.disabled"
    y = run_uci(uci)
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
    uci = "uci set network.wan6.disabled='1';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/connectwan6')
def connect_wan6():
    uci = "uci set network.wan6.disabled='0';uci commit;/etc/init.d/network restart"
    response = run_uci(uci)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
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
  uci1 = "uci set network.wan6.proto='pppoe';"+string1+username+";"+string2+password+";"+"uci commit;/etc/init.d/network restart"
  if contype == 'PPPoE':
    response = run_uci(uci1)
    status = "connected"
  else:
    uci2 = "uci del network.wan6.username;uci del network.wan6.password;uci set network.wan6.proto='dhcp';uci set network.wan6.metric='6';uci commit"
    response = run_uci(uci2)
    status = "connected"
  result = {
       'status':status
     }

  return(result)
# >>>>>>>>>>>Wireless Wan Interface >>>>>>>>>>>


@app.route('/wifion')
def wirelessnetwork_on():
  uci = "uci set wireless.radio0.disabled='0'; uci commit; wifi up radio0;/etc/init.d/network restart"
  response = run_uci(uci)
  data = "wifi on"
  result = {
        "id":1,
        "result":data,
        "error": None
    }
  return(result)



@app.route('/wifioff')
def wirelessnetwork_off():
  uci = "uci set wireless.radio0.disabled='1'; uci commit; wifi down radio0;/etc/init.d/network restart"
  response = run_uci(uci)
  data = "wifi off"
  result = {
        "id":1,
        "result":data,
        "error": None
    }
  return(result)



@app.route('/wifistatus')
def wifistatus():
  uci = "uci show wireless.radio0.disabled"
  y = run_uci(uci)
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
    uci1 = "uci show system.wan_name.wlan0;uci show system.wan_ip.wlan0;cat /sys/class/net/wlan0/address;uci show network.wlan0.proto"
    y = run_uci(uci1)
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
    mac7 = mac7.upper()
    try:
      proto_initial = y_new[3].split("\n")
      proto_initial = proto_initial[0].split("'")
      proto7 = proto_initial[1]
    except:
      proto7=""
    uci2 = "uci show wireless.wifinet1.ssid"
    y = run_uci(uci2)
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
    uci = "uci show system.wan_internet.wlan0"
    y = run_uci(uci)
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

@app.route('/add_network', methods=['POST'])
def add_network():
  data = request.get_json()
  name=data['networkName']
  security=data['securityMode']
  password=data['password']
  uci1 = "uci set wireless.wifinet1.encryption='psk2';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
  uci2 = "uci set wireless.wifinet1.encryption='psk-mixed';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
  uci3 = "uci set wireless.wifinet1.encryption='none';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
  if security == 'WPA/WPA2 PSK':
    response = run_uci(uci1)
  elif security == "mixed WPA/WPA2 PSK":
    response = run_uci(uci2)
  else:
    response = run_uci(uci3)
  return("200 ok")


@app.route('/scanwwan')
def scan():
  uci = "iwinfo wlan0-3 scan | grep 'ESSID\|Encryption' | awk '{ print $2,$3}'"
  y = run_uci(uci)
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
  uci = "iwinfo wlan0 scan | grep 'ESSID\|Encryption' | awk '{ print $2,$3}'"
  y = run_uci(uci)
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
  name=data['networkName']
  security=data['securityMode']
  password=data['password']
  uci1 = "uci set wireless.wifinet1.encryption='psk2';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";uci commit;wifi up radio0"
  uci2 = "uci set wireless.wifinet1.encryption='psk-mixed';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
  uci3 = "uci set wireless.wifinet1.encryption='none';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"wifi up radio0"
  if security == 'WPA2 PSK':
    response = run_uci(uci1)
    result = {
      "id":1,
      "result":"200 ok",
      "error":None
    }
  elif security == "mixed WPA/WPA2":
    response = run_uci(uci2)
    result = {
      "id":1,
      "result":"200 ok",
      "error":None
    }
  else:
    password = ""
    response = run_uci(uci3)
    result = {
      "id":1,
      "result":"200 ok",
      "error":None
    }

  return(result)


#>>>>>>>>>To TEST>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/test')
def test_test():
    uci1 =  "uci show system.wan_name.eth1;uci show system.wan_ip.eth1;cat /sys/class/net/eth1/address;uci show network.wan.proto"
    y = run_uci(uci1)
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
    uci2 = "uci show system.wan_name.eth2;uci show system.wan_ip.eth2;cat /sys/class/net/eth2/address;uci show network.wan2.proto"
    y = run_uci(uci2)
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
    uci3 = "uci show system.wan_name.eth3;uci show system.wan_ip.eth3;cat /sys/class/net/eth3/address;uci show network.wan3.proto"
    y = run_uci(uci3)
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
    uci4 = "uci show system.wan_name.eth4;uci show system.wan_ip.eth4;cat /sys/class/net/eth4/address;uci show network.wan4.proto"
    y = run_uci(uci4)
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
    uci5 = "uci show system.wan_name.eth5;uci show system.wan_ip.eth5;cat /sys/class/net/eth5/address;uci show network.wan5.proto"
    y = run_uci(uci5)
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
    uci6 = "uci show system.wan_name.eth6;uci show system.wan_ip.eth6;cat /sys/class/net/eth6/address;uci show network.wan6.proto"
    y = run_uci(uci6)
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
    uci7 = "uci show system.wan_name.wlan0;uci show system.wan_ip.wlan0;cat /sys/class/net/wlan0/address;uci show network.wlan0.proto"
    y = run_uci(uci7)
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



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Wireless Settings>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Network Storage>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route('/nason')
def nas_on():
    uci = "uci set system.nas.nas=1;uci set system.nas.nas_change=1;uci commit"
    response = run_uci(uci)
    status = "Enabled"
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)

@app.route('/nasoff')
def nas_off():
    uci = "uci set system.nas.nas=0;uci set system.nas.nas_change=1;uci commit"
    response = run_uci(uci)
    status = "disabled"
    result = {
      "id":1,
      "result":status,
      "error":None
    }
    return(result)

@app.route('/nasstatus')
def nas_status():
    uci = "uci show system.nas.nas"
    x = run_uci(uci)
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
  #uci =  #--->Add Script Here""
  # run run_uci(uci) fun
  return("result")
  
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Network Ends>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Speed Boost>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/setspeedboost', methods=['POST'])
def set_speedboost():
  data = request.get_json()
  interface=data['interface']
  if interface == 'wan1':
    interface='wan'
  if interface == 'wwan':
    interface='wwan'
  isp = data['isp']
  statustype = data['statusType']
  uci1 = "uci set network."+interface+".multipath=on;uci commit"
  if statustype == True:
    response = run_uci(uci1)
    x = 200
    if x == 200:
      result = {
      "id":1,
      "result":"Enabled",
      "error":None
      }
  else:
    uci2 = "uci set network."+interface+".multipath=off;uci commit"
    response = run_uci(uci2)
    x = 200
    if x == 200:
      result = {
      "id":1,
      "result":"disabled",
      "error":None
      }
  return(result)


@app.route('/getspeedboost')
def get_speedboost():
  uci1 = "uci show system.wan_internet.eth1;uci show network.wan.multipath"
  y = run_uci(uci1)
  list1=[]
  #>>>>>>>>wan1>>>>>>>>>
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
      uci2 = "uci show system.wan_name.eth1;"
      y = run_uci(uci2)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci3 = "uci show mwan3.wan.enabled;uci show mwan3.wan_m1_w1.weight"
      y = run_uci(uci3)
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
       "interface": [y1,"WAN 1",status,toggle_stat,weight]
      }
      list1.append(result)
  else:
    list1

  #>>>>>>>>>>>wan2>>>>>>>>>>>>>>
  uci4 = "uci show system.wan_internet.eth2;uci show network.wan2.multipath"
  y = run_uci(uci4)
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
      uci5 = "uci show system.wan_name.eth2"
      y = run_uci(uci5)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci6 = "uci show mwan3.wan2.enabled;uci show mwan3.wan2_m1_w1.weight"
      y = run_uci(uci6)
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
       "interface": [y1,"WAN 2",status,toggle_stat,weight]
      }
      list1.append(result)

  else:
    list1
  #>>>>>wan3>>>>>>>>>>>>>>>>>>
  uci7 = "uci show system.wan_internet.eth3;uci show network.wan3.multipath"
  y = run_uci(uci7)
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
      uci8 = "uci show system.wan_name.eth3"
      y = run_uci(uci8)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci9 = "uci show mwan3.wan3.enabled;uci show mwan3.wan3_m1_w1.weight"
      y = run_uci(uci9)
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
       "interface": [y1,"WAN 3",status,toggle_stat,weight]
      }
      list1.append(result)
  else:
    list1
#>>>>>>>>>wan4>>>>>>>>>>>>>>>>>>>>
  uci10 = "uci show system.wan_internet.eth4;uci show network.wan4.multipath"
  y =run_uci(uci10)
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
      uci11 = "uci show system.wan_name.eth4"
      y = run_uci(uci11)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci12 = "uci show mwan3.wan4.enabled;uci show mwan3.wan4_m1_w1.weight"
      y = run_uci(uci12)
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
       "interface": [y1,"WAN 4",status,toggle_stat,weight]
      }
      list1.append(result)

  else:
    list1

#>>>>>>>>>>>wan5>>>>>>>>>>>>>>>>>>>>>>
  uci12 = "uci show system.wan_internet.eth5;uci show network.wan5.multipath"
  y = run_uci(uci12)
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
      uci13 = "uci show system.wan_name.eth5"
      y = run_uci(uci13)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci14 = "uci show mwan3.wan5.enabled;uci show mwan3.wan5_m1_w1.weight"
      y = run_uci(uci14)
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
       "interface": [y1,"WAN 5",status,toggle_stat,weight]
      }
      list1.append(result)

  else:
    list1
#>>>>>>>>>>>wan6>>>>>>>>>>>>>>>>>>>>>>>>>
  uci15 = "uci show system.wan_internet.eth6;uci show network.wan6.multipath"
  y = run_uci(uci15)
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
      uci16 = "uci show system.wan_name.eth6"
      y = run_uci(uci16)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci17 = "uci show mwan3.wan6.enabled;uci show mwan3.wan6_m1_w1.weight"
      y = run_uci(uci17)
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
       "interface": [y1,"WAN 6",status,toggle_stat,weight]
      }
      list1.append(result)

  else:
    list1
#>>>>>>>>>>>>>>>wwan>>>>>>>>>>>>>>>>>>>>>>>>>>
  uci18 = "uci show system.wan_internet.wlan0;uci show network.wwan.multipath"
  y = run_uci(uci18)
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
      uci19 = "uci show system.wan_name.wlan0"
      y = run_uci(uci19)
      y = y.split("=")
      y1 = y[1].strip("''\n")
      uci20 = "uci show mwan3.wwan.enabled;uci show mwan3.wwan_m1_w1.weight"
      y = run_uci(uci20)
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
       "interface": [y1,"WWAN",status,toggle_stat,weight]
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

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Parental Control>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/parentalon')

def parental_on():
  x = "uci set system.pc.parental='1';system.pc.parental_change='1';uci commit"
  response = run_uci(x)
  return("200 ok")



@app.route('/parentaloff')

def parental_off():
  x = "uci set system.pc.parental='0';system.pc.parental_change='1';uci commit"
  response = run_uci(x)
  return("200 ok")



@app.route('/ualevelon')

def ualevel_on():
    x="uci set system.pc.parental_ua='1';system.pc.parental_change='1';uci commit"
    response = run_uci(x)
    return("200 ok")


@app.route('/ualeveloff')

def ualevel_off():
    x="uci set system.pc.parental_ua='0';system.pc.parental_change='1';uci commit"
    response = run_uci(x)
    return("200 ok")



@app.route('/ualevelstatus')

def ualevel_status():
    uci = "uci show system.pc.parental_ua"
    x = run_uci(uci)
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
    x="uci set system.pc.parental_u='1';system.pc.parental_change='1';uci commit"
    response = run_uci(x)
    return("200 ok")


@app.route('/uleveloff')

def ulevel_off():
    x="uci set system.pc.parental_u='0';system.pc.parental_change='1';uci commit"
    response = run_uci(x)
    return("200 ok")


@app.route('/ulevelstatus')

def ulevel_status():
    uci = "uci show system.pc.parental_u"
    x = run_uci(uci)
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
    x="uci set system.pc.parental_a='1';system.pc.parental_change='1';uci commit"
    response = run_uci(x)
    return("200 ok")


@app.route('/aleveloff')

def alevel_off():
    x="uci set system.pc.parental_a='0';system.pc.parental_change='1';uci commit"
    response = run_uci(x)
    return("200 ok")


@app.route('/alevelstatus')

def alevel_status():
     uci = "uci show system.pc.parental_a"
     x = run_uci(uci)
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
    uci = "sh /root/adblock_report.sh"
    incoming_data = run_uci(uci)
    incoming_data = incoming_data.split("\n",15)
    data_list=[]
    for value in incoming_data:
      data = value.split(" ")
      data_list.append(data)
    json_string = json.dumps(data_list)
    return(json_string)


@app.route('/editblacklist')

def edit_blacklist():
     uci = "cat /etc/adblock/adblock.blacklist"
     x = run_uci(uci)
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
     uci = "cat /etc/adblock/adblock.whitelist"
     x = run_uci(uci)
     y = x.split("\n")
     del y[-1]
     result = {
     "result":y,
     "error":None
     }
     return(result)


@app.route('/deletewhitelist', methods=['POST'])
def delete_whitelist():
  data = request.get_data()
  data_new=data.decode('UTF-8')
  uci1 = "cp /etc/adblock/adblock.whitelist /app/api/adw.txt"
  y = run_uci(uci1)
  a_file = open("adw.txt", "r")
  lines = a_file.readlines()
  a_file.close()
  new_file = open("adw.txt", "w")
  for line in lines:
    if line.strip("\n") != data_new:
        new_file.write(line)
  new_file.close()
  uci2 = "cp /app/api/adw.txt  /etc/adblock/adblock.whitelist"
  y = run_uci(uci2)
  uci3 = "/etc/init.d/adblock reload"
  y = run_uci(uci3)
  return("deleted")

@app.route('/savewhitelist',methods=['POST'])

def save_whitelist():
  data = request.get_data()
  data_new=data.decode('UTF-8')
  script = 'echo '+data_new+'>>/etc/adblock/adblock.whitelist'
  y = run_uci(script)
  uci3 = "/etc/init.d/adblock reload"
  y = run_uci(uci3)
  return("Saved")



@app.route('/saveblacklist', methods=['POST'])
def save_blacklist():
  data = request.get_data()
  data_new=data.decode('UTF-8')
  uci1 =   "echo "+data_new+">>/etc/adblock/adblock.blacklist"
  y = run_uci(uci1)
  uci2 = "/etc/init.d/adblock reload"
  return("saved")


@app.route('/deleteblacklist', methods=['POST'])
def delete_blacklist():
  data = request.get_data()
  data_new=data.decode('UTF-8')
  uci1 = "cp /etc/adblock/adblock.blacklist /app/api/adb.txt"
  y = run_uci(uci1)
  a_file = open("adb.txt", "r")
  lines = a_file.readlines()
  a_file.close()
  new_file = open("adb.txt", "w")
  for line in lines:
    if line.strip("\n") != data_new:
        new_file.write(line)
  new_file.close()
  uci2 = "cp /app/api/adb.txt  /etc/adblock/adblock.blacklist"
  y = run_uci(uci2)
  uci3 = "/etc/init.d/adblock reload"
  y = run_uci(uci3)
  return("deleted")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LAN MI ROUTER>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/getlan', methods=['GET'])
def get_lan():
  try:
    pass
  except:
    pass
  uci1 = "uci show network.lan.ipaddr;uci show network.lan.netmask;cat /sys/class/net/eth0/address;uci show dhcp.lan.start;uci show dhcp.lan.limit;uci show dhcp.lan.dynamicdhcp;uci show network.lan.gateway"
  y = run_uci(uci1)
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
    mac = mac.upper()
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


@app.route('/test2')
def client_test():
  try:
    pass
  except:
    pass
  uci1 = "cat /tmp/dhcp.leases | awk '{ print $2,$3}' | wc -l"
  rows = run_uci(uci1)
  rows=int(rows)
  uci2 = "cat /tmp/dhcp.leases | awk '{ print $2,$3,$4}'"
  incoming_data= run_uci(uci2)
  incoming_data = incoming_data.split("\n",rows)
  data_list=[]
  for value in incoming_data:
    data = value.split(" ")
    data_list.append(data)
  z= data_list
  z_new = data_list.pop()
  for i in range(len(z)):
      for j in range(len(z)):
          z[i][0]=z[i][0].upper()
  json_string = json.dumps(z)
  return(json_string)

######>>>>>>>>**********************Wireless Setings MI Router********************************>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@app.route('/wifinet1')
def wifi_net1():
    try:
      pass
    except:
      pass
    uci1 = "uci show wireless.wifinet1.ssid;uci show wireless.wifinet1.encryption"
    y = run_uci(uci1)
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
      pass
    except:
      pass
    uci1 = "uci show wireless.wifinet2.ssid;uci show wireless.wifinet2.encryption"
    y = run_uci(uci1)
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
      pass
    except:
      pass

    uci1 = "uci show wireless.wifinet3.ssid;uci show wireless.wifinet3.encryption"
    y = run_uci(uci1)
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
      pass
    except:
      pass

    uci1 = "uci show wireless.wifinet4.ssid;uci show wireless.wifinet4.encryption"
    y = run_uci(uci1)
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
      pass
    except:
      pass

    uci1 = "uci show wireless.wifinet1.disabled"
    y = run_uci(uci1)
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
      pass
    except:
      pass
    uci1 = "uci show wireless.wifinet2.disabled"
    y = run_uci(uci1)
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
      pass
    except:
      pass

    uci1 = "uci show wireless.wifinet3.disabled"
    y = run_uci(uci1)
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
      pass
    except:
      pass

    uci1 = "uci show wireless.wifinet4.disabled"
    y = run_uci(uci1)
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


@app.route('/wirelessstatus')
def wireless_status():
    try:
      pass
    except:
      pass
    uci = "uci show system.custom.wireless_set"
    y= run_uci(uci)
    x=y.split(".")
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


@app.route('/wifinet1disconnect')
def disconnect_wifi1():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet1.disabled=1;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 Ok",
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet2disconnect')
def disconnect_wifi2():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet2.disabled=1;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 oK",
    "error":None
    }
    return(data_dummy)
@app.route('/wifinet3disconnect')
def disconnect_wifi3():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet3.disabled=1;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet4disconnect')
def disconnect_wifi4():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet4.disabled=1;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/wifinet1connect')
def connect_wifi1():

    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet1.disabled=0;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 Ok",
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet2connect')
def connect_wifi2():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet2.disabled=0;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet3connect')
def connect_wifi3():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet3.disabled=0;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)

@app.route('/wifinet4connect')
def connect_wifi4():
    try:
      pass
    except:
      pass
    uci1 = "uci set wireless.wifinet4.disabled=0;uci commit;wifi up radio0"
    y = run_uci(uci1)
    data_dummy = {
    "id":"1",
    "result":"200 ok",
    "error":None
    }
    return(data_dummy)


@app.route('/wifinet1addnetwork', methods=['POST'])
def add_network1():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  uci1 = "uci set wireless.wifinet1.encryption='psk2';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"uci commit;wifi up radio0"
  uci2 = "uci set wireless.wifinet1.encryption='psk-mixed';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"uci commit"
  uci3 = "uci set wireless.wifinet1.encryption='none';uci set wireless.wifinet1.ssid="+name+";"+"uci set wireless.wifinet1.key="+password+";"+"uci commit"
  if security == 'WPA/WPA2':
    y = run_uci(uci1)
    result = {
      "result":"200 ok"
    }
  elif security == "mixed WPA/WPA2":
    y = run_uci(uci2)
    result = {
      "result":"200 ok"
    }
  else:
    y = run_uci(uci3)
    result = {
      "result":"200 ok"
    }
  return(result)



@app.route('/wifinet2addnetwork', methods=['POST'])
def add_network2():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  uci1 = "uci set wireless.wifinet2.encryption='psk2';uci set wireless.wifinet2.ssid="+name+";"+"uci set wireless.wifinet2.key="+password+";"+"uci commit"
  uci2 = "uci set wireless.wifinet2.encryption='psk-mixed';uci set wireless.wifinet2.ssid="+name+";"+"uci set wireless.wifinet2.key="+password+";"+"uci commit"
  uci3 = "uci set wireless.wifinet2.encryption='none';uci set wireless.wifinet2.ssid="+name+";"+"uci set wireless.wifinet2.key="+password+";"+"uci commit"
  if security == 'WPA/WPA2':
    y = run_uci(uci1)
    result = {
      "result":"200 ok"
    }
  elif security == "mixed WPA/WPA2":
    y = run_uci(uci2)
    result = {
      "result":"200 ok"
    }
  else:
    y = run_uci(uci3)
    result = {
      "result":"200 ok"
    }
  return(result)

@app.route('/wifinet3addnetwork', methods=['POST'])
def add_network3():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  uci1 = "uci set wireless.wifinet3.encryption='psk2';uci set wireless.wifinet3.ssid="+name+";"+"uci set wireless.wifinet3.key="+password+";"+"uci commit"
  uci2 = "uci set wireless.wifinet3.encryption='psk-mixed';uci set wireless.wifinet3.ssid="+name+";"+"uci set wireless.wifinet3.key="+password+";"+"uci commit"
  uci3 = "uci set wireless.wifinet3.encryption='none';uci set wireless.wifinet3.ssid="+name+";"+"uci set wireless.wifinet3.key="+password+";"+"uci commit"
  if security == 'WPA/WPA2':
    y = run_uci(uci1)
    result = {
      "result":"200 ok"
    }
  elif security == "mixed WPA/WPA2":
    y = run_uci(uci2)
    result = {
      "result":"200 ok"
    }
  else:
    y = run_uci(uci3)
    result = {
      "result":"200 ok"
    }
  return(result)

@app.route('/wifinet4addnetwork', methods=['POST'])
def add_network4():
  data = request.get_json()
  name=data['ssid']
  security=data['securityMode']
  password=data['password']
  uci1 = "uci set wireless.wifinet4.encryption='psk2';uci set wireless.wifinet4.ssid="+name+";"+"uci set wireless.wifinet4.key="+password+";"+"uci commit"
  uci2 = "uci set wireless.wifinet4.encryption='psk-mixed';uci set wireless.wifinet4.ssid="+name+";"+"uci set wireless.wifinet4.key="+password+";"+"uci commit"
  uci3 = "uci set wireless.wifinet4.encryption='none';uci set wireless.wifinet4.ssid="+name+";"+"uci set wireless.wifinet4.key="+password+";"+"uci commit"
  if security == 'WPA/WPA2':
    y = run_uci(uci1)
    result = {
      "result":"200 ok"
    }
  elif security == "mixed WPA/WPA2":
    y = run_uci(uci2)
    result = {
      "result":"200 ok"
    }
  else:
    y = run_uci(uci3)
    result = {
      "result":"200 ok"
    }
  return(result)


@app.route('/wirelesson')
def wireless_on():
    try:
      pass
    except:
      pass
    uci = "uci set system.custom.wireless_set=1;uci commit"
    y = run_uci(uci)
    data = "wireless On"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)

@app.route('/wirelessoff')
def wireless_off():
    try:
      pass
    except:
      pass
    uci = "uci set system.custom.wireless_set=0;uci commit"
    y = run_uci(uci)
    data = "wireless On"
    result = {
        "id":1,
        "result":data,
        "error": None
    }
    return(result)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Speedtest>>>>>>>>>>>>>>>>>>>>

@app.route('/downloadtest')

def download_test():
  start_timer = time.time()
  uci1 = "cat /sys/class/net/wlan0/statistics/rx_bytes"
  dresult = run_uci(uci1)
  if dresult == '':
          wlan0 = 0
  else:
          wlan0 = float(dresult)
  uci2 = "cat /sys/class/net/eth1/statistics/rx_bytes"
  dresult=run_uci(uci2)
  if dresult == '':
          eth1 = 0
  else:
          eth1 = float(dresult)
  uci3 = "cat /sys/class/net/eth3/statistics/rx_bytes"
  dresult=run_uci(uci3)
  if dresult == '':
          eth3 = 0
  else:
          eth3 = float(dresult)
  uci4 = "cat /sys/class/net/eth2/statistics/rx_bytes"
  dresult = run_uci(uci4)
  if dresult == '':
          eth2new = 0
  else:
          eth2new = float(dresult)

  uci5 =  "cat /sys/class/net/eth4/statistics/rx_bytes"
  dresult= run_uci(uci5)
  if dresult == '':
          eth4 = 0
  else:
          eth4 = float(dresult)
  uci6 = "cat /sys/class/net/eth5/statistics/rx_bytes"
  dresult = run_uci(uci6)
  if dresult == '':
          eth5 = 0
  else:
          eth5 = float(dresult)
  #Eth6>>>>>>>>
  uci7 = "cat /sys/class/net/eth6/statistics/rx_bytes"
  dresult = run_uci(uci7)
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
  uci8 = "cat /sys/class/net/wlan0/statistics/rx_bytes"
  dresult=run_uci(uci8)
  if dresult == '':
          wlan02 = 0
  else:
          wlan02 = float(dresult)
  uci9 = "cat /sys/class/net/eth1/statistics/rx_bytes"
  dresult = run_uci(uci9)
  if dresult == '':
          eth12 = 0
  else:
          eth12 = float(dresult)
  uci10 = "cat /sys/class/net/eth3/statistics/rx_bytes"
  dresult = run_uci(uci10)
  if dresult == '':
          eth32 = 0
  else:
          eth32 = float(dresult)
  uci11 = "cat /sys/class/net/eth2/statistics/rx_bytes"
  dresult = run_uci(uci11)
  if dresult == '':
          eth22new = 0
  else:
          eth22new = float(dresult)
  uci12 = "cat /sys/class/net/eth4/statistics/rx_bytes"
  dresult = run_uci(uci12)
  if dresult == '':
          eth42 = 0
  else:
          eth42 = float(dresult)
  uci13 = "cat /sys/class/net/eth5/statistics/rx_bytes"
  dresult = run_uci(uci13)
  if dresult == '':
          eth52 = 0
  else:
          eth52 = float(dresult)
  #Eth6>>>>>>>>>>>>
  uci14 = "cat /sys/class/net/eth6/statistics/rx_bytes"
  dresult = run_uci(uci14)
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
  uci15 = "uci show system.custom.speedboost"
  y = run_uci(uci15)
  x=y.split(".")
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






if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0',port=5002)