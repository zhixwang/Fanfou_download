# -*- coding: utf-8 -*-

import fanfou
import config as config


# login in on fanfou
consumer = {'key': config.key, 'secret': config.secret}
client = fanfou.XAuth(consumer, config.client_name, config.client_pwd)
fanfou.bound(client)

user = {'id':config.target_id,'page':'0'}


page_max = config.page_max

file_name = user['id']+'.txt'
try:
    out_file = open(file_name,'a')
except:
    print "Output file open failed!"

for i in range(0,page_max):
	page = i+1
	print('Page:'+str(page)+'\n')
	user['page'] = str(page)
	tweets = client.statuses.user_timeline(user).json()
	length = len(tweets)

	for j in range(0,length):
		foo = tweets[j]['text']	#type: unicode
		if foo.find('@') >= 0:		#if reply/mention: skip
			continue
		print(foo)
		print('\n')
		try:
			out_file.write(foo.encode('gb2312'))
		except UnicodeEncodeError:
			out_file.write(foo.encode('gb2312','ignore'))
		except:
			out_file.write(foo.encode('gb18030','ignore'))
		out_file.write('\n')

out_file.close()




