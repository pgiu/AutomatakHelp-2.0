OpenDNP3 has a few bells and whistles that allow you optimize your binary for size on embedded systems. Here's a summary of options that you can feed to the configure script:

* **--enable-opendnp3nomaster** - Strips out the master from Makefile.am for embedded systems that only need the outstation. This configure option defines the directive OPENDNP3_NO_MASTER which strips out references to the master from the channel interface.

* **--enable-opendnp3noserial** - Strips out serial port support from Makefile.am for embedded systems that only need IP connectivity. This configure option defines the direction OPENDNP3_NO_SERIAL which strips out references to serial class from the DNP3Manager class.

* **--enable-opendnp3nomocks** - OpenDNP3 contains a few interface reference implementations shared by demos and tests. This configure options strips these out. 

* **-DOPENDNP3_SUPPRESS_LOG_LOCATION** - For debugging purposes, file and line number location gets compiled into the library as string literals. This can be stripped out with this directive.

* **-DOPENDNP3_STRIP_LOG_MESSAGES** - Strips out log messages, associated ToString functions and exception descriptions.

* **-DOPENDNP3_LIMIT_VISIBILITY** - Marks internal classes / functions as such. This allows the compiler to reduce the size of the symbol table and results in faster load times as well. This option is not set by default, because the test suite needs access to internal classes.

Feeding all of these options to configure and optimizing for size would look like:
```
$ ./configure --enable-opendnp3nomaster --enable-opendnp3nomocks --enable-opendnp3noserial "CXXFLAGS=-Os -DOPENDNP3_SUPPRESS_LOG_LOCATION -DOPENDNP3_STRIP_LOG_MESSAGES -DOPENDNP3_LIMIT_VISIBILITY"
```

When you go to install your library don't forget to strip it to further reduce the size:
```
$ sudo make install-strip
```

As of 02/23/13 this process produced the following x86 library size with G++4.7:

```
757416 Feb 23 19:56 /usr/lib/libopendnp3.so.1.0.1
```