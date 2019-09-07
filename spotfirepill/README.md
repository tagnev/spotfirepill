
This is a simple example package. You can use

Using Spotfire class. Create the object to instantiate the spotfire class.
And then login using "Client Id" & "Client Secret" to execute the jobs & check the status.

If you face any issue, kindly droup out the issue to tagnev.vengat@gmail.com


pip install spotfire-job-api

import spotfire-job-api as spt
spot_fire_instance = spt.SpotFire(base_url,client_id,client_secret)
spot_fire_login = spot_fire_instance.login()
