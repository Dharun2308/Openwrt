#!/bin/bash

while true
do

{

for i in  eth1 eth2 eth3 eth4 eth5 eth6 wlan0 
do
{
ip1=`(ifconfig  2>/dev/null $i | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ip1" ]]
then
        echo "$i IP present"
        uci set system.wan_ip."$i"="$ip1"
        uci commit
        
else
        echo "$i NO IP present"
        uci set system.wan_ip."$i"='Not connected'
        uci commit
fi

}
done


sleep 2
}
done