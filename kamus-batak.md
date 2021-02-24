## Batak Language Word Translator to Bahasa Indonesia (default) or Otherwise

> This is just for educational purpose. Use it at your own risk

## Usage

Add to `.bashrc`, `.profile`, or any startup shell scripts
```bash
$ alias kamus-batak.py="python3 {PATH_TO_Koleksi_DIR}/kamus-batak.py.py"
```

```bash
~/Koleksi$ kamus-batak.py -h
usage: kamus-batak.py [-h] [-i] Words) [Word(s ...]

Kamus Bahasa Batak - Indonesia dan sebaliknya

positional arguments:
  Word(s)     Kata / kalimat yang ingin di terjemahkan

optional arguments:
  -h, --help  show this help message and exit
  -i          Bahasa Indonesia - Batak
```

Batak Language to Bahasa Indonesia
```bash
~/Koleksi$ kamus-batak.py horas
 ▶️ horas = selamat, damai sejahtera yang diucapkan dalam acara pesta adat Batak, damai, sejahtera, teguh, sapaan salam hormat, selamat datang, halo, selamat jalan
 ▶️ Bahasa indonesia-nya kata: dihorasi
   direstui
 ▶️ Bahasa indonesia-nya kata: horas
   selamat
 ▶️ Bahasa indonesia-nya kata: horas
   damai sejahtera yang diucapkan dalam acara pesta adat Batak
 ▶️ Bahasa indonesia-nya kata: horas
   damai
 ▶️ Bahasa indonesia-nya kata: horas
   sejahtera
 ▶️ Bahasa indonesia-nya kata: horas
   teguh
 ▶️ Bahasa indonesia-nya kata: horas
   sapaan salam hormat
 ▶️ Bahasa indonesia-nya kata: horas
   selamat datang
 ▶️ Bahasa indonesia-nya kata: horas
   halo
 ▶️ Bahasa indonesia-nya kata: horas
   selamat jalan
```

Bahasa Indonesia to Bahasa Batak
```bash
~/Koleksi$ kamus-batak.py -i "damai sejahtera"
 ▶️ Bahasa batak-nya kata: damai sejahtera
   dame na sumurung
 ▶️ Bahasa batak-nya kata: damai sejahtera yang diucapkan dalam acara pesta adat Batak
   horas
 ▶️ Bahasa batak-nya kata: damai sejahtera
   sonang sohariboriboan
```

## Deps

- [Requests](http://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```bash
pip3 install --user beautifulsoup4 requests
```

## [<< Back to main page](https://github.com/jockerz/Koleksi) 

