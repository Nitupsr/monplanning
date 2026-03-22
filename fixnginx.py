content = open('/etc/nginx/sites-available/default').read()
# Supprimer le bloc dans la section commentée
old = "#       location /planning.html {\n                auth_basic \"MonPlanning\";\n                auth_basic_user_file /etc/nginx/.htpasswd;\n        }\n"
new = ""
content = content.replace(old, new)
open('/etc/nginx/sites-available/default', 'w').write(content)
print('OK')
