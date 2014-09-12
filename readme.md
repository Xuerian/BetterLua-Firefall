BetterLua-Firefall
====

A python file to fetch the [BetterLua](https://github.com/Xuerian/Sublime-BetterLua) syntax file, the exposed Firefall API as JSON ([Thanks to Arkii](http://firefall.nyaasync.net/Apiii/live.php)), and merge them into one new syntax file.

Installation
----
* Install BetterLua (Provides theme and extra standard language files)
* Clone or download and extract this folder into your Data/Packages directory

Usage
----
Either select __Lua (Better-Firefall)__ per-file, or set up [ApplySyntax](https://github.com/facelessuser/ApplySyntax)

ApplySyntax
----
Follow [ApplySyntax](https://github.com/facelessuser/ApplySyntax) installation and usage.

This snippet should work for your user settings:

    "syntaxes": [
        {
            "name": ["Firefall/BetterLua-Firefall", "BetterLua/BetterLua"],
            "rules": [
                {"file_name": ".*/Firefall/.*\\.lua$"},
            ]
        },
    ]

New syntax highlighting
----
A version of the modified syntax file is included with each push to this repository, but a supporting theme is not.

API functions are scoped support.function.vendor.lua.firefall - BetterLua introduces more scopes that your theme can also support, see its readme. A dark theme with partial support for these scopes is included in BetterLua.

Building
----
For instructions on building the modified syntax file, see BetterLua's readme.