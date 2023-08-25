# SHEBANG is a "message", that starts with #! to the OS, usually to
# tell what to use to run this script

import os
import sys

arguments = {"lang": None,
             "count": 1,
             }

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-")
    value = value.strip()
    if key not in arguments:
        print(f"Invalid argument '{key}'")
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG", "en_US")[:5]

msg = {"en_US": "Hello World!",
       "pt_BR": "Olá mundo!",
       "it_IT": "Ciao mondo!",
       "es_SP": "Hola mundo!",
       "fr_FR": "Bonjour monde!"}

print(msg[current_language] * int(arguments["count"]))
