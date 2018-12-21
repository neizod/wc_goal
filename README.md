Word Count Goal
===============

Trace your writing on markdown blog.


Install Requirements
--------------------

Clone this repo and go into the repo's directory, then run

``` bash
$ pip install -r requirements.txt
```

Sorry no PYPI, yet.


Config & Use
------------

On the repo's directory, copy the example config `config.example.yml` into `config.yml`, then change it's values to suite your preferences. For example,

``` yaml
watch:      # local markdown files to analyse.
  - ~/mainblog.github.io/_posts/*.md
  - ~/anotherblog.github.io/_posts/*.md
  - ~/ideas/*.md
report:     # which report do you want to see?
  - per article
```

Then run,

``` bash
$ ./wc_goal
```

Example output:

```
year |   wc   |              hist             
---- | ------ | ------------------------------
2011 |   6815 | ▒▒▒▒▒▒
2012 |  17806 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
2013 |  11822 | ▒▒▒▒▒▒▒▒▒▒
2014 |  13296 | ▒▒▒▒▒▒▒▒▒▒▒▒
2015 |  11417 | ▒▒▒▒▒▒▒▒▒▒
2016 |  22176 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
2017 |   8864 | ▒▒▒▒▒▒▒▒
2018 |  34552 | ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
```
