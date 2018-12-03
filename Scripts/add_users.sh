#!/bin/bash
host="localhost"
port=8888
input="users_me.csv"
while IFS= read -r var
do
 name="$(echo "$var" | cut -d "," -f 1)"
 pass="$(echo "$var" | cut -d "," -f 2)"
 echo "$name"
 echo "{\"data\": {\"password\": \"$pass\"}}"
 echo "{\"data\": {\"password\": \"$pass\"}}" | http PUT http://$host:$port/v1/accounts/$name --verbose
done < "$input"
