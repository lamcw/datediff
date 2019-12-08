# datediff

Computes number of full days elapsed between two arbitrary dates.

```console
$ datediff 02/06/1983 - 22/06/1983
19
```

## Installation

You can install the package after generating the wheel package by `poetry`.

```console
$ poetry build -f wheel
Building datediff (0.1.0)
 - Building wheel
 - Built datediff-0.1.0-py3-none-any.whl
$ pip install dist/datediff-0.1.0-py3-none-any.whl
```
