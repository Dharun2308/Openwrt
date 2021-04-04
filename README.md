# Openwrt


https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project



## USB Tethering

Guide to install USB tethering support for OpenWrt Routers

#### For Android devices
```
opkg update
opkg install kmod-usb-net-rndis kmod-nls-base kmod-usb-core kmod-usb-net kmod-usb-net-cdc-ether kmod-usb2
```
#### Additional steps for iOS devices:

```
opkg install kmod-usb-net-ipheth usbmuxd libimobiledevice usbutils
```

