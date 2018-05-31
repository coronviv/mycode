#!/usr/bin/env python3
#
import http.client
conn=http.client.HTTPConnection("localhost",9021)
#
conn.request('HEAD','/')
res=conn.getresponse()
print(res.status, res.reason)