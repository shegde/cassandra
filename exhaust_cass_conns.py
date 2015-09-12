"""
Script to create python thrift connections to Cassandra cluster

 Installation:
 1. Pip
	wget https://bootstrap.pypa.io/get-pip.py
	sudo python get-pip.py

2. Dependencies
	sudo apt-get install gcc python-dev
	sudo apt-get install libev4 libev-dev

3. Cassandra driver
	sudo pip install cassandra-driver

4. Verify
	python -c 'import cassandra; print cassandra.__version__'

5. Optional
	sudo pip install blist

"""

from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from multiprocessing     import Process
from sys                import argv
import time

auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')

def create_conns(server, num):
	conns = []
	for i in range(int(num):
		c = Cluster(['10.5.108.33', '10.5.108.30'], auth_provider=auth_provider)
		c.connect()
		conns.append(c)


if __name__ == '__main__':
	jobs = []
	for i in range(0, 10):
		p=Process(target=create_conns, args=(argv[1], int(argv[2])))
		jobs.append(p)
	for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print "DONE"
