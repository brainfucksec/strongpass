### Strongpass v3.4.1

#### Generate strong random passwords 

#### Program Usage:

```
usage: strongpass [-h] [-l LENGHT] [-n NUMBER] [-a {1,0}] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -l LENGHT, --lenght LENGHT
                        Lenght of password
  -n NUMBER, --number NUMBER
                        Number of password to generate
  -a {1,0}, --algorithm {1,0}
                        1 - random password, 0 - pronounceable password
  -v, --version         display program version and exit


Examples:

Generate 10 random passwords of 21 characters lenght:

python strongpass.py -n 10 -a 1 -l 21
{6r|H8C,9=F!*px|BEA[Q
Bf(C^js=ILXjm-U5fy]W_
LHewrXAdCJZ$Q!n+9/&LG
v%Vt-^c!S})2~4rAY\9g,
ARnn&7f^|2:xJQTwgtRxh
N+f%vI}ku29N&fRiyu8.%
_)2e2&,@V+:[$Ds++2?fM
Wg:N\hajTcBm=ye7>A;\c
```



#### Docs:
Documentation about Python 3 module "secrets":
https://docs.python.org/3/library/secrets.html#module-secrets
