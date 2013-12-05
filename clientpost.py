# -*- coding: utf-8 -*-
import sys, httplib, urllib

def printPostUsage():
	print '*'*20;
	print 'python *.py ip port suburl param';
	print '*'*20;

def post(argv):
	if not len(argv)==5:
		printPostUsage();
		exit(1);
	ip=argv[1];
	port=argv[2];
	suburl=argv[3];
	param=argv[4];
	hdr={
		'Connection':'keep-alive',
		'Content-Type':'text/plain',
		'Host':ip,
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.5) Gecko/20120606 Firefox/10.0.5',
	};
	d={};
	kvl=param.split('@');
	for kv in kvl:
		tmp=kv.split('=');
		if len(tmp)==2:
			d[tmp[0]]=tmp[1];
	post_param=urllib.urlencode(d);
	conn=httplib.HTTPConnection(ip, port);
	try:
		conn.request("POST",suburl,post_param,headers=hdr);
	except Exception, e:
		print e;
		conn.close();
		exit(1);
	res=conn.getresponse();
	data=res.read();
	if res.status==200:
		print data;
	else:
		print res.status;
	conn.close();

if __name__=="__main__":
	post(sys.argv);

