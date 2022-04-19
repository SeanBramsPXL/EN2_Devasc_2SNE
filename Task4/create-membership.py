import requests
access_token = 'ZDc5MmJkOWEtNGU4Mi00Y2FiLWIzZmMtYmIyMDkwOTBhNTZlMzdmODllZTgtM2Nm_PE93_d18234f8-808f-47c0-86d0-8c22f2a047f0'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNjVjODdhYjAtYmZjNi0xMWVjLWI0NGQtYzc0NmU5NWE2MzUx'
person_email = 'wim.leppens@pxl.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
