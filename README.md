# CGC Multi-arch

This is a repository containing build scripts to build CGC binaries as Linux binaries for different operating systems.
It is loosely based on TrailOfBits' cb-multios.

## Usage

```bash
cd cgc-multiarch
bash clone.sh
cd cgc-challenge-corpus && git apply ../corpus.diff && cd ..
make
```