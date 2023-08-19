# SHEBANG is a "message", that starts with #! to the OS, usually to
# tell what to use to run this script

import os

current_language = os.getenv("LANG")[:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá mundo!"
elif current_language == "it_IT":
    msg = "Ciao mondo!"
elif current_language == "es_SP":
    msg = "Hola mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour monde!"

print(msg)
