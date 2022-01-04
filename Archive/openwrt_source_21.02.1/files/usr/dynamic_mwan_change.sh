#!/bin/bash

while true
do

{

clear 

ip1=`(ifconfig  2>/dev/null eth1 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "eth1 IP present"
                ping=` timeout 3s ping  -c 2 -I eth1 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wan_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wan_m1_w1.weight=10
                uci commit
                fi
                echo "$val1"
        else
                echo "eth1 NO IP present"
        fi







ip1=`(ifconfig  2>/dev/null eth2 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "eth2 IP present"
                ping=` timeout 3s ping  -c 2 -I eth2 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wan2_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wan2_m1_w1.weight=10
                uci commit
                fi
                
                echo "$val1"
        else
                echo "eth2 NO IP present"
        fi






ip1=`(ifconfig  2>/dev/null eth3 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "eth3 IP present"
                ping=` timeout 3s ping  -c 2 -I eth3 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wan3_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wan3_m1_w1.weight=10
                uci commit
                fi
                
                echo "$val1"
        else
                echo "eth3 NO IP present"
        fi







ip1=`(ifconfig  2>/dev/null eth4 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "eth4 IP present"
                ping=` timeout 3s ping  -c 2 -I eth4 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wan4_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wan4_m1_w1.weight=10
                uci commit
                fi
                
                echo "$val1"
        else
                echo "eth4 NO IP present"
        fi








ip1=`(ifconfig  2>/dev/null eth5 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "eth5 IP present"
                ping=` timeout 3s ping  -c 2 -I eth5 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wan5_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wan5_m1_w1.weight=10
                uci commit
                fi
                
                echo "$val1"
        else
                echo "eth5 NO IP present"
        fi




ip1=`(ifconfig  2>/dev/null eth6 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "eth6 IP present"
                ping=` timeout 3s ping  -c 2 -I eth6 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wan6_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wan6_m1_w1.weight=10
                uci commit
                fi
                
                echo "$val1"
        else
                echo "eth6 NO IP present"
        fi





ip1=`(ifconfig  2>/dev/null wlan0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

        if [[ ! -z  "$ip1" ]]
        then
                echo "wlan0 IP present"
                ping=` timeout 3s ping  -c 2 -I wlan0 google.com | grep round-trip | awk '{ print $4}' | sed 's|^[^/]*\(/[^/]*/\).*$|\1|' | sed 's/^\///;s/\// /g'`
                b="1000"
                round=${ping%.*}
                val1=`echo $(( b / round ))`
                if [[ ! -z  "$val1" ]]
                then
                uci set mwan3.wwan_m1_w1.weight="$val1"
                uci commit
                else
                uci set mwan3.wwan_m1_w1.weight=10
                uci commit
                fi
                echo "$val1"
        else
                echo "wlan NO IP present"
        fi


sleep 30
}
done


