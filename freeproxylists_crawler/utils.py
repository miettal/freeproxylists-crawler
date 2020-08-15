import subprocess
import json


def get_proxies(source):
    if source is None:
        option = []
    else:
        option = ['--source', source]

    p = subprocess.Popen(
        ['python', '-m' 'freeproxylists_crawler.tools.show_proxies'] + option,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    (stdout, stderr) = p.communicate()

    items = []
    for item_str in stdout.decode('utf-8').strip().split('\n'):
        item = json.loads(item_str)
        items.append(item)

    return items
