# Installation Notes

## What NOT to Install

Most people will feel the urge typing `pip install z3`. STOP! That's the package for interfacing with Amazon S3! Check their page https://pypi.org/project/z3/ as see that it says loud and clear:

> Backup ZFS snapshots to S3

## What to Install

You should install `z3-sovler` for Python:

```
pip install z3-solver
```

Feel free to check their page here: https://pypi.org/project/z3-solver/

## For Hardcore People Who Love Compiling

I really enjoy building and compiling packages. This love comes with pain and Z3 has quirks when you are trying to install it. Some steps to alleviate the pain:

```
$ sudo chmod -R a+r /usr/lib/python2.7/dist-packages/z3
$ sudo chmod a+x /usr/lib/python2.7/dist-packages/z3
$ sudo chmod a+x /usr/lib/python2.7/dist-packages/z3/lib

$ sudo chmod -R a+r /usr/lib/python3.5/dist-packages/z3
$ sudo chmod a+x /usr/lib/python3.5/dist-packages/z3
$ sudo chmod a+x /usr/lib/python3.5/dist-packages/z3/lib

$ sudo chmod a+rx /usr/lib/libz3.so
```

Only then you can do the basic import operation:

```
>>> from z3 import *
```
