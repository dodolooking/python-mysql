import pymysql
import datetime

datastr="BG,00002,202007032300,T0,27.6,0.0,0.0,U,62.1,0.0,0.0,P,1007.6,0.0,0.0,WS,0.1,0.0,0.0,WD,45.0,0.0,0.0,PM2.5,19.5,0.0,0.0,NO2,0.0558,0.0000,0.0000,SO2,0.0000,0.0000,0.0000,NH3,168.7,0.0,0.0,6682,ED"
array=datastr.split(",")

stationnum=array[1]
datatimestr=datetime.datetime.strptime(array[2], '%Y%m%d%H%M').strftime('%Y-%m-%d %H:%M:00')
t0=array[4]
t1=array[5]
t2=array[6]

u0=array[8]
u1=array[9]
u2=array[10]

p0=array[12]
p1=array[13]
p2=array[14]


ws0=array[16]
ws1=array[17]
ws2=array[18]

wd0=array[20]
wd1=array[21]
wd2=array[22]

pm25_0=array[24]
pm25_1=array[25]
pm25_2=array[26]

no2_0=array[28]
no2_1=array[29]
no2_2=array[30]

so2_0=array[32]
so2_1=array[33]
so2_2=array[34]

nh3_0=array[36]
nh3_1=array[37]
nh3_2=array[38]

conn=pymysql.connect(host="localhost",user="test",passwd="123456",db="test")

cursor=conn.cursor()

tablename="ychbdata_2020"
cursor.execute("select count(*) from information_schema.TABLES where table_name ='"+tablename+"'")

conn.commit()

data=cursor.fetchone()

print(data[0])
#create table

if data[0]==0:
    cursor.execute(
        "	CREATE TABLE `" + tablename + "` (  `stationnum` varchar(100) NOT NULL,  `datatime` datetime NOT NULL,  `t0` float(9,1) DEFAULT NULL,  `t1` float(9,1) DEFAULT NULL,  `t2` float(9,1) DEFAULT NULL,  `u0` float(9,1) DEFAULT NULL,  `u1` float(9,1) DEFAULT NULL,  `u2` float(9,1) DEFAULT NULL,  `p0` float(9,1) DEFAULT NULL,  `p1` float(9,1) DEFAULT NULL,  `p2` float(9,1) DEFAULT NULL,  `ws0` float(9,1) DEFAULT NULL,  `ws1` float(9,1) DEFAULT NULL,  `ws2` float(9,1) DEFAULT NULL,  `wd0` float(9,1) DEFAULT NULL,  `wd1` float(9,1) DEFAULT NULL,  `wd2` float(9,1) DEFAULT NULL,  `pm25_0` float(9,1) DEFAULT NULL,  `pm25_1` float(9,1) DEFAULT NULL,  `pm25_2` float(9,1) DEFAULT NULL,  `no2_0` float(9,4) DEFAULT NULL,  `no2_1` float(9,4) DEFAULT NULL,  `no2_2` float(9,4) DEFAULT NULL,  `so2_0` float(9,4) DEFAULT NULL,  `so2_1` float(9,4) DEFAULT NULL,  `so2_2` float(9,4) DEFAULT NULL,  `nh3_0` float(9,1) DEFAULT NULL,  `nh3_1` float(9,1) DEFAULT NULL,  `nh3_2` float(9,1) DEFAULT NULL,  PRIMARY KEY (`stationnum`,`datatime`))")
    conn.commit()
#############

#insert data


sql="INSERT INTO "+tablename+" VALUES(\'"+stationnum+"\',\'"+datatimestr+"\',"+t0+","+t1+","+t2+","+u0+","+u1+","+u2+","+p0+","+p1+","+p2+","+ws0+","+ws1+","+ws2+","+wd0+","+wd1+","+wd2+","+pm25_0+","+pm25_1+","+pm25_2+","+no2_0+","+no2_1+","+no2_2+","+so2_0+","+so2_1+","+so2_2+","+nh3_0+","+nh3_1+","+nh3_2+")"

cursor.execute(sql)
conn.commit()
#data=cursor.fetchall()

conn.close()
