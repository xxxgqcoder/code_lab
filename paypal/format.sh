#!/bin/sh
set -e

cd $(dirname "$0")

# find and format python files
# find . -type f -name '*py' \( -not -path "*/__pycache__/*" -and -not -path "*/.git/*" -and -not -path "*/.ipynb_checkpoints/*" \) -prune \
#     -exec yapf -i {} +

# format changed python files
git ls-files -m | grep -E "\.py" | xargs -I {} yapf -i {}