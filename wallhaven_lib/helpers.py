import json


def load_config_file(config, filepath):
    tmp_conf = dict()
    with open(filepath) as fp:
        tmp_conf = json.loads(fp.read())
    for k, v in tmp_conf.items():
        config.__setattr__(k, v)
