## Bahasa Indonesia Word Translator to English (default) or Otherwise 

> This is just for educational purpose. Use it at your own risk

## Usage

Add to `.bashrc`, `.profile`, or any startup shell scripts
```bash
$ alias kamus="python3 {PATH_TO_Koleksi_DIR}/kamus-cli.py"
```

```bash
~/Koleksi$ kamus -h
usage: kamus-cli.py [-h] [-e] Words) [Word(s ...]

Word translator Bahasa Indonesia to English(default) or otherwise

positional arguments:
  Word(s)     Word to translate

optional arguments:
  -h, --help  show this help message and exit
  -e          English to Bahasa Indonesia

~/Koleksi$ kamus percobaan
[Term]:   percobaan
[Result]: attempt, checkout, flyer, experiment, probation, testing, trial, try, tryout, workout, experiment, experimenter, experimentalist

~/Koleksi$ python kamus-cli.py -e test
[Term]:   test (v)
[Result]: mencoba, ujian, cobaan
[Term]:   test (n)
[Result]: tes


```

## Deps

- [Requests](http://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```bash
pip3 install --user beautifulsoup4 requests
```

## [<< Back to main page](https://github.com/jockerz/Koleksi) 

