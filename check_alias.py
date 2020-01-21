import subprocess
import json

# In this function will get the email of the candidate and return a JSON output if true and False if false

#email = 'bamohame@microsoft.com'
#alias = "az ad user show --id " + email + " --query '{name:displayName, alias:mailNickname}' --output json"
##print(alias)
#bash_alias = subprocess.getstatusoutput(alias)
#alias_json_convert = json.loads(bash_alias[1])
#
#print(alias_json_convert)
#print(type(alias_json_convert))
def check_alias(email):
    alias = "az ad user show --id " + email + " --query '{name:displayName, alias:mailNickname}' --output json"
    bash_alias = subprocess.getstatusoutput(alias)
    if bash_alias[0] == 0 :
      alias_json_convert = json.loads(bash_alias[1])
      return alias_json_convert
    else :
      return False

print(check_alias('bamohame@microsoft.com'))
