import time
import sys

import stomp
"""
class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)


hosts=[('localhost', 61613)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

conn.subscribe(destination='/topic/home', id=1, ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/topic/home')

time.sleep(2)
conn.disconnect()
"""
class HornetqListener(object):
    def on_connecting(self, host_and_port):
        print('on_connecting %s %s' % host_and_port)
    def on_error(self, headers, message):
        print('received an error %s' % (headers, message))
    def on_message(self, headers, body):
        print('on_message %s %s' % (headers, body))
    def on_heartbeat(self):
        print('on_heartbeat')
    def on_send(self, frame):
        print('on_send %s %s %s' % (frame.cmd, frame.headers, frame.body))
    def on_connected(self, headers, body):
        print('on_connected %s %s' % (headers, body))
    def on_disconnected(self):
        print('on_disconnected')
    def on_heartbeat_timeout(self):
        print('on_heartbeat_timeout')
    def on_before_message(self, headers, body):
        print('on_before_message %s %s' % (headers, body))
        return (headers, body)
    
hosts=[('localhost', 61613)]
conn = stomp.Connection(host_and_ports=hosts ,keepalive=True ) #,vhost='irs.example.com', heartbeats=(20,20))

conn.set_listener('',HornetqListener())

conn.start()

conn.connect('guest', 'guest', wait=True)
 

conn.subscribe(destination='/topic/home', id='trans1', ack='auto')

conn.send(body='the current time is: 458 '  , destination='/topic/home',persistent='true')

conn.disconnect()

