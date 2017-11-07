### strongpass

#### Version: 3.6.1

#### Generate strong random passwords




##### Program Usage:

```bash
usage: strongpass [-h] [-l LENGHT] [-n NUMBER] [-m {0,1,2}] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -l LENGHT, --lenght LENGHT
                        Lenght of passwords
  -n NUMBER, --number NUMBER
                        Number of passwords to generate
  -m {0,1,2}, --mode {0,1,2}
                        Passwords generation mode: 0 only letters, 1 random, 2
                        alphanumeric
  -v, --version         display program version and exit
```


##### Examples:

__Generate 10 random passwords of 21 characters lenght:__
```bash
./strongpass.py -n 10 -m 1 -l 21
{6r|H8C,9=F!*px|BEA[Q
Bf(C^js=ILXjm-U5fy]W_
LHewrXAdCJZ$Q!n+9/&LG
v%Vt-^c!S})2~4rAY\9g,
ARnn&7f^|2:xJQTwgtRxh
N+f%vI}ku29N&fRiyu8.%
_)2e2&,@V+:[$Ds++2?fM
Wg:N\hajTcBm=ye7>A;\c
```

__Generate 10 alphanumeric passwords of 15 characters lenght:__
```bash
./strongpass.py -n 10 -m 2 -l 15
XRywgJfyjLiQPGB
WFaakuYZYvrZYVt
yzzFBrtGYeYCcSa
mzXRryuHdayAvGE
UtymQptCJPxPQfV
EkbWHSJnvrtKdbT
VZqWBYkgSttViVx
qhmykZCHWQiwPEH
EeFxTyLZbjAfQTw
ekHJTCtPNqCHWDY
```



#### Docs:
Documentation about Python 3 module "secrets":
https://docs.python.org/3/library/secrets.html#module-secrets
