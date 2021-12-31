#!/bin/bash
on=1
off=0

while true
do

{

boost=`uci show system.custom.speedboost | cut -c27`
if [ "$boost" = "$on" ]
then
        echo "Speed boost ON. Not running isp.sh"
else
        echo "Running isp.sh"
        process=`ps | grep "[s]h /usr/isp.sh" | awk '{print $1}'`
	if [[ ! -z  "$process" ]]
        then
		echo "isp.sh running Already"
	else
		timeout 10s sh /usr/isp.sh 
	fi
fi

sleep 15
}
done