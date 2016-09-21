# bookDeploy
auto deploy gitbook to apache web server
##dependencies
1. apache
2. git
3. npm
3. gitbook

##install
1. clone your gitbook on your server at a place,such as `/root/mybook`
2. clone this repo at /root/bookDeploy/
3. change bookDeploy.py , `gitPath = "/root/mybook"`
4. `sh /root/bookDeploy/start.sh`
5. view url `http://yourhost/book`
