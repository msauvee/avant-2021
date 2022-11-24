# How to setup

* Copy all current files in a new folder named XX
* open menu 'View | Terminal', add venv : `python3 -m venv .venv`
* set python interpreter (`Command + Shift + P`) and select local one
* set Python Test Configuration  (`Command + Shift + P`), select pytest with 'root', and accept installation
* discover tests, and run all tests

Ready !!

0 => 6 seg
1 => 2 seg*
2 => 5 seg
3 => 5 seg
4 => 4 seg*
5 => 5 seg
6 => 6 seg
7 => 3 seg*
8 => 7 seg*
9 => 6 seg

1 = [xx]
4 = [xxxx]
7 = [xxx]
8 = [xxxxxxx]

5 seg => 2, 3 ou 5
6 seg => 0, 6 ou 9

Segments:

 1111
6    2
6    2
6    2
 7777
5    3
5    3 
5    3
 4444 

6-7=4
9-7=3
0-7=3

6-1=5
9-1=4
0-1=4

6-4=3
9-4=2
0-4=3

