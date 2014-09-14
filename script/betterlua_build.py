import urllib.request
import json
import os

os.chdir("..")

# Fetch source syntax
syntax_response = urllib.request.urlopen("https://raw.githubusercontent.com/Xuerian/Sublime-BetterLua/master/BetterLua.YAML-tmLanguage")
assert syntax_response.getcode() == 200, "Could not fetch base syntax file"

# Fetch Apiiiiii
api_response = urllib.request.urlopen("http://firefall.nyaasync.net/Apiii/assests/production/api-production.json")
assert api_response.getcode() == 200, "Could not fetch API json file"

# Load JSON and remove info
data = json.loads(api_response.readall().decode("utf-8"))
del data["info"]

# Extract modules and methods to form regex string
regex = "|".join("({}\\.({}))".format(module, "|".join(str(method) for method in sorted(data[module]))) for module in sorted(data))

replacements = [
	["Lua (Better)", "Lua (Better Firefall)"],
	["scopeName: source.lua", "scopeName: source.vendor.lua.firefall"],
	["fileTypes: [lua]\n", ""],
	["uuid: ", "# uuid: "],
	["#VENDOR ", ""],
	["#VENDOR", ""],
	["#NAME_VENDOR", "firefall"],
	["#REGEX_VENDOR", regex]
]

# Construct new file
with open("BetterLua-Firefall.YAML-tmLanguage", "w") as output:
	text = syntax_response.readall().decode("utf-8")
	for x in replacements:
		text = text.replace(x[0], x[1])
	output.write(text)

print("Done, make sure to build the YAML-tmLanguage file")