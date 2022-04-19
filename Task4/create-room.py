import requests
access_token = 'ZDc5MmJkOWEtNGU4Mi00Y2FiLWIzZmMtYmIyMDkwOTBhNTZlMzdmODllZTgtM2Nm_PE93_d18234f8-808f-47c0-86d0-8c22f2a047f0'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}

params={'title': 'EN2_Devasc_SNE_SB'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
