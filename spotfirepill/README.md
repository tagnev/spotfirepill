
This is a simple example package. You can use

Using Spotfire class. Create the object to instantiate the spotfire class.
And then login using "Client Id" & "Client Secret" to execute the jobs & check the status.

If you face any issue, kindly droup out the issue to tagnev.vengat@gmail.com

Example
-------

pip install spotfirepill

import spotfirepill as spt
spot_fire_instance = spt.SpotFire(base_url,client_id,client_secret)
spot_fire_instance.login()


# Execute the Job
spot_fire_instance.start_library('{job_id}')
it returns job execution id

#Get the Status

spot_fire_instance.get_status('{job execution id}')
