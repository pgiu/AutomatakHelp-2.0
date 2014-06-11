```
./configure CXXFLAGS="--coverage -g -O0" LDFLAGS="--coverage -g -O0"
```

``
make check
./dnp3test
./openpaltest
```

now generate the info file with lcov
```
lcov -c -d ./ -b ./ -o coverage.info
```

and then the html versions:
```
genhtml coverage.info -o test_html
```