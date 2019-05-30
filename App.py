from ICCApi import ICCApi
iccApiInstance = ICCApi()
all_matches=[]
api_response = iccApiInstance.get_fixtures(iccApiInstance.get_params("2019-05-30","2019-06-04")).json()
total_pages=api_response["pageInfo"]["numPages"]
print("Total number of pages " +str(total_pages))
for page in range(total_pages):
   all_matches=all_matches+list(filter(lambda x : x["tournamentId"]["id"] == 8191,
   iccApiInstance.get_fixtures(iccApiInstance.get_params("2019-05-30","2019-06-04",page)).json()["content"]))
for match in all_matches:
    print("_______________")
    print(match["scheduleEntry"]["matchDate"])
    print(match["scheduleEntry"]["team1"]["team"]["fullName"])
    print(match["scheduleEntry"]["team2"]["team"]["fullName"])
