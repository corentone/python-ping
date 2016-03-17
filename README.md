# Pure Python3 ping (ICMP)

Running this requires root access or raw socket access.
Only runs on Python3. Tested on Python 3.4.3.


## Usage
To run:
```python
import ping

# delay = ping.do_one(dest_addr, timeout)

#pings github.com with a 2s timeout and returns the delay
delay = ping.do_one('github.com', 2)

```

## Install
You can simply import the ping module or in the case of a bigger project with requirements.txt, use
`pip install git+git://github.com/corentone/python3-ping.git#egg=ping`.

== License ==
License from Matthew Dixon Cowles is GNU GPL v2 so this repository is as well in GNU GPL v2

Originally from http://svn.pylucid.net/pylucid/CodeSnippets/ping.py
This version maintained at http://github.com/samuel/python-ping
