# Openwrt 

## Table of contents
* [General info](#general-info)
* [Build using imagebuilder](#Build-using-imagebuilder)
* [Build Custom packages](#Build-Custom-packages)
* [Host packages for devices in custom feed](#Host-packages-for-devices-in-custom-feed)
* [Build packages using SDK](#Build-packages-using-SDK)
* [Setting up a TFTP server for TFTP](#Setting-up-a-TFTP-server-for-TFTP)
* [OpenVPN server setup](#OpenVPN-server-setup)
* [Router as switch](#Router-as-switch)
* [802.11s Mesh](#802.11s-Mesh)
* [Openwrt on TP Link Archer C7 v5 AC1750](#Openwrt-on-TP-Link-Archer-C7-v5-AC1750)
* [Openwrt on TP Link Archer A7 v5](#Openwrt-on-TP-Link-Archer-A7-v5)
* [Openwrt on TP Link Archer C2600](#Openwrt-on-TP-Link-Archer-C2600)
* [Connecting to a Wireless Network](#Connecting-to-a-Wireless-Network)
* [Luci Web Interface](#Luci-Web-Interface)
* [USB Tethering](#usb-tethering)
* [4G Dongle support](#4G-Dongle-support)
* [Load balancing with multiple WAN interfaces](#Load-balancing-with-multiple-WAN-interfaces)
* [Ad Block](#Ad-Block)
* [Speed Test Ookla and Netperf](#Speed-Test-Ookla-and-Netperf)
* [SQM](#SQM)
* [NAS](#NAS)
* [OpenVPN Client](#OpenVPN-Client)
* [Remote Logging](#Remote-Logging)
* [Other](#other)





## General info


Pre requisites: Knowledge on OpenWrt, vi editor, Basic linux commands.

To write a Readme file on Github:

https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project

https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

Some major tutorials:

https://kenfavors.com/code/how-to-protect-ssh-with-fail2ban/

### Openwrt Table of Hardware

Check devices supported by openwrt 

https://openwrt.org/toh/views/toh_extended_all

### Openwrt firmware selector
https://firmware-selector.openwrt.org

### Flash new image on router 
Place image file in /

Execute command:
```ruby
sysupgrade -v -n -F /image_file_name.img.gz
```


## Build using imagebuilder

### Downloads link
https://downloads.openwrt.org

Download imagebuilder for specific traget from above link.


Decompress the file using following command:
```ruby
tar -xvf filename
```

Go inside the decompressed folder:
```ruby
cd filename
```

Find out available profiles using the command:
```ruby
make info
```

Build for a specific profile with required packages for example:

```ruby
make image PROFILE=rpi-4 PACKAGES="uhttpd uhttpd-mod-ubus libiwinfo-lua luci-base luci-mod-admin-full luci-theme-bootstrap wpad-mesh-wolfssl -wpad-basic -wpad-mini -ppp -ppp-mod-pppoe -kmod-pppoe -ip6tables -odhcp6c -kmod-ipv6 -kmod-ip6tables -odhcpd-ipv6only -odhcpd -iptables -opkg -uclient-fetch -libuclient20160123 -firewall -kmod-ipt-core -kmod-ipt-offload -kmod-nf-conntrack -kmod-nf-flow -kmod-nf-ipt -kmod-nf-reject -dnsmasq"
```

The following website has an example:
https://bmaupin.github.io/wiki/other/openwrt/openwrt-80211s.html


## Build Custom packages

https://forum.openwrt.org/t/solved-add-a-new-package-to-the-source/11542

http://dvblog.soabit.com/building-custom-openwrt-packages-an-hopefully-complete-guide/

https://github.com/mwarning/openwrt-examples/blob/master/README.md

custom package feed:

https://stackoverflow.com/questions/57845074/how-does-one-create-a-custom-package-feed-in-openwrt

https://github.com/plan44/plan44-feed


## Host packages for devices in custom feed






## Build packages using SDK 

For tutorial visit: https://openwrt.org/docs/guide-developer/toolchain/using_the_sdk

### Downloads link
https://downloads.openwrt.org

Download SDK for specific traget from above link.

Decompress the file using following command:
```ruby
tar -xvf filename
```

Go inside the decompressed folder:
```ruby
cd filename
```

If any additional feeds need to be added, add them in "feeds.conf.default" file.

#### Load packages list
```ruby
./scripts/feeds update -a
```

To prepare a single package and its dependencies:
```ruby
./scripts/feeds install <packagename>
```

To make all packages available, again, just like in the buildroot:
```ruby
./scripts/feeds install -a
```

After the Makefile is in place, the usual buildroot commands apply:

* make package/example/download - download the soures of example
* make package/example/prepare - extract the sources, apply patches and download if necessary
* make package/example/compile - compile example, prepare and download if necessary
* make package/example/clean - clean the sourcecode
* make package/index - build a repository index to make the output directory usable as local opkg source


Or, just run make to build everything selected. After the compilation is finished, the generated .ipk files are placed in the bin/packages and bin/targets directories inside the directory you extracted the SDK into.


## Setting up a TFTP server for TFTP]

Link : https://openwrt.org/docs/guide-user/troubleshooting/tftpserver#setting_up_tftp_server

Video example : https://www.youtube.com/watch?v=u8Y5ekdsHlo

## OpenVPN server setup

Referenced from : https://www.cyberciti.biz/faq/ubuntu-20-04-lts-set-up-openvpn-server-in-5-minutes/

```ruby
sudo apt update
sudo apt upgrade

# Get your private ip address ( the shell script automatically finds it, but note it just for reference)
ip a show eth0 | grep inet

# Get your public ip address ( the shell script automatically finds it, but note it just for reference)
dig -4 +short myip.opendns.com @resolver1.opendns.com

# Download the shell script
wget -L https://raw.githubusercontent.com/Dharun2308/myfiles/main/other/openvpn-ubuntu-install.sh

# Make the file executable
chmod -v +x openvpn-ubuntu-install.sh

# Run the script
sudo ./openvpn-ubuntu-install.sh

```

```ruby
# check private IP
# check public IP
# Select port of VPN server
# Select TCP or UDP
# Select DNS server
# Select client name, password option and set password

# start server
sudo systemctl start openvpn@server.service

# stop server
sudo systemctl stop openvpn@server.service

# Restart service after changing any configuration
sudo systemctl restart openvpn@server.service

# To get status
sudo systemctl status openvpn@server.service

# To edit configuration file 
nano /etc/openvpn/server.conf

# To check connection run following commands on client device. Run ping and then check ip on next command
ping -c 4 10.8.0.1
dig TXT +short o-o.myaddr.l.google.com @ns1.google.com
```

```ruby
# To add new user 
sudo ./openvpn-ubuntu-install.sh
```
 Select from options:
   * Add a new client
   * Revoke an existing client
   * Remove OpenVPN
   * Exit

For troubleshooting vist bottom of the following link : https://www.cyberciti.biz/faq/ubuntu-20-04-lts-set-up-openvpn-server-in-5-minutes/


## Router as switch

Tutorial link: https://www.youtube.com/watch?v=OGIJpqfHwkw&t=0s

### Main router config (RPI 4)
lan config in /etc/config/network
```ruby 
config device
        option name 'br-lan'
        option type 'bridge'
        list ports 'eth0'

config interface 'lan'
        option device 'br-lan'
        option proto 'static'
        option ipaddr '192.168.1.1'
        option netmask '255.255.255.0'
        option delegate '0'
        option multipath 'off'
```
wireless config in /etc/config/wireless

```ruby
config wifi-device 'radio0'
        option type 'mac80211'
        option path 'platform/soc/fe300000.mmcnr/mmc_host/mmc1/mmc1:0001/mmc1:0001:1'
        option cell_density '0'
        option htmode 'VHT40'
        option hwmode '11a'
        option channel '44'
        
config wifi-iface 'wifinet1'
        option device 'radio0'
        option mode 'ap'
        option ssid 'mesh'
        option key 'Dharun@123'
        option ieee80211r '1'
        option nasid '12345'
        option ft_over_ds '1'
        option ft_psk_generate_local '1'
        option network 'lan'
        option encryption 'psk-mixed'
        option mobility_domain 'ab12'
```

### Switch router config (MI4C)

lan config in /etc/config/network
```c
config device
        option name 'br-lan'
        option type 'bridge'
        list ports 'eth0.1'

config interface 'lan'
        option device 'br-lan'
        option proto 'static'
        option netmask '255.255.255.0'
        option ipaddr '192.168.1.5'
        option delegate '0'
        option gateway '192.168.1.1'
```
wireless config in /etc/config/wireless

```ruby
config wifi-device 'radio0'
        option type 'mac80211'
        option channel '11'
        option hwmode '11g'
        option path 'platform/10300000.wmac'
        option cell_density '0'
        option txpower '14'
        option htmode 'HT40'

config wifi-iface 'mesh'
        option device 'radio0'
        option key 'Dharun@123'
        option mode 'ap'
        option ssid 'mesh'
        option encryption 'psk-mixed'
        option ieee80211r '1'
        option nasid '12346'
        option mobility_domain 'ab12'
        option ft_over_ds '1'
        option ft_psk_generate_local '1'
        option network 'mesh lan'
```


## 802.11s Mesh

Youtube Tutorial: https://www.youtube.com/watch?v=cw8ykKgVKbM&t=159s

Setup the 2nd node router as a switch (https://www.youtube.com/watch?v=OGIJpqfHwkw&t=0s) and then use above tutorial for mesh

Openwrt forum links:
https://forum.openwrt.org/t/best-wireless-mesh-setup-with-openwrt/73570

https://forum.openwrt.org/t/mesh-performance-with-various-routers/104317

Linksys WRT3200ACM does not support mesh : https://github.com/kaloz/mwlwifi/issues?utf8=✓&q=is%3Aissue+802.11s


#### Libre Mesh:

Suggested hardware and basic requirements info: https://libremesh.org/docs/hardware/

Suitable openwrt devices : https://openwrt.org/toh/views/toh_extended_all?datasrt=availability&dataflt%5BWLAN%20driver_wlan-drivers%2A~%5D=ath9k&dataflt%5BWLAN%205.0GHz%2A~%5D=n&dataflt%5BWLAN%202.4GHz%2A~%5D=n&dataflt%5BSupported%20Current%20Rel%2A~%5D=.0





## Openwrt on TP Link Archer C7 v5 AC1750

For Archer C7 v1.1, v2, v2.1, v4, and V5 (fw1.0.11), installing OpenWrt is confirmed to work by simply uploading the OpenWrt firmware in the stock OEM's firmware-upgrade page. Please note, however, that this page will refuse to install firmware uploaded with a long filename. To bypass this limitation, download the relevant factory-flash BIN-file and then rename the file to firmware.bin before uploading.

Some forum links:
https://forum.openwrt.org/t/archer-c7-v5-new-one-installing-openwrt-process/79435

Device details page and installation guides:
https://openwrt.org/toh/tp-link/archer_c7

Tech Data:
https://openwrt.org/toh/hwdata/tp-link/tp-link_archer_c7_v5

Revert to stock Firmware:
https://forum.openwrt.org/t/help-required-to-revert-to-stock-tp-link-archer-c7-v4-eu/17641/7?u=dharun_561

Openwrt does not give good wifi speeds. Of my 450 Mbps I got only 180 Mbps on 5Ghz wifi and only 60 Mbps on 2.4 Ghz wifi. 

On searching the openwrt forum(https://forum.openwrt.org/t/archer-c7-v5-poor-wireless-performance/53854), found that enabling SFE (Qualcom fast path) would improve the performance. Another forum link : https://forum.openwrt.org/t/qualcomm-fast-path-for-lede/4582/765?page=36

Builds with SFE enabled can be found here : https://github.com/gwlim/openwrt-sfe-flowoffload

Image with SFE on for TP Link Archer C7 v5 AC1750 https://github.com/gwlim/openwrt-sfe-flowoffload-ath79/blob/master/MAY-2020/openwrt-sfe-flowoffload-normal/TP-Link%20Archer%20C7v5-mips74k-ath10k/openwrt-ath79-generic-tplink_archer-c7-v5-squashfs-factory.bin


## Openwrt on TP Link Archer A7 v5 
The Archer A7 is very similar to the Archer C7, but it has its own set of firmware. One difference is that the A7's switch shows only eth0, but the C7's switch shows eth0 and eth1. It has five 1 GBit/s Ethernet ports and has 2.4GHz and 5GHz Wifi integrated

Device page: https://openwrt.org/toh/tp-link/archer_a7_v5

## Openwrt on TP Link Archer C2600

On Version 1.1 of this device, the factory default username and password doesn't work. Hence the need to use TFTP to load OpenWrt.

Tech data:
https://openwrt.org/toh/tp-link/archer_c2600_v1

Forum links:
https://forum.openwrt.org/t/installing-openwrt-on-archer-c2600-v1-1/116160


## Connecting to a Wireless Network

We need Internet connection in the Router to install new packages. 


Before doing any actual configuration, the Wi-Fi interface must be enabled in order to be able to scan for networks in the vicinity:
```ruby
uci set wireless.@wifi-device[0].disabled=0
uci commit wireless
wifi
```
Now we can list networks in range substituting your actual wireless interface for wlan0:
```ruby
iw dev
iw dev wlan0 scan
```

Change the Network configuration file

```ruby
vi /etc/config/network
```

Add the next lines to the end:
```ruby
config interface 'wan'
        option proto 'dhcp'
```

Modify the Wireless configuration file
```ruby
vi /etc/config/wireless
```
Delete the full config wifi-iface 'default_radio0'


<img width="689" alt="Screenshot 2021-04-06 at 10 06 01 AM" src="https://user-images.githubusercontent.com/81893327/113659880-a15c4c80-96c0-11eb-9165-ecf70c5d760f.png">


Add the follwong with the wifi credentials to the file
```ruby
config wifi-iface 'wifinet0'
        option network 'wan'
        option ssid 'YOUR_SSID'
        option encryption 'psk' #enter your main wifi router's encryption  (psk, psk2, etc)
        option device 'radio0'
        option mode 'sta'
        option key 'YOUR_PASSWORD'
```

For example 


<img width="689" alt="Screenshot 2021-04-06 at 10 18 59 AM" src="https://user-images.githubusercontent.com/81893327/113662023-e2566000-96c4-11eb-8c39-641c3576201e.png">

Now restart the network using the following command to connect to the internet
```ruby
/etc/init.d/network restart 
```


## Luci Web Interface
To access and configure the router through a browser, install luci package.
```ruby
opkg update
opkg install luci
```



## USB Tethering

Guide to install USB tethering support for OpenWrt Routers

#### For Android devices
```ruby
opkg update
opkg install kmod-usb-net-rndis kmod-nls-base kmod-usb-core kmod-usb-net kmod-usb-net-cdc-ether kmod-usb2
```
#### Additional steps for iOS devices:
```ruby
opkg install kmod-usb-net-ipheth usbmuxd libimobiledevice usbutils
```



## 4G Dongle support

##### Suppport for Huawei 4G Dongles. 
Install the required packages and reboot the router for changes to take effect.

```ruby
opkg update
opkg install kmod-usb-net-cdc-ether usb-modeswitch comgt-ncm kmod-usb-net-huawei-cdc-ncm
opkg install kmod-usb-serial kmod-usb-serial-option kmod-usb-serial-wwan
reboot 
```


## Load balancing with multiple WAN interfaces

The mwan3 package provides the following functionality and capabilities:

* Outbound WAN traffic load balancing or fail-over with multiple WAN interfaces based on a numeric weight assignment
* Monitors each WAN connection using repeated ping tests and can automatically route outbound traffic to another WAN interface if the first WAN interface loses connectivity
 * Creating outbound traffic rules to customize which outbound connections should use which WAN interface (policy based routing). This can be customised based on source IP, destination IP, source port(s), destination port(s), type of IP protocol etc
* Physical and/or logical WAN interfaces are supported

### Why should I use mwan3?

* If you have multiple internet connections and you want to control what traffic goes through which specific WAN interface.
* Mwan3 can handle multiple levels of primary and backup interfaces, load-balanced or not. Different sources can have different primary or backup WANs.
* Mwan3 uses netfilter mark mask to be compatible with other packages (such as OpenVPN, PPTP VPN, QoS-script, Tunnels, etc) as you can configure traffic to use the default routing table.
* Mwan3 can also load-balance traffic originating from the router itself

### Prerequisites

* Ensure no other multiple WAN or policy routing packages are installed such as multiwan. Having multiwan installed at the same time as mwan3 is known not to work and is obsolete package. 
* Equally make sure you aren't using an other package that makes use of the same firewall mask value mwan3 uses as this will cause conflicts. 
* The firewall mask value used by mwan3 is able to be changed in the configuration to avoid this problem.


### Pre-configuration

* You will need a minimum of two WAN interfaces for mwan3 to work effectively. While mwan3 is primarily designed for physical WAN connections it can also be used with logical interfaces like OpenVPN or Wireguard.

#### On the command line (SSH)
```ruby
opkg update
opkg install mwan3 luci-app-mwan3
```
#### On the web interface (LuCI)

* Go to System → Software
* click “Update lists” to get the latest package databases
* In the “Download and install package:” box, enter “luci-app-mwan3” and click OK to download and install the luci-app-mwan3 package and all related packages, including mwan3 itself and all dependencies.



## Ad Block
 visit https://github.com/Dharun2308/AdBlock for more details
```ruby
opkg update
opkg install adblock luci-app-adblock libustream-mbedtls20201210 tcpdump-mini
```


## Speed Test Ookla and Netperf

### Speedtest by ookla

To install with pip: 
```ruby
pip install speedtest-cli
```

To install with wget:
```ruby
wget -O speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
chmod +x speedtest-cli
```

Speedtest package from official openwrt repo gives error. So modify the speedtest.py file with the help of following forum link.

https://github.com/sivel/speedtest-cli/pull/769/files

Modify line 1174. In nano editor press ctrl+w and search for "map(int, server_config['ignoreids'].split(','))" and replace with "map(int, (server_config['ignoreids'].split(',') if len(server_config['ignoreids']) else []) )"

```ruby
opkg update
opkg install python3-speedtest-cli python3-speedtest-cli-src
nano nano /usr/lib/python3.9/site-packages/speedtest.py
```
visit https://github.com/sivel/speedtest-cli for more updated speedtest package.


### Netperf

visit https://forum.openwrt.org/t/speedtest-new-package-to-measure-network-performance/24647/73

```ruby
opkg update
opkg install speedtest-netperf
```
Getting speed test results
```ruby
speedtest-netperf.sh -t 10 -n 10 -H netperf-eu.bufferbloat.net --sequential
```



## SQM
Smart Queue Management (SQM) is our name for an intelligent combination of better packet scheduling (flow queueing) techniques along with with active queue length management (AQM).

```ruby
opkg update
opkg install sqm-scripts luci-app-sqm
reboot
```
        
## NAS
https://openwrt.org/docs/guide-user/services/nas/start

```ruby
opkg update
opkg install block-mount kmod-fs-ext4 kmod-usb-storage kmod-usb-ohci kmod-usb-uhci e2fsprogs fdisk kmod-fs-antfs kmod-fs-exfat kmod-fs-hfs kmod-fs-ntfs
opkg install luci-app-samba4
reboot
```

To view current permissions of a folder
```ruby
ls -l /mnt/sha3
 ```       
 
Samba Server  configuration https://openwrt.org/docs/guide-user/services/nas/samba_configuration
To change and make the folder readable and writeable give chmod followed by path of the folder

```ruby
chmod 777 /mnt/nas/
service samba restart
 ```       

## OpenVPN Client

List of packages required for using OpenVPN client

Requires router to be set with login password. Doesnt work if the router has no login password 
```ruby
opkg update
opkg install openvpn-openssl luci-app-openvpn
```

## Remote Logging

Follow tutorial from :
http://www.aturnofthenut.com/2020/12/17/remote-logging-from-openwrt-to-rsyslog/

and 
https://openwrt.org/docs/guide-user/base-system/log.essentials


## Other

### MPTCP Enabled VPS:
Steps To How to configure VPS with MPTCP:

In order to install the Multipath TCP enabled Kernel do the following steps: 
```ruby
sudo apt update
sudo apt upgrade
wget https://raw.githubusercontent.com/onemarcfifty/mptcp-tools/main/makescript.sh
chmod 755 makescript.sh
./makescript.sh
# This creates the fetch_ycarus_kernel.sh
chmod 755 fetch_ycarus_kernel.sh
./fetch_ycarus_kernel.sh
# This now creates two debian packages in the /tmp directory
sudo apt install /tmp/linux-image*
sudo apt install /tmp/linux-headers*
sudo apt upgrade
sudo reboot
``

Now restart os & check by following cmd if MPTCP enabled or not.
```
curl http://multipath-tcp.org
```
You will get MPTCP enabled or disabled message.


### Docker shadowsocks server on Ubuntu

Edit docker-compose.yml file for changing configuration.
```c
sudo apt install docker-compose
curl -sSLO https://github.com/shadowsocks/shadowsocks-libev/raw/master/docker/alpine/docker-compose.yml
sudo docker-compose up -d
```

### Linux File Permissions

Details : https://phoenixnap.com/kb/linux-file-permissions

To check file permissions:
```ruby
ls –l filename
```
<img width="384" alt="Screen Shot 2022-02-13 at 1 21 11 PM" src="https://user-images.githubusercontent.com/81893327/153768973-4dda9b49-8add-4206-ab0e-6da100765341.png">


### To see live logs
        logread -f

### To view CPU Usage in Linux
        top

### view disk details 
        fdisk -l
        df -h

### Ping with specific time duration and interface
        ping -c 1 -I eth0.1 www.google.com

### wget from Google Drive

Steps:
1.	Select a file that is need to be downloaded and do right click.
2.	Click Share. A dialog box will appear.
3.	Click Advance in the right bottom corner.
4.	Click on the Change.. under who has access.
5.	Make it On- Public on the web.
6.	Click Save button.
7.	Copy the link for sharing…like…https://drive.google.com/file/d/1UibyVC_C2hoT_XEw15gPEwPW4yFyJFeOEA/view?usp=sharing
8.	Extrac FILEID part like….from above….1UibyVC_C2hoT_XEw15gPEwPW4yFyJFeOEA

For small file run following command on your terminal:
```ruby
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O FILENAME
```


### UCI commands
https://openwrt.org/docs/guide-user/base-system/uci



### ip table commands
https://serverfault.com/questions/904649/route-only-packets-from-specific-interface-over-vpn

        netstat -r

http://linux-ip.net/html/routing-tables.html

https://openwrt.org/docs/guide-user/network/routing

https://openwrt.org/docs/guide-user/network/ip_rules

https://openwrt.org/docs/guide-user/network/routes_configuration

Policy based routing
https://linux-club.de/wiki/opensuse/Policy_Based_Routing

ip route examples

https://serverfault.com/questions/953198/why-nexthop-has-invalid-gateway-when-it-seems-to-be-defined

https://serverfault.com/questions/904649/route-only-packets-from-specific-interface-over-vpn

### Scheduling tasks
https://openwrt.org/docs/guide-user/base-system/cron


### run executable .txt in terminal of linux
https://www.quora.com/How-do-I-run-executable-txt-in-terminal-of-linux


### OpenWrt Package manager

https://openwrt.org/docs/guide-user/additional-software/opkg

### Finding files

        find . -name "*file-name*"
        find / -name "*jpg"
        
https://www.howtoforge.com/tutorial/linux-search-files-from-the-terminal/
##
https://www.plesk.com/blog/various/find-files-in-linux-via-command-line/

### Using storage devices

https://openwrt.org/docs/guide-user/storage/usb-drives


### Expanding root filesystem
https://openwrt.org/docs/guide-user/additional-software/extroot_configuration

### Resetting the router

https://openwrt.org/docs/guide-user/troubleshooting/failsafe_and_factory_reset


### Shell Scripts
https://openwrt.org/docs/techref/initscripts


### Backing up a SD card or cloning it to computer
https://magpi.raspberrypi.org/articles/back-up-raspberry-pi
For Ubuntu
    
    sudo dd bs=4M if=/dev/sdb of=raspbian.img
Replace /dev/sdb by disk location (Find using df -h command).
 Replace raspbian.img by location and name of the file you want to save.
 
For Mac
        
    sudo dd bs=4m if=/dev/rdisk2 of=raspbian.img


 
