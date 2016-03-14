# -*- coding: utf-8 -*-
import MySQLdb as Db


class CreateDb(object):

    # 디비에 연결 상태
    DB_CONNECT_STATE = True
    # 디비 생성 결과
    CREATE_DB_STATE = True
    comment = None
    con = None
    cur = None

    def __init__(self, db_id, db_pw, new_db_nm):
        self.db_id = db_id
        self.db_pw = db_pw
        self.new_db_nm = new_db_nm

    # db connect
    def db_con(self):

        db_config = {
            'host': 'localhost',
            'user': self.db_id,
            'passwd': self.db_pw,
            'db': 'mysql',
        }

        try:
            self.con = Db.connect(**db_config)
            self.cur = self.con.cursor()

        except Db.DatabaseError:
            self.DB_CONNECT_STATE = False

        return [self.con, self.cur, self.DB_CONNECT_STATE]

    # create database
    def new_create_db(self):

        try:
            self.cur.execute('create database {0}'.format(self.new_db_nm))
            self.comment = '{0} 생성되었습니다.'.format(self.new_db_nm)

        except Db.ProgrammingError as e:
            self.CREATE_DB_STATE = False
            self.comment = e

        return [self.comment, self.CREATE_DB_STATE, self.new_db_nm]

    # drop database
    def drop_database(self):
        try:
            self.comment = self.cur.execute('drop database {0}'.format(self.new_db_nm))

        except Db.DatabaseError as e:
            self.comment = e

        return self.comment

    # close db
    def close_db(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':

    db_id = input('DB ID: ')
    db_pw = input('DB PASSWORD: ')
    new_db_nm = input('New db name: ')

    create = CreateDb(db_id, db_pw, new_db_nm)
    con_state = create.db_con()

    print('*'*50)

    if con_state:
        print('DB connect success')
    else:
        print('DB connect fail')

    print('*'*50)
    print('')

    if con_state[2]:
        result = create.new_create_db()
        print('*'*50)
        if result[1] == 0:
            comment = '{new_db_nm}를 생성 하지 못했습니다.'.format(new_db_nm=result[2])
            print('error code: {0}'.format(result[0].args[0]))
            print('error msg: {0}'.format(result[0].args[1]))
            print(comment)

        else:
            print('{0} DB 생성 완료! ')

        print('*'*50)

    create.close_db()