# Openwrt 

## Table of contents
* [General info](#general-info)
* [Connecting to a Wireless Network](#Connecting-to-a-Wireless-Network)
* [Luci Web Interface](#Luci-Web-Interface)
* [USB Tethering](#usb-tethering)
* [4G Dongle support](#4G-Dongle-support)
* [Load balancing with multiple WAN interfaces](#Load-balancing-with-multiple-WAN-interfaces)
* [OpenVPN Client](#OpenVPN-Client)
* [Setup](#setup)


Load balancing/failover with multiple WAN interfaces


## General info
This project is simple Lorem ipsum dolor generator.

pre requisites: Knowledge on openwrt, vi editor , basic linux commands.


https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project

https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax



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
reboot -f
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

## OpenVPN Client

List of packages required for using OpenVPN client

Requires router to be set with login password. Doesnt work if the router has no login password 
```ruby
opkg update
opkg install openvpn-openssl luci-app-openvpn
```




To see live logs
logread -f


