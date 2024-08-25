set -e

rm -rf cgc-challenge-corpus
git clone https://github.com/Mem2019/cgc-challenge-corpus.git
find cgc-challenge-corpus -type f -exec \
	sed -i 's|main(void)|main(int, char **, char **)|g' {} +
rm -rf tmp