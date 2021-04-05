# Openwrt 

## Table of contents
* [General info](#general-info)
* [Connecting to a Wireless Network](#Connecting-to-a-Wireless-Network)
* [USB Tethering](#usb-tethering)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.


https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax



## Connecting to a Wireless Network

We need Internet connection in our Router to install new packages. 


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
Delete the full config wifi-iface 'default_radio0'.
Add the follwong with the wifi credentials to the file.
```ruby
config wifi-iface 'wifinet0'
        option network 'wan'
        option ssid 'YOUR_SSID'
        option encryption 'psk' #enter your main wifi router's encryption  
        option device 'radio0'
        option mode 'sta'
        option key 'karthikeyan'
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

Suppport for Huawei 4G Dongles 
```ruby
opkg update
opkg install kmod-usb-net-cdc-ether usb-modeswitch comgt-ncm kmod-usb-net-huawei-cdc-ncm
opkg install kmod-usb-serial kmod-usb-serial-option kmod-usb-serial-wwan
reboot -f
```



## OpenVPN Client

List of packages required for using OpenVPN client

Requires router to be set with login password. Doesnt work if the router has no login password 
```ruby
opkg update
opkg install openvpn-openssl luci-app-openvpn
```




To see live logs
logread -f


