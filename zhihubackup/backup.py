import requests
import json
import os
from tqdm import tqdm

def act_api(username):
    return "https://www.zhihu.com/api/v4/members/%s/activities" % username

def get_json(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"}
    r = requests.get(url, headers=headers)
    return json.loads(r.text)

def makedirs(username, target_type):
    try:
        os.makedirs(os.path.join(username, target_type))
    except OSError:
        pass

def loop(username):
    api = read_record()
    if api is None:
        api = act_api(username)
    t = tqdm()
    while True:
        save_record(api)
        jdata = get_json(api)
        # data: ['target', 'action_text', 'is_sticky', 'actor', 'verb', 'created_time', 'type', 'id']
        for dd in jdata['data']:
            target = dd['target']
            if 'author' not in target or target["author"]["url_token"] != username:
                # skip others' content
                continue
            target_type = target['type']
            makedirs(username, target_type)
            saved = []
            if 'question' in target and 'title' in target['question']:
                saved.append(target['question']['title'])
            for saved_type in ('title', 'content', 'updated_time'):
                if saved_type in target:
                    saved.append(str(target[saved_type]))
            with open(os.path.join(username, target_type, "%s.txt" % target['id']), 'w') as f:
                f.write('\n'.join(saved))
            t.update(1)
        # paging: is_end next previous
        paging = jdata['paging']
        if paging['is_end']:
            break
        api = paging['next']

def save_record(current_api, record_file='record'):
    with open(record_file, 'w') as f:
        f.write(current_api)

def read_record(record_file='record'):
    if os.path.isfile(record_file):
        with open(record_file) as f:
            return f.read().strip()
    else:
        return None
