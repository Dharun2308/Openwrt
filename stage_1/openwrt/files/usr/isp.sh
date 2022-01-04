#!/bin/bash

#/etc/init.d/firewall restart

clear

for i in  eth1 eth2 eth3 eth4 eth5 eth6 wlan0 
do
{
ip1=`(ifconfig  2>/dev/null $i | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ip1" ]]
then

                for k in  1 2 3
                do
                {
                if [[ ! -z  "$name1" ]]
                then
                        break
                else
                        echo "Trying attempt $k for ISP name"
                        name1=`timeout 10s whois $(curl --interface $i -s ipinfo.io/org | cut -d" " -f1) | awk -F: 'BEGIN{IGNORECASE=1}/(as-?name|org-?name):/{sub("^  *","",$2);print$2}' | sed -n 2p | awk '{print $1,$2}'`
                fi
                }
                done

                # check if isp name found

                if [[ ! -z  "$name1" ]]
                then
                        echo " "
                        uci set system.wan_name."$i"="$name1"
                        uci commit
                else
                        uci set system.wan_name."$i"='Unknown'
                        uci commit
                fi

                uci commit
                name1=""

        
else
        echo "$i NO IP present"
        echo " "
        uci set system.wan_name."$i"='---'
        uci commit
fi

}
done


