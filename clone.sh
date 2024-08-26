set -e

rm -rf cgc-challenge-corpus
git clone https://github.com/lungetech/cgc-challenge-corpus.git
python3 rename_builtins.py
