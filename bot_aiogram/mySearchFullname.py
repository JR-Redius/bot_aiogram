import myConnectSQL
from pymysql import cursors

def getSearchFullname(full_name):
    sql = "SELECT name, fullname, secret, ipaddr, useragent FROM sippeers WHERE fullname like '%"+str(full_name)+"%';"
    connection = myConnectSQL.getConnection()
    cursor = connection.cursor()
    cursor.executor(sql)