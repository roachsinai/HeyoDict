## HeyoDict

A command line dict (English <-> Chinese) tool developed in python

HeyoDict is based on Youdao Open API. http://fanyi.youdao.com/openapi?path=data-mode

---

### Usage:

```
dict -d word[s] # English word[s] to Chinese.
dict -t word    # Chinese word to English.
dict -v word[s] # English word[s] to Chinese, and with pronunciation.
dict -r         # replay the pronunciation of last English word[s].
dict -m word[s] # same to -d option, but show More things, like phrases.
dict word[s]    # mixture of -d and -t, but you should input either English word[s] or Chinese word[s].
```

### dependencies

To make a voice, you should install one dependency `sox` by:

`sudo pacman -S sox`

and create a folder to store the pronunciation file by:

`mkdir ~/.dict_youdao/voice -p`

as each time you run this tool with -d option, the corresponding pronunciation file will download and write it to that only file.
