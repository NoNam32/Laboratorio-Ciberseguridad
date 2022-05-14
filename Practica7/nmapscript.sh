host=$(hostname -I > nmap.txt)

ip=$(ip addr >> nmap.txt)

infor=$(wget -q -O - ipinfo.io/ip >> nmap.txt)

nmap -sL 189.218.43.* >> nmap.txt

base64 nmap.txt > nmap.b64
