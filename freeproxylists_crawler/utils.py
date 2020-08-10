import subprocess
import json


def get_proxies():
    p = subprocess.Popen(
        ['python', '-m' 'freeproxylists_crawler.tools.show_proxies'],
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
