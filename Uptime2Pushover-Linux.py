import subprocess, httplib, urllib

uptime = subprocess.Popen(["uptime"], stdout=subprocess.PIPE)
output = uptime.communicate()[0]
clean_output = output[14:-44]

hostname = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
hostout = hostname.communicate()[0]
cleanhost = hostout[0:-1]

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "APP_TOKEN", #Pushover App Token goes here!
    "user": "USER_KEY", #Pusover User Key goes here!
    "message": cleanhost + " has been online for " + clean_output + " Hours!",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

print cleanhost + " has been online for " + clean_output + " Hours!"
