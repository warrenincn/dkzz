#!/usr/bin/python
# -*- coding: utf-8 -*-

import web,json,uuid
from cfg import *

db = web.database(
	dbn='mysql', 
	user='root', 
	pw='12345', 
	db='dkzz');

class pubicModule:
	@staticmethod
	def checkInput(param):
		d={};
		kvl=param.split(INPUT_SPLITER);
		for e in kvl:
			kv=e.split(KV_CONNECTOR);
			if not len(kv)==2:
				print kv;
				return PARAM_ERR,"param error, the format should be k=v.";
			else:
				d[kv[0]]=kv[1];
		print d;
		for e in NECESS_KEY:
			if not d.has_key(e):
				return PARAM_ERR,"param error, missing NECESS_KEY";
		return SUCCEED,d;

	@staticmethod
	def insertSql(tblname, kvpair):
		key='';
		val='';
		for k, v in kvpair.items():
			key+=k+',';
			val+='\''+str(v)+'\''+',';
		if not key=='':
			key=key[:-1];
		if not val=='':
			val=val[:-1];
		sql="INSERT INTO %s(%s) VALUES(%s)" % (tblname,key,val);
		# print sql;
		rst=db.query(sql_query=sql,_test=False);
		return rst;

	@staticmethod
	def selectSql(tblname, cols, conditions):
		c='';
		for col in cols:
			c+=col+',';
		if not c=='':
			c=c[:-1];
		sql="SELECT %s from %s where %s" % (c,tblname,conditions);
		# print sql;
		rst=db.query(sql_query=sql,_test=False);
		return rst;

	@staticmethod
	def deleteSql(tblname, conditions):
		sql="DELETE FROM %s where %s" % (tblname,conditions);
		rst=db.query(sql_query=sql,_test=False);
		return rst;

	@staticmethod
	def updateSql(tblname, cols, conditions):
		sql="UPDATE %s SET %s where %s" % (tblname,cols, conditions);
		rst=db.query(sql_query=sql,_test=False);
		return rst;

class table:
	param=None;
	methodMapping={};
	def __init__(self):
		self.methodMapping={
		#method=0@total_player=7(default value is 5)@player_id=XXX
			"0":self.createTable,
		#method=1@owner_id=XXXXX
			"1":self.deleteTable,
		#method=2@game_id=XXXX
			"2":self.checkTable,
		#method=3@player_id=XXXX@game_id=XXXX
			"3":self.addPlayer,
			};

	def GET(self):
		return json.dumps({'status': METHOD_ERR, 'data': METHOD_ERR_MSG});

	def POST(self):
		param=web.data();
		mCode=None;
		ret=None;
		rst=None;
		if not param:
			return json.dumps({'status': PARAM_ERR, 'data': PARAM_ERR_MSG});
		ret,self.param=pubicModule.checkInput(param);
		if not ret==SUCCEED:
			return json.dumps({'status': ret, 'data': self.param});
		mCode=self.param["method"];
		ret, rst=self.methodMapping[mCode]();
		return json.dumps({'status': ret, 'data': rst});

	def createTable(self):
		tableid=str(uuid.uuid1());
		if self.param.has_key("total_player"):
			totalplayer=self.param["total_player"];
			if int(totalplayer)<5:
				return PARAM_ERR, PARAM_ERR_MSG;
		else:
			totalplayer='5';
		playerid=self.param["player_id"];
		if not playerid:
			return PARAM_ERR, PARAM_ERR_MSG;
		kv={
			"game_id":tableid,
			"player_num":1,
			"game_status":-1,
			"total_player":totalplayer,
			"owner_id":playerid,
		};
		cols=["game_id","player_id"];
		conditions="player_id='"+playerid+'\'';
		rst=pubicModule.selectSql("game_player", cols, conditions);
		if len(rst)>0:
			resp={};
			for e in rst:
				for k,v in e.items():
					resp[k]=v;
			return PLAYER_ALREADY_IN_TABLE,resp;
		rst=pubicModule.insertSql("game_detail",kv);
		if rst==1:
			kv2={
				"player_id":playerid,
				"game_id":tableid,
			};
			rst=pubicModule.insertSql("game_player",kv2);
			if rst==1:
				resp={
					"game_id":tableid,
					"player_num":1,
					"game_status":-1,
					"owner_id":playerid,
					"total_player":totalplayer,
				};
				return SUCCEED, resp;
			else:
				return CREATE_TABLE_FAILED, CREATE_TABLE_FAILED_MSG;
		else:
			return CREATE_TABLE_FAILED, CREATE_TABLE_FAILED_MSG;

	def deleteTable(self):
		ownerid=self.param["owner_id"];
		if not ownerid:
			return PARAM_ERR, PARAM_ERR_MSG;
		cols=["game_id"];
		conditions="owner_id='"+ownerid+'\'';
		rst=pubicModule.selectSql("game_detail", cols, conditions);
		if len(rst)==1:
			gameid=rst[0]["game_id"];
			conditions="game_id='"+gameid+'\'';
			rst=pubicModule.deleteSql("game_detail", conditions);
			print rst;
			rst=pubicModule.deleteSql("game_player", conditions);
			print rst;
			return SUCCEED, DELETE_TABLE_OK_MSG;
		else:
			return DELETE_TABLE_FAILED, DELETE_TABLE_FAILED_MSG;

	def checkTable(self):
		gameid=self.param["game_id"];
		if not gameid:
			return PARAM_ERR, PARAM_ERR_MSG;
		cols=["game_id","player_num","game_status","total_player","owner_id"];
		conditions="game_id='"+gameid+'\'';
		rst=pubicModule.selectSql("game_detail", cols, conditions);
		if len(rst)==1:
			resp={};
			for k, v in rst[0].items():
				resp[k]=v;
			return SUCCEED, resp;
		else:
			return TABLE_NOT_FOUND, TABLE_NOT_FOUND_MSG;

	def addPlayer(self):
		playerid=self.param["player_id"];
		if not playerid:
			return PARAM_ERR, PARAM_ERR_MSG;
		gameid=self.param["game_id"];
		if not gameid:
			return PARAM_ERR, PARAM_ERR_MSG;
		cols=["player_num","total_player","game_id","game_status","owner_id"];
		conditions="game_id='"+gameid+'\'';
		rst=pubicModule.selectSql("game_detail", cols, conditions);
		if len(rst)==1:
			e=rst[0];
			playernum=e["player_num"];
			totalplayer=e["total_player"];
			gameid=e["game_id"];
			gamestatus=e["game_status"];
			ownerid=e["owner_id"];
			if playernum>=totalplayer:
				return ADD_PLAYER_TABLE_FULL, ADD_PLAYER_TABLE_FULL_MSG;
			kv={
				"player_id":playerid,
				"game_id":gameid,
			};
			rst=pubicModule.insertSql("game_player",kv);
			if rst==1:
				resp={
					"game_id":gameid,
					"total_player":totalplayer,
					"game_status":gamestatus,
					"owner_id":ownerid,
				};
				playernum+=1;
				resp["player_num"]=playernum;
				cols=["player_id"];
				conditions="game_id='"+gameid+'\'';
				rst=pubicModule.selectSql("game_player", cols, conditions);
				player=[];	
				if len(rst)>0:
					for e in rst:
						d={
							"player_id":e["player_id"],
						};
						player.append(d);
				if not len(player)==0:
					resp["player"]=player;
				cols="player_num='%s'" % (playernum);
				conditions="game_id='"+gameid+'\'';
				rst=pubicModule.updateSql("game_detail", cols, conditions);
				if rst==1:
					return SUCCEED, resp;
				else:
					return ADD_PLAYER_DB_ERROR, ADD_PLAYER_DB_ERROR_MSG;
			else:
				return ADD_PLAYER_DB_ERROR, ADD_PLAYER_DB_ERROR_MSG;
		else:
			return ADD_PLAYER_TABLE_N0T_FOUND, ADD_PLAYER_TABLE_N0T_FOUND_MSG;


urls=(
	'/table','table'
	);

if __name__=="__main__":
	app=web.application(urls, globals(),autoreload=True);
	app.run();