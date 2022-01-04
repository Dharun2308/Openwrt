#!/bin/bash

while true
do

{


# FOR All wan Sources

for i in  eth1 eth2 eth3 eth4 eth5 eth6 wlan0 
do
{
ip1=`(ifconfig  2>/dev/null $i | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ip1" ]]
then
        # Internet checking

        for j in  amazon.in www.google.co.in in.yahoo.com apple.com 139.130.4.5 google.com paypal.com drive.google.com youtube.com
        do
        {
        if [[ ! -z  "$int" ]]
        then
                echo "Internet Found on $i"
                uci set system.wan_internet."$i"="1"
                uci commit
                break
        else   
                int=`ping -w 1 -c 1 -I $i $j | grep "from"`
        fi
        }
        done
        
else
        echo "$i NO IP present"
        uci set system.wan_internet."$i"='0' 
        uci commit
fi

}
done


# FOR Main system internet

inte=`ping -w 1 -c 1 google.com | grep "from"`
if [[ ! -z  "$inte" ]]
then
        echo "Internet Found on Main system"
        uci set system.custom.internet=1
        uci commit

else
        echo "Internet Not Found on main system"
        uci set system.custom.internet=0
        uci commit
fi


sleep 2
}
done