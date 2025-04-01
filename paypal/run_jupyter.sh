#!/usr/bin/env bash
set -e

port_num=3456

ps aux | grep "jupyter-lab" | grep "${port_num}" | awk '{print $2}' | xargs -I {} kill -9 {} || true

echo "removing running log"

rm notebook.log || true

nohup jupyter lab --port=${port_num} > notebook.log 2>&1 & 

echo "jupyter notebook started"
