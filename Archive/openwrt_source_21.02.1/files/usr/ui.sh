#!/bin/bash

while true
do

{
        /etc/init.d/main stop
        /etc/init.d/main start

        sleep 180
}
done
