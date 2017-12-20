#!/bin/bash

echo  Limpia las tablas de iptables
iptables -F
iptables -X
iptables -Z
sudo iptables -t nat -F

sudo service apache2 stop

echo  ejecuta las tablas para TOR

sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 4000 -j REDIRECT --to-ports 4000

sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 22 -j REDIRECT --to-ports 22

sudo iptables -t nat -A PREROUTING -i wlan0 -p udp --dport 53 -j REDIRECT --to-ports 53

sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --syn -j REDIRECT --to-ports 9040


sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"


sudo service tor start
