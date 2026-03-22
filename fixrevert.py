content = open('/var/www/html/planning.html').read()
start = content.find('function updateNextServiceBanner() {')
if start == -1:
    print('NOT FOUND')
else:
    depth = 0
    i = start
    while i < len(content):
        if content[i] == '{': depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                content = content[:start] + content[i+1:]
                break
        i += 1
    open('/var/www/html/planning.html', 'w').write(content)
    print('OK')
