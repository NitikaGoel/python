import requests

class ICCApi:
    baseUrl="https://cricketapi-icc.pulselive.com/fixtures"

    def get_params(self,start_date,end_date,page=0):
       return {"startDate":start_date,
        "endDate":end_date,
        "page":page}
    
    def get_fixtures(self,query_params):
        return requests.get(self.baseUrl,query_params)







