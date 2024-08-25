set -e

rm -rf tmp
git clone https://github.com/lungetech/cgc-challenge-corpus.git tmp
rm -rf cgc-challenge-corpus && mkdir cgc-challenge-corpus
cat targets.txt | xargs -I{} mv tmp/{} cgc-challenge-corpus/
rm -rf tmp