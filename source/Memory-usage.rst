Memory usage is a tricky thing to pin down, especially when shared libraries are involved. Analysis of the outstationdemo program with the memory profiler Valgrind (massif) suggests that heap usage is very low. Total memory usage seems to be dominated by the required shared libraries. Total memory usage is less than 16MB even if all of the shared libraries. Most programs will load shared libraries like libc and libstdc++ anyway so this portion of the memory usage is really shared by opendnp3 and any other applications you choose to run. Below is the output of the pmap -x utility showing the libraries loaded by opendnp3:

```
19383:   ./outstationdemo
Address   Kbytes     RSS   Dirty Mode   Mapping
08048000       0      12       0 r-x--  outstationdemo
0804c000       0       4       4 r----  outstationdemo
0804d000       0       4       4 rw---  outstationdemo
08e03000       0      40      40 rw---    [ anon ]
b6900000       0       4       4 rw---    [ anon ]
b6921000       0       0       0 -----    [ anon ]
b6af0000       0       0       0 -----    [ anon ]
b6af1000       0      28      28 rw---    [ anon ]
b72f4000       0      24       0 r-x--  libm-2.15.so
b731e000       0       4       4 r----  libm-2.15.so
b731f000       0       4       4 rw---  libm-2.15.so
b7320000       0       8       0 r-x--  libboost_system.so.1.53.0
b7322000       0       4       4 r----  libboost_system.so.1.53.0
b7323000       0       4       4 rw---  libboost_system.so.1.53.0
b7324000       0     452       0 r-x--  libc-2.15.so
b74c7000       0       0       0 -----  libc-2.15.so
b74c8000       0       8       8 r----  libc-2.15.so
b74ca000       0       4       4 rw---  libc-2.15.so
b74cb000       0      12      12 rw---    [ anon ]
b74ce000       0      16       0 r-x--  libgcc_s.so.1
b74ea000       0       4       4 r----  libgcc_s.so.1
b74eb000       0       4       4 rw---  libgcc_s.so.1
b74ec000       0     464       0 r-x--  libstdc++.so.6.0.17
b75c8000       0       0       0 -----  libstdc++.so.6.0.17
b75c9000       0      16      16 r----  libstdc++.so.6.0.17
b75cd000       0       4       4 rw---  libstdc++.so.6.0.17
b75ce000       0      16      16 rw---    [ anon ]
b75d6000       0      72       0 r-x--  libpthread-2.15.so
b75ed000       0       4       4 r----  libpthread-2.15.so
b75ee000       0       4       4 rw---  libpthread-2.15.so
b75ef000       0       4       4 rw---    [ anon ]
b75f1000       0     616       0 r-x--  libopendnp3.so.1.0.1
b76dc000       0      60      60 r----  libopendnp3.so.1.0.1
b76eb000       0       4       4 rw---  libopendnp3.so.1.0.1
b76ec000       0       4       4 rw---    [ anon ]
b76fd000       0      12      12 rw---    [ anon ]
b7701000       0       4       0 r-x--    [ anon ]
b7702000       0     104       0 r-x--  ld-2.15.so
b7722000       0       4       4 r----  ld-2.15.so
b7723000       0       4       4 rw---  ld-2.15.so
bffcb000       0       8       8 rw---    [ stack ]
-------- ------- ------- ------- -------
total kB   13744       -       -       -
```