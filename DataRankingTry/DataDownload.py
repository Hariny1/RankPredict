import requests 
data_url = "https://data.gov.in/sites/default/files/Report-144-27042015123446105PM-2012-2013.csv"
r = requests.get(data_url) # create HTTP response object   
with open("StudTeacher.csv",'wb') as f: 
    f.write(r.content) 




Krishna Prasad KPM0000002
Mayank Singh MS0000001
Udit Bhatia UB0000001
