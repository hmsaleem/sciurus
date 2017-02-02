# sciurus
## A minimalist Python function scheduler

Sciurus is a minimal scheduler for Python. 

Ever wanted to run a function every X minutes?
Sleep doesn't cut it if you have long running processes...

Enter Sciurus.

## How to use

```python
from sciurus import scheduler


def fn(a,b):
	print a+b
	return

ss = scheduler.scheduler(s=3)
ss.runit(fn, 1, 3)
```

Create a scheduler object, intialising it with the time interval.

```python
ss = scheduler.scheduler(h=1, m=2, s=3)
```

Run your function with specific arguments.

```python
ss.runit(fn, arg1, arg2, ...)
```

## Use case

Sciurus is especially useful in cases where you wish to run same function again and again. For example, continuous web scraping.


