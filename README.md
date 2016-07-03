## Morbi
Morbi is a commandline dating algorithm that allows to for matching users to one another.

### Installation
To install just clone the repo and from the root directory of the project enter the following commands.
```
$ python morbi/run.py
```

### Commands
Morbi allows the following commands:
* Adding a user.
```
$ add_user PersonA {(25, 35), [Running, Biking, Trekking, Reading], {age:20, }}
$ add_user PersonB {(32, 27), [Sketching, Music, Painting], {age:20, }}
$ add_user PersonC {(9, 35), [Running, Trekking], {}}
$ add_user PersonD {(22, 37), [Sketching, Travelling], {}}
$ add_user PersonE {(17, 42), [Running, Reading, Trekking], {}}
$ add_user PersonF {(24, 32), [Running, Trekking, Travelling], {age:20, gender:m}}
```

* Viewing a user.
```
$ user PersonF
```

* Matching a user.
```
$ match_very_near PersonA age:20 gender:m
```

* Help:
```
$ help
```
