#!/usr/bin/env python
import os
import sys
import time

sys.path.append('gen-py')

from tutorial import Calculator

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    print("Start client @ %s" % (os.getpid()))
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Calculator.Client(protocol)

    # Connect!
    transport.open()

    print("Start thrift req")
    start = time.time()
    res = client.get_image()
    dur = time.time() - start
    print("get %d bytes in %s" % (len(res), dur))


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
