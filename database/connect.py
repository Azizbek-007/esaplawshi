from sqlite3 import Error
import sqlite3
from time import ctime
from ast import literal_eval
import requests
def post_sql_query(sql_query):
    with sqlite3.connect('my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE "USERS" (
	"user_id"	INTEGER NOT NULL,
	"username"	TEXT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"reg_date"	TEXT,
	"status"	INTEGER,
	PRIMARY KEY("user_id")
);'''

    post_sql_query(users_query)

create_tables()

def create_groups():
    sql = '''CREATE TABLE "groups" (
	"id"	INTEGER,
	"group_id"	TEXT,
	"add"	INTEGER,
	"lan"	TEXT,
	"status"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);''' 
    post_sql_query(sql)

create_groups()

def create_members():
  sql = '''CREATE TABLE "members" (
	"id"	INTEGER,
	"user_id"	INTEGER,
	"new_user_id"	TEXT,
	"group_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);'''
  post_sql_query(sql)

create_members()

def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date, status) VALUES ' \
                             f'({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}", 1);'
        post_sql_query(insert_to_db_query)

def reg_group(chat_id):
    sql = f"SELECT * FROM `groups` WHERE group_id = '{chat_id}'"
    res = post_sql_query(sql)
    if len(res) == 0:
        sql = f"INSERT INTO `groups`('group_id', 'add', 'status', 'lan') VALUES ('{chat_id}', '0', '1', 'off')"
        post_sql_query(sql)

def group_setting(chat_id, son):
  sql = f"UPDATE groups SET  `add` = '{son}' WHERE group_id = '{chat_id}'"
  post_sql_query(sql)

def group_get_setting(chat_id):
    sql = f"SELECT * FROM `groups` WHERE group_id = '{chat_id}'"
    return post_sql_query(sql)

def new_member(user_id, new_user_id, chat_id):
    sql = f"SELECT `new_user_id` FROM `members` WHERE user_id = '{user_id}' AND group_id = '{chat_id}'"
    res = post_sql_query(sql)
    newuser = [] if res == [] else res[0][0]
    if newuser != []: newuser = literal_eval(newuser)
    if new_user_id not in newuser:
        newuser.append(new_user_id)
        if not res:
            sql = f'INSERT INTO `members`(user_id, new_user_id, group_id) VALUES ("{user_id}","{newuser}","{chat_id}")'
            post_sql_query(sql)
        else:
            sql = f'UPDATE members SET  `new_user_id` = "{newuser}" WHERE user_id = {user_id} AND group_id = {chat_id}'
            post_sql_query(sql)

        
def usercount(user_id, chat_id):
    sql = f"SELECT new_user_id FROM members WHERE user_id = '{user_id}' AND group_id = '{chat_id}'"
    try:
        return len(literal_eval(post_sql_query(sql)[0][0]))
    except: return 0
    
def tops(user_id, chat_id):
    sql = f'SELECT json_array_length(new_user_id), user_id FROM members WHERE group_id = {chat_id} ORDER BY json_array_length(new_user_id) DESC  LIMIT 50'
    data = post_sql_query(sql)
    return data

def members_clear(chat_id):
    sql = f"DELETE FROM `members` WHERE `group_id`='{chat_id}'"
    post_sql_query(sql)

def member_clear(user_id):
    sql = f"DELETE FROM `members` WHERE `user_id`={user_id}"
    post_sql_query(sql)

def chan_off_on(chat_id, lan):
    sql = f"UPDATE groups SET  lan = '{lan}' WHERE group_id = '{chat_id}'"
    post_sql_query(sql)

def cnumber(chat_id, user_id):
    ucount = int(usercount(user_id, chat_id))
    print(ucount)
    chat = group_get_setting(chat_id)[0][2]
    return int(chat) - int(ucount)

def botPr(chat_id, API_TOKEN):
    x = requests.get(f'https://api.telegram.org/bot{API_TOKEN}/getChat?chat_id={chat_id}')
    y = x.json()['result']['permissions']
    return y

def users_id():
    sql = "SELECT user_id, status FROM USERS WHERE status=1"
    return post_sql_query(sql)

def user_count():
    sql = "SELECT count(*), status FROM USERS WHERE status=1"
    return post_sql_query(sql)

def group_count():
    sql = "SELECT count(*), status FROM groups WHERE status=1"
    return post_sql_query(sql)

def user_status_up(user_id):
    sql = f"UPDATE USERS SET status=0 WHERE user_id={user_id}"
    post_sql_query(sql)

def groups_id():
    sql = "SELECT group_id, status FROM groups WHERE status=1"
    return post_sql_query(sql)

def group_status_up(group_id):
    sql = f"UPDATE groups SET status=0 WHERE group_id={group_id}"
    post_sql_query(sql)
