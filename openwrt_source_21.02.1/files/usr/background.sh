#!/bin/bash

on=1
off=0


##############  FUNCTION DEFINITIONS  ##############


loadb_cont()
{
	# Load balancing control

	load_b=`uci show system.custom.loadbalancing | cut -c30`

	if [ "$load_b" = "$on" ]
	then
	status=`/etc/init.d/mwan3 status`
	
		if [ "$status" = "inactive" ]
		then 
		{
			echo "Turning Load Balancing on"

			process=`ps | grep "[s]h /usr/isp.sh" | awk '{print $1}'`
			kill $process

			uci set shadowsocks-libev.@ss_tunnel[0].disabled='1' 
			uci set shadowsocks-libev.ss_rules.disabled='1' 
			uci set shadowsocks-libev.ssr0.disabled='1' 
			uci set shadowsocks-libev.sss0.disabled='1' 
			uci commit
			/etc/init.d/shadowsocks-libev disable
			/etc/init.d/shadowsocks-libev stop
			/etc/init.d/mwan3 enable
			/etc/init.d/mwan3 restart

		}

		elif [ "$status" = "running" ]
		then	
			lb_set=`uci show system.custom.static_load | cut -c28`
			if [ "$lb_set" = "$on" ]
			then
				process=`ps | grep "[s]h /usr/static_mwan_change.sh" | awk '{print $1}'`
				if [[ ! -z  "$process" ]]
        		then
					echo "Static LB running Already"
				else
					process=`ps | grep "[s]h /usr/dynamic_mwan_change.sh" | awk '{print $1}'`
					kill $process
					sh /usr/static_mwan_change.sh &
					sleep 1
				fi
			
			else
				process=`ps | grep "[s]h /usr/dynamic_mwan_change.sh" | awk '{print $1}'`
				if [[ ! -z  "$process" ]]
        		then
					echo "Dynamic LB running Already"
				else
					process=`ps | grep "[s]h /usr/static_mwan_change.sh" | awk '{print $1}'`
					kill $process
					sh /usr/dynamic_mwan_change.sh &
					sleep 1
				fi

			fi
		else
			echo "Load balancing Already ON"
		fi

	else
		status=`/etc/init.d/mwan3 status`
		if [ "$status" = "running" ]
		then 
		{
			echo "Turning Load Balancing Off"
			/etc/init.d/mwan3 stop
			/etc/init.d/mwan3 disable
			process=`ps | grep "[s]h /usr/static_mwan_change.sh" | awk '{print $1}'`
			kill $process
			process=`ps | grep "[s]h /usr/dynamic_mwan_change.sh" | awk '{print $1}'`
			kill $process
			/etc/init.d/shadowsocks-libev stop
			
		}
		else
			echo "Loadbalancing Already off"
		fi	
	fi
}

speedb_cont()
{
	# Speed Boost control

	boost=`uci show system.custom.speedboost | cut -c27`
	if [ "$boost" = "$on" ]
	then
			status=`/etc/init.d/shadowsocks-libev status`
			if [ "$status" = "inactive" ]
			then 
			{
				process=`ps | grep "[s]h /usr/isp.sh" | awk '{print $1}'`
				kill $process
				process=`ps | grep "[s]h /usr/static_mwan_change.sh" | awk '{print $1}'`
				kill $process
				process=`ps | grep "[s]h /usr/dynamic_mwan_change.sh" | awk '{print $1}'`
				kill $process
				echo "Turning Speedboost on"
				/etc/init.d/mwan3 stop
				/etc/init.d/mwan3 disable
				/etc/init.d/shadowsocks-libev enable
				process=`ps | grep "[s]h /usr/mptcp_change.sh" | awk '{print $1}'`
				if [[ ! -z  "$process" ]]
        		then
					echo "MPTCP.sh running Already"
				else
					sh /usr/mptcp_change.sh &
				fi
				
			}
			elif [ "$status" = "active with no instances" ]
			then
				process=`ps | grep "[s]h /usr/isp.sh" | awk '{print $1}'`
				kill $process
				process=`ps | grep "[s]h /usr/static_mwan_change.sh" | awk '{print $1}'`
				kill $process
				process=`ps | grep "[s]h /usr/dynamic_mwan_change.sh" | awk '{print $1}'`
				kill $process
				echo "Turning Speedboost on"
				/etc/init.d/mwan3 stop
				/etc/init.d/mwan3 disable
				/etc/init.d/shadowsocks-libev enable

				process=`ps | grep "[s]h /usr/mptcp_change.sh" | awk '{print $1}'`
				if [[ ! -z  "$process" ]]
        		then
					echo "MPTCP.sh running Already"
				else
					sh /usr/mptcp_change.sh &
				fi

			else
			echo "Speed boost Already ON"
			fi
	else
		status=`/etc/init.d/shadowsocks-libev status`
        if [ "$status" = "running" ]
        then 
        {
        echo "Turning Speedboost Off"
		process=`ps | grep "[s]h /usr/mptcp_change.sh" | awk '{print $1}'`
		kill $process

		/etc/init.d/shadowsocks-libev disable
        uci set shadowsocks-libev.@ss_tunnel[0].disabled='1'
        uci set shadowsocks-libev.ss_rules.disabled='1'
        uci set shadowsocks-libev.ssr0.disabled='1'
        uci set shadowsocks-libev.sss0.disabled='1'
		uci commit
        /etc/init.d/shadowsocks-libev stop
        
		}

		elif [ "$status" = "active with no instances" ]
		then
		{
		echo "Turning Speedboost Off"
		process=`ps | grep "[s]h /usr/mptcp_change.sh" | awk '{print $1}'`
		kill $process
		/etc/init.d/shadowsocks-libev disable
        uci set shadowsocks-libev.@ss_tunnel[0].disabled='1'
        uci set shadowsocks-libev.ss_rules.disabled='1'
        uci set shadowsocks-libev.ssr0.disabled='1'
        uci set shadowsocks-libev.sss0.disabled='1'
		uci commit
        /etc/init.d/shadowsocks-libev stop
		}

		else
		echo "Speedboost Already off"
		fi	
	fi
}

nas_cont()
{
		echo " Change detected in NAS"
		pcm=`uci show system.nas.nas | cut -c17`
		if [ "$pcm" = "$on" ]
		then
		echo " Turning NAS on"
		/etc/init.d/vsftpd start
		uci set system.nas.nas_change='0'
		uci commit
		else
		echo " Turning NAS off"
		/etc/init.d/vsftpd stop
		uci set system.nas.nas_change='0'
		uci commit
		fi
}


##############  MAIN FUNCTION  ##############

# Continuously check

sleep 3

while true
do
{

echo "############################"

loadb_cont

speedb_cont

vpn_cont

nas_cont

echo "############################"



sleep 4

clear
}

done


 
