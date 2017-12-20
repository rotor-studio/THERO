#!/bin/bash

echo  Limpia las tablas de iptables
sudo iptables -F
sudo iptables -X
sudo iptables -Z
sudo iptables -t nat -F

echo  ejecuta las tablas para Activar la navegacion normal

sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 4000 -j REDIRECT --to-ports 4000

sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT

sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"


