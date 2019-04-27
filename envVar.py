import os

jamf_user = os.environ.get('JAMF_USER')
jamf_pass = os.environ.get('JAMF_PASS')
jamf_url = "https://tryitout.jamfcloud.com/JSSResource/computers/subset/basic"
# jamf_url = os.environ.get('JAMF_URL')

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_host = os.environ.get('DB_HOST')
db_database = os.environ.get('DB_DB')
