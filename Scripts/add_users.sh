#!/bin/bash

input="users_me.csv"
while IFS= read -r var
do
  name="$(echo "$var" | cut -d "," -f 1)"
  echo "$name"
  echo "{\"data\": {\"password\": \"$name\"}}"
  #echo "{\"data\": {\"password\": \"$name\"}}" | http PUT http://ec2-18-232-250-82.compute-1.amazonaws.com:8888/v1/accounts/$name --verbose
  echo "{\"data\": {\"password\": \"$name\"}}" | http PUT http://localhost:8888/v1/accounts/$name --verbose
done < "$input"

