ft_package
==========

Provides count_in_list(lst, value).

Usage:

```py
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

To install it, first build using 
```
python3 -m build
```

make sure to have installed these dependencies
```
python3 -m pip install --upgrade build setuptools wheel
```

then run one of these commands
```
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
