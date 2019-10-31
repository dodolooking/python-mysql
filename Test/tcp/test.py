import datetime
str="hello,2019-10-20,13:00:00"

print(str.encode('utf-8'))
print(b'hello,2019-10-20,13:00:00')

b2 = bytes(str,encoding='utf8')
print(b2)



a = '201810030055'
b = datetime.datetime.strptime(a, '%Y%m%d%H%M').strftime('%Y-%m-%d %H:%M:00')


print(b)