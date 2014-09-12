import urllib.request
import json
import os

# sourcefile = os.path.join("..", "BetterLua", "BetterLua.YAML-tmLanguage")

# assert os.path.exists(sourcefile), "Could not locate BetterLua.YAML-tmLanguage"

# Fetch source syntax
syntax_response = urllib.request.urlopen("https://raw.githubusercontent.com/Xuerian/Sublime-BetterLua/master/BetterLua.YAML-tmLanguage")
assert syntax_response.getcode() == 200, "Could not fetch base syntax file"

# Fetch Apiiiiii
api_response = urllib.request.urlopen("http://firefall.nyaasync.net/Apiii/assests/production/api-production.json")
assert api_response.getcode() == 200, "Could not fetch API json file"

data = json.loads(api_response.readall().decode("utf-8"))
del data["info"]

# Extract modules and methods to form regex string
regex = "|".join("({}\\.({}))".format(module, "|".join(str(method) for method in sorted(data[module]))) for module in sorted(data))

with open("BetterLua-Firefall.YAML-tmLanguage", "w") as output:
	for line in syntax_response:
		output.write(line.decode("utf-8").replace("#VENDOR ", "").replace("#VENDOR", "").replace("#REGEX_VENDOR", regex).replace("#NAME_VENDOR", "firefall").replace("Lua (Better)", "Lua (Better-Firefall)"))

print("Done, make sure to build the YAML-tmLanguage file")