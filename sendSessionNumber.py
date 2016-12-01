import commands
import time

while(1):
  (status, output) = commands.getstatusoutput('netstat -tunp | grep -w "front" | grep "41205" | wc -l')
  print status, output

  (status, output) = commands.getstatusoutput('zabbix_sender -z "192.168.103.112" -s "Linux_redhat5.8_51" -k "front.session.number" -o '+output)
  print status, output

  time.sleep(1)



