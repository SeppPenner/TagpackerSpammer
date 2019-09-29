TagpackerSpammer
====================================
TagpackerSpammer is a software written in Python 3.7.4. Its goal is to spam the website [tagpacker.com](https://tagpacker.com).

[![Build status](https://ci.appveyor.com/api/projects/status/du912lbew4k86yab?svg=true)](https://ci.appveyor.com/project/SeppPenner/tagpackerspammer)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/TagpackerSpammer.svg)](https://github.com/SeppPenner/TagpackerSpammer/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/TagpackerSpammer.svg)](https://github.com/SeppPenner/TagpackerSpammer/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/TagpackerSpammer.svg)](https://github.com/SeppPenner/TagpackerSpammer/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/TagpackerSpammer/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/TagpackerSpammer/badge.svg)](https://snyk.io/test/github/SeppPenner/TagpackerSpammer)

## Basic usage:
Adjust the accounts in the [TagpackerSpammer.py](https://github.com/SeppPenner/TagpackerSpammer/blob/master/TagpackerSpammer.py) file.

The api keys can be taken from tagpacker.com --> Settings --> Account --> API access.

The api key is something like abcawe8gzwf:wgfzwbzf-sdfgsfbsd where the first part is the user id.

In this case we would write:

```python
accounts = [["abcawe8gzwf", "abcawe8gzwf:wgfzwbzf-sdfgsfbsd"]]
```

Execute the script via:

```batch
python TagpackerSpammer.py
```

## Required installation:
Python 3.x

```batch
pip install json
pip install requests
```

and adjust the execution rights:

```batch
chmod +x TagpackerSpammer.py
```

## Run this script as cronjob:

```batch
crontab -e
```

or 

```batch
sudo crontab -e 
```

Add the following line (With replacing the pathtofile of course) to run the script every minute:

```batch
* * * * * /usr/bin/python /pathtofile/TagpackerSpammer.py
```

## Limits:
Only 20 requests per api key per minute are allowed!!!

Change history
--------------

* **Version 1.0.0.1 (2019-09-29)** : Updated python version, updated requirements.
* **Version 1.0.0.0 (2018-02-17)** : 1.0 release.