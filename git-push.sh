#!/bin/bash

read -r gitToken < /home/socrates/scripts/.secret.git.txt

echo $gitToken

$(git add * )
$( git commit * -m "first" )

gitUrl="github.com/shauryaCodesAndHosts/all_code.git"

gitUserName="shauryaCodesAndHosts"

final_url="https://$gitUserName:$gitToken@$gitUrl"

echo $final_url

# $(git push -u origin master)

echo $(git remote set-url origin $final_url)

$(git push origin master)

