#!/usr/bin/python
# -*- coding: utf-8 -*-

INPUT_SPLITER='&';
KV_CONNECTOR='=';
NECESS_KEY=['method'];

SUCCEED=0;
METHOD_ERR=1;
METHOD_ERR_MSG="only post method are allowed.";
PARAM_ERR=2;
PARAM_ERR_MSG="param error.";

CREATE_TABLE_FAILED=10000;
CREATE_TABLE_FAILED_MSG="create table failed.";
PLAYER_ALREADY_IN_TABLE=10001;
PLAYER_ALREADY_IN_TABLE_MSG="player already sit.";
DELETE_TABLE_FAILED=10002;
DELETE_TABLE_FAILED_MSG="delete table failed.";
DELETE_TABLE_OK_MSG="delete table ok.";
TABLE_NOT_FOUND=10003;
TABLE_NOT_FOUND_MSG="table not foud.";
ADD_PLAYER_TABLE_N0T_FOUND=10004;
ADD_PLAYER_TABLE_N0T_FOUND_MSG="add player failed, table not found, create table first.";
ADD_PLAYER_TABLE_FULL=10005;
ADD_PLAYER_TABLE_FULL_MSG="add player failed, table full.";
ADD_PLAYER_DB_ERROR=10006;
ADD_PLAYER_DB_ERROR_MSG="add player database operation failed.";