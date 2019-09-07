import requests
import base64

class SpotFire:
    def __init__(self, base_url, client_id, client_secret):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret

    # Using Base Encode64 logic get the below Authorization id(clientid:clientsecret)
    def encodebase64(self):
        self.encoded = base64.b64encode(bytes(str(self.client_id)+str(':')+(str(self.client_secret)),'utf-8'))
        self.encoded = self.encoded.decode('utf-8')
        return self.encoded

    def login(self):
        self.encodebase64()
        header_gs = {
            'accept': 'application/json',
            'Authorization': 'Basic '+str(self.encoded),
            'content-type': 'application/x-www-form-urlencoded'
        }
        data_get = {
            'grant_type': 'client_credentials',
            "scope": "api.rest.automation-services-job.execute"
            }
        try:
            r = requests.post(self.base_url + '/spotfire/oauth2/token', headers=header_gs, data=data_get)
            if r.status_code == 200:
                self.auth_token = r.json()
                self.auth_token = self.auth_token['access_token']
                return self.auth_token
        except Exception as e:
            return e
            exit(0)

    def start_library(self, *args):
        self.login()
        job_id = args[0]
        header_gs = {
            'authorization': 'Bearer ' + str(self.auth_token)
        }
        data_get = {
            'id': job_id
        }
        try:
            self.r = requests.post(self.base_url + '/spotfire/api/rest/as/job/start-library', headers=header_gs, data=data_get)
            self.return_job_id = self.r.json()['JobId']
            return self.return_job_id
        except Exception as e:
            return e
            exit(0)

    def get_status(self, *args):
        self.login()

        header_gs = {
            'authorization': 'Bearer ' + str(self.auth_token)
        }
        try:
            r = requests.get(self.base_url + f'/spotfire/api/rest/as/job/status/{args[0]}', headers=header_gs)
            return r.json()['StatusCode']
        except Exception as e:
            return e
            exit(0)




