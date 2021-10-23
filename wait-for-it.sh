#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

>&2 echo "Testing $host availability to execute $cmd"

while !</dev/tcp/"$host"; do
  sleep 1
done

>&2 echo "$host is up - executing command: $cmd "
exec $cmd
