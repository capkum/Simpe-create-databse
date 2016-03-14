# -*- coding: utf8 -*-
"""
mysql exception 참고 url(https://www.python.org/dev/peps/pep-0249/#cursor-attributes)

"""
import MySQLdb as Db

db_id = input('DB ID: ')
db_pw = input('DB PASSWORD: ')
new_db_nm = input('New db name: ')
result_state = True
error_msg = ''
con = ''
cur = ''

# db config
db_config = {
        'host': 'localhost',
        'user': db_id,
        'passwd': db_pw,
        'db': 'mysql',
        }

# db connect
try:
    con = Db.connect(**db_config)
    cur = con.cursor()

except Db.DatabaseError as e:
    result_state = False
    error_msg = '디비에 연결할수 없습니다.'
    print(error_msg)

# create database
if result_state:

    try:
        result = cur.execute('create database %s' % new_db_nm)
        if result:
            print('%s create success!' % new_db_nm)
        else:
            print('%s fail!! try agin!' % new_db_nm)

    except Db.ProgrammingError as e:
        comment = '{new_db_nm}를 생성 하지 못했습니다.'.format(new_db_nm=new_db_nm)
        print('error code: {0}'.format(e.args[0]))
        print('error msg: {0}'.format(e.args[1]))
        print(comment)

    finally:
        cur.close()
        con.close()
