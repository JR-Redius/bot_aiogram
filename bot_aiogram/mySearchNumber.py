import myConnectSQL
from pymysql import cursors


def getSearchNumber(phone_number):
    list_number =[]
    sql = 'SELECT name FROM sippeers;'
    connection = myConnectSQL.getConnection()
    cursor = connection.cursor()
    cursor.execute(sql)
    for id in cursor:
        list_number.append(id['name'])
    
    if list_number.count(str(phone_number)):
        cursor.execute('SELECT name, fullname, secret, ipaddr, useragent FROM sippeers WHERE name="'+str(phone_number)+'";')
        return cursor.fetchone()
    else:
        return ('Номер не найден')
