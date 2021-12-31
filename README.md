# Bitcoin Stackexchange To Markdown

Fetch the [bitcoin stackexchange](https://bitcoin.stackexchange.com/) answers and export it as a markdown file.

## Setup

```bash
git clone https://github.com/arnabsen1729/btc_stackexchange_markdown.git
python3 setup.py install
```

## Usage

Every question on stackexchange has an unique id. That id needs to be used to fetch the questions and the corresponding answers.

```bash
$ btcmd 84004 q1.md
[-] Fetching data of question 84004
[*] Found an accepted answer
[*] Exporting to q1.md
[√] Done!
```

By default it will consider accepted answers. If some question doesn't have any accepted answers it will prompt for the available answers to fetch from.

```bash
$ btcmd 89385 q1.md
[-] Fetching data of question 89385
[!] There is no accepted answer, choose the answer you want to use.
1: 89418
2: 89387
> 1
[*] Exporting to q1.md
[√] Done!
```
