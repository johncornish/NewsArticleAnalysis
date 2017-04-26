#! /usr/bin/zsh
i=0
for u in $(python3 smmry.py);
  do echo "$i: $u";
  i=$i + 1
done
