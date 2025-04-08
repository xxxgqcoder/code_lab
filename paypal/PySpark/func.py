def parse_quota(line):
    lines = line.strip().split('\n')
    assert len(lines) >= 2, f"hadoop cmd ret invalid: {line}"
    head = lines[0].split()
    ret = {}
    for i, e in enumerate(lines[1].strip().split()):
        ret[head[i]] = e.strip()
    return ret


def quota_check(uri):
    from model_automation.utils.rmr import run_cmd
    row = {'uri': uri}
    try:
        quota = run_cmd(f"hadoop fs -count -q -v {uri}",
                        print_ret=False,
                        get_ret=True)
        ret = parse_quota(quota)
        row.update(ret)
    except Exception as e:
        print(e)
    return row


def quota_stats(root_dir, max_level=1, use_mp=False):
    """
    get HDFS quota stats under root_dir.
    : params:
    : root_dir: root dir where to start.
    : max_level: max directory hierarchy level to collect quota count. For driectory hierarchy `roo_dir/dir1/sub_dir`, `max_level=1`
        will only return quota count of `roo_dir/dir1`, `max_level=2` will return quota count of `roo_dir/dir1` and `roo_dir/dir1/sub_dir2`.
        
    : return:
        - A pandas dataframe with columns:
            - day_since_last_mod: day since the checked uri last modified time (UTC time).
            - last_mod: checked uri last modified time (UTC time, seconds).
            - owner: owner of the checked uri.
            - quota: file count of all files within the checked uri.
            - uri: the checked uri.
            - level: the checked uri level relative to root_dir.
    """
    import os
    import multiprocessing as mp
    from datetime import datetime

    import pandas as pd
    from hdfs3 import HDFileSystem
    from model_automation.utils.rmr import run_cmd

    hdfs = HDFileSystem(host='horton')
    print(f'walk {root_dir}, max level = {max_level}')
    check_uris = []
    for uri, dirs, fpaths in hdfs.walk(root_dir):
        level = len([e for e in uri.lstrip(root_dir).split('/') if len(e) > 0])
        if level > max_level:
            continue
        check_uris.append(uri)
    print(f'total {len(check_uris)} uris to check')

    if use_mp:
        print(f'use mp to accelerate')
        # too large pool size may cause Java OOM error
        with mp.Pool(8) as pool:
            rows = pool.map(quota_check, check_uris)
    else:
        rows = []
        for i, uri in enumerate(check_uris):
            rows.append(quota_check(uri))

    now = datetime.now()
    for row in rows:
        level = len([e for e in uri.lstrip(root_dir).split('/') if len(e) > 0])
        info = hdfs.info(row['uri'])
        last_mod = datetime.fromtimestamp(int(info['last_mod']))
        row['last_mod'] = last_mod.strftime('%Y-%m-%d %H:%M:%S')
        row['day_since_last_mod'] = (now - last_mod).days
        row['owner'] = info['owner']
        row['quota'] = int(row['FILE_COUNT'])
        row['level'] = int(level)

    df = pd.DataFrame()
    for r in rows:
        df = df.append(r, ignore_index=True)
    return df
