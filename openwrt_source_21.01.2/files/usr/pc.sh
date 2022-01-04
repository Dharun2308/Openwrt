#!/bin/bash

while true
do

{
       pc=`uci show system.pc.parental_change | cut -c28`
	if [ "$pc" = "$on" ]
	then
		echo " Change detected in Adblock"
		pcm=`uci show system.pc.parental | cut -c21`
		if [ "$pcm" = "$on" ]
		then
		echo " Turning Adblock on"
		/etc/init.d/adblock start
		uci set system.pc.parental_change='0'
		uci commit
		else
		echo " Turning Adblock off"
		/etc/init.d/adblock suspend
		uci set system.pc.parental_change='0'
		uci commit
		sleep 1
		fi
	else
		echo " No change in Adblock"
	fi	

        sleep 30
}
done
