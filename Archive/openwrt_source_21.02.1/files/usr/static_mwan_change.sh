#!/bin/bash

pre="none"

while true
do

{

# ETH1
ipadd1=`(ifconfig  2>/dev/null eth1 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd1" ]]
then
	cur1="yes"
else
	cur1="no"
fi





# ETH2
ipadd2=`(ifconfig  2>/dev/null eth2 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd2" ]]
then
        cur2="yes"    
else
        cur2="no"
fi



# ETH3
ipadd2=`(ifconfig  2>/dev/null eth3 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd2" ]]
then
        cur3="yes"
else
        cur3="no"
fi




# ETH4
ipadd2=`(ifconfig  2>/dev/null eth4 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd2" ]]
then
        cur4="yes"
else
        cur4="no"
fi




# USB0
ipadd2=`(ifconfig  2>/dev/null usb0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd2" ]]
then
        cur5="yes"
else
        cur5="no"
fi




# USB1
ipadd2=`(ifconfig  2>/dev/null usb1 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd2" ]]
then
        cur6="yes"
else
        cur6="no"
fi




# WLAN0
ipadd2=`(ifconfig  2>/dev/null wlan0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`

if [[ ! -z  "$ipadd2" ]]
then
        cur7="yes"
else
        cur7="no"
fi




cur="$cur1"+"$cur2"
cur="$cur"+"$cur3"
cur="$cur"+"$cur4"
cur="$cur"+"$cur5"
cur="$cur"+"$cur6"
cur="$cur"+"$cur7"



if [ "$cur" == "$pre" ] 
then 
    echo "No Change" 
    
else 

    /etc/init.d/mwan3 restart
   
fi 


pre=$cur

sleep 5
}
done


