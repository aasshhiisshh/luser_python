'''
This is open source for all. YOu can store your Data on DropBox without any hasitation. Thankss

'''

#Including the dropbox sdk and other required modules
import dropbox
import os
import webbrowser


#Providing the app key and app secret.

app_key = "YOUR KEY HERE"
app_secret = "YOUR SECRET HERE"

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
webbrowser.open(authorize_url)

# Have the user sign in and authorize this token
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'

code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
# print 'linked account: ', client.account_info()

file_list = os.listdir(".")
count = 0
for file in file_list:
    fileName, fileExtension = os.path.splitext(file)
    if fileExtension!='.py':
        count+=1
        f = open(file, 'rb')
        response = client.put_file('/Uploaded-Files/'+ fileName + fileExtension, f)
        print "Uploaded File "+ str(count)
