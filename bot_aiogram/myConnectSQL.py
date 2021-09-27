import pymysql.cursors

def getConnection():
    connection = pymysql.connect(
        host = '172.13.12.27',
        user = 'jred',
        password = 'A912n157tno',
        db = 'asterisk',
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection