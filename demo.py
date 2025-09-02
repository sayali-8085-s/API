# import json
# pdata ={'name':'say'}
# jdata1 =json.dumps(pdata)
# print(jdata1)
# print(type(jdata1))

# import json
# pdata ={'name':'say'}
# with open('n1.json','a') as f :
#  jdata1 =json.dump(pdata ,f)
# print(jdata1)
# print(type(jdata1))

import json
pdata ={'name':True ,'age':False ,'active':None}
with open('n1.json','a') as f :
 jdata1 =json.dump(pdata ,f)
print(jdata1)
print(type(jdata1))

j_data ='{"name": true, "age": false, "active": null}'
p_data = json.loads(j_data)
print(p_data)
print(type(p_data))