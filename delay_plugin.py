# -*- coding: utf-8 -*-
"""
proxy.py
~~~~~~~~
⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
Network monitoring, controls & Application development, testing, debugging.

:copyright: (c) 2013-present by Abhinav Singh and contributors.
:license: BSD, see LICENSE for more details.
"""
from typing import Optional

from proxy.http.proxy import HttpProxyBasePlugin
from proxy.http.parser import HttpParser
from proxy.common.utils import text_

import uuid

connection_state_table = {}

# we can implement a whitelist instead of blacklist
class SleepPlugin(HttpProxyBasePlugin):
    """Drop traffic by inspecting upstream host."""

    # there is only three async funcs:
    # get_descriptors, write_to_descriptors, read_from_descriptors
    # async def get_descriptors(self):
    #     print("Getting descriptors")
    #     return [], []
    def on_upstream_connection_close(self):
        connection_state_table[self._connection_id]["state"] = "closed"

    def handle_upstream_chunk(self, chunk:memoryview):
        connection_state_table[self._connection_id]["state"] = "established"
        return chunk

    def before_upstream_connection(
        self,
        request: HttpParser,
    ) -> Optional[HttpParser]:
        # assign a unique uuid to each connection
        setattr(self, "_connection_id", str(uuid.uuid4()))
        connection_state_table[self._connection_id] = {"state": "syn_sent"}
        request_host = text_(request.host)
        print("Request host:", request_host)
        if True:
            import time
            time.sleep(5)
        print("Sleeped for 5 seconds")
        return request
