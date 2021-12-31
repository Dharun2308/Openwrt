#!/bin/bash

on=1
off=0

while true
do

{


	# VPN Control Settings
	vpn_state=`uci show system.vpn.vpn | cut -c17`
	if [ "$vpn_state" = "$on" ]
	then

		status=`/etc/init.d/openvpn status`
    	if [ "$status" = "active with no instances" ]
    	then
			
        	vpn1_state=`uci show system.vpn.vpn1 | cut -c18`
			if [ "$vpn1_state" = "$on" ]
			then
				status=`uci show openvpn.vpn1.enabled | cut -c23`
				if [ "$status" = "$on" ]
				then	
					echo "VPN1 Already enabled"
				else
					echo "Enabling VPN1"
					uci set openvpn.vpn1.enabled='1'
					uci set openvpn.vpn2.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi

			else
				status=`uci show openvpn.vpn1.enabled | cut -c23`
				if [ "$status" = "$off" ]
				then	
					echo "VPN1 Already disabled"
				else
					echo "Disabling VPN1"
					uci set openvpn.vpn1.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi
			fi

			vpn2_state=`uci show system.vpn.vpn2 | cut -c18`
			if [ "$vpn2_state" = "$on" ]
			then
				status=`uci show openvpn.vpn2.enabled | cut -c23`
				if [ "$status" = "$on" ]
				then	
					echo "VPN2 Already enabled"
				else
					echo "Enabling VPN2"
					uci set openvpn.vpn2.enabled='1'
					uci set openvpn.vpn1.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi

			else
				status=`uci show openvpn.vpn2.enabled | cut -c23`
				if [ "$status" = "$off" ]
				then	
					echo "VPN2 Already disabled"
				else
					echo "Disabling VPN2"
					uci set openvpn.vpn2.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi
			fi


		elif [ "$status" = "inactive" ]
		then
			
			vpn1_state=`uci show system.vpn.vpn1 | cut -c18`
			if [ "$vpn1_state" = "$on" ]
			then
				status=`uci show openvpn.vpn1.enabled | cut -c23`
				if [ "$status" = "$on" ]
				then	
					echo "VPN1 Already enabled"
				else
					echo "Enabling VPN1"
					uci set openvpn.vpn1.enabled='1'
					uci set openvpn.vpn2.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi

			else
				status=`uci show openvpn.vpn1.enabled | cut -c23`
				if [ "$status" = "$off" ]
				then	
					echo "VPN1 Already disabled"
				else
					echo "Disabling VPN1"
					uci set openvpn.vpn1.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi
			fi

			vpn2_state=`uci show system.vpn.vpn2 | cut -c18`
			if [ "$vpn2_state" = "$on" ]
			then
				status=`uci show openvpn.vpn2.enabled | cut -c23`
				if [ "$status" = "$on" ]
				then	
					echo "VPN2 Already enabled"
				else
					echo "Enabling VPN2"
					uci set openvpn.vpn2.enabled='1'
					uci set openvpn.vpn1.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi

			else
				status=`uci show openvpn.vpn2.enabled | cut -c23`
				if [ "$status" = "$off" ]
				then	
					echo "VPN2 Already disabled"
				else
					echo "Disabling VPN2"
					uci set openvpn.vpn2.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi
			fi

		elif [ "$status" = "running" ]
		then
			
			vpn1_state=`uci show system.vpn.vpn1 | cut -c18`
			if [ "$vpn1_state" = "$on" ]
			then
				status=`uci show openvpn.vpn1.enabled | cut -c23`
				if [ "$status" = "$on" ]
				then	
					echo "VPN1 Already enabled"
				else
					echo "Enabling VPN1"
					uci set openvpn.vpn1.enabled='1'
					uci set openvpn.vpn2.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi

			else
				status=`uci show openvpn.vpn1.enabled | cut -c23`
				if [ "$status" = "$off" ]
				then	
					echo "VPN1 Already disabled"
				else
					echo "Disabling VPN1"
					uci set openvpn.vpn1.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi
			fi

			vpn2_state=`uci show system.vpn.vpn2 | cut -c18`
			if [ "$vpn2_state" = "$on" ]
			then
				status=`uci show openvpn.vpn2.enabled | cut -c23`
				if [ "$status" = "$on" ]
				then	
					echo "VPN2 Already enabled"
				else
					echo "Enabling VPN2"
					uci set openvpn.vpn2.enabled='1'
					uci set openvpn.vpn1.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi

			else
				status=`uci show openvpn.vpn2.enabled | cut -c23`
				if [ "$status" = "$off" ]
				then	
					echo "VPN2 Already disabled"
				else
					echo "Disabling VPN2"
					uci set openvpn.vpn2.enabled='0'
					uci commit
					/etc/init.d/openvpn restart
				fi
			fi

		else

			ipadd1=`(ifconfig  2>/dev/null tun0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}')`
			if [[ ! -z  "$ipadd1" ]]
			then
				echo "VPN Already ON"
			else
				/etc/init.d/openvpn restart
			fi	
			
		fi

	else
		status=`/etc/init.d/openvpn status`
		if [ "$status" = "running" ]
		then
			{
			echo "Turning VPN Off"
			/etc/init.d/openvpn stop
			}
		elif  [ "$status" = "active with no instances" ]
		then 
			{
			echo "Turning VPN Off"
			/etc/init.d/openvpn stop
			}
		else
			echo "VPN Already off"
		fi
	fi 



sleep 2
}
done