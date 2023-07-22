#!/usr/bin/env bash
set -e
cd $(dirname "$0")/py

ps ax | grep -E "jupyter-lab" | grep -v "grep" | awk '{print $1}' | xargs -I {} kill -9 {}

jupyter_log_file='.logs/jupyter.logs'

rm -r ${jupyter_log_file} || True

mkdir -p $(dirname ${jupyter_log_file})

touch ${jupyter_log_file}

nohup jupyter-lab > ${jupyter_log_file} 2>&1 &

echo 'jupyter-lab is running'

