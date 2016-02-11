#!/usr/bin/env python
# encoding: utf-8
'''
'''
from distutils.core import setup
def install():
    setup(
          name = 'robotframework-websocketclient',
          version = "1.0.0",
          description = "WebSocket testing library for Robot Framework",
          url = 'https://github.com/greums/robotframework-websocketclient',
          classifiers = ['Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Education',
                     'Intended Audience :: End Users/Desktop',
                     'License :: Freeware',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Education',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4'],
          py_modules = ['WebSocketClient'],
          install_requires=['websocket-client'],
          author = 'Steven Mak',
          author_email = 'damien.lebourdonnec@gmail.com',
          scripts=['WebSocketClient.py']
          )

if __name__ == "__main__":
    install()
