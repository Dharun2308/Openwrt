# Openwrt 

## Table of contents
* [General info](#general-info)
* [Build using imagebuilder](#Build-using-imagebuilder)
* [Build Custom packages](#Build-Custom-packages)
* [Build packages using SDK](#Build-packages-using-SDK)
* [Connecting to a Wireless Network](#Connecting-to-a-Wireless-Network)
* [Luci Web Interface](#Luci-Web-Interface)
* [USB Tethering](#usb-tethering)
* [4G Dongle support](#4G-Dongle-support)
* [Load balancing with multiple WAN interfaces](#Load-balancing-with-multiple-WAN-interfaces)
* [Ad Block](#Ad-Block)
* [Speed Test](#Speed-Test)
* [SQM](#SQM)
* [NAS](#NAS)
* [OpenVPN Client](#OpenVPN-Client)
* [Other](#other)





## General info


Pre requisites: Knowledge on OpenWrt, vi editor, Basic linux commands.

To write a Readme file on Github:

https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project

https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

Some major tutorials:

https://kenfavors.com/code/how-to-protect-ssh-with-fail2ban/


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

* Go to System ??? Software
* click ???Update lists??? to get the latest package databases
* In the ???Download and install package:??? box, enter ???luci-app-mwan3??? and click OK to download and install the luci-app-mwan3 package and all related packages, including mwan3 itself and all dependencies.



## Ad Block
 visit https://github.com/Dharun2308/AdBlock for more details
```ruby
opkg update
opkg install adblock luci-app-adblock libustream-mbedtls20201210 tcpdump-mini
```


## Speed Test 

visit https://forum.openwrt.org/t/speedtest-new-package-to-measure-network-performance/24647/73

```ruby
opkg update
opkg install speedtest-netperf
```
Getting speed test results
```ruby
speedtest-netperf.sh -t 10 -n 10 -H netperf-eu.bufferbloat.net --sequential
```
## Speedtest by ookla
visit https://github.com/sivel/speedtest-cli
```ruby
opkg update
opkg install python3-speedtest-cli
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



## Other


### To see live logs
        logread -f

### To view CPU Usage in Linux
        top

### view disk details 
        fdisk -l
        df -h

### Ping with specific time duration and interface
        ping -c 1 -I eth0.1 www.google.com



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


## run executable .txt in terminal of linux
https://www.quora.com/How-do-I-run-executable-txt-in-terminal-of-linux


## OpenWrt Package manager

https://openwrt.org/docs/guide-user/additional-software/opkg

## Finding files

        find . -name "*file-name*"
        find / -name "*jpg"
        
https://www.howtoforge.com/tutorial/linux-search-files-from-the-terminal/
##
https://www.plesk.com/blog/various/find-files-in-linux-via-command-line/

## Using storage devices

https://openwrt.org/docs/guide-user/storage/usb-drives


## Expanding root filesystem
https://openwrt.org/docs/guide-user/additional-software/extroot_configuration

## Resetting the router

https://openwrt.org/docs/guide-user/troubleshooting/failsafe_and_factory_reset


## Shell Scripts
https://openwrt.org/docs/techref/initscripts


## Backing up a SD card or cloning it to computer
https://magpi.raspberrypi.org/articles/back-up-raspberry-pi
For Ubuntu
    
    sudo dd bs=4M if=/dev/sdb of=raspbian.img
Replace /dev/sdb by disk location (Find using df -h command).
 Replace raspbian.img by location and name of the file you want to save.
 
For Mac
        
    sudo dd bs=4m if=/dev/rdisk2 of=raspbian.img

# New topic
 
