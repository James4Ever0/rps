export PYTHONPATH=. # in order to find the plugin
# https://github.com/abhinavsingh/proxy.py/issues/726
# proxy --plugin ManInTheMiddlePlugin
HOSTNAME=127.0.0.1
PORT=8880
echo "Proxy hosted at: http://$HOSTNAME:$PORT"

# dashboard might be a security loophole, since it allows live configuration changes via web requests. we might want to use it before production. if anyone wants to inspect traffic in production, better use custom plugins instead.
# echo "Visit dashboard at: http://$HOSTNAME:$PORT/dashboard"

# use threaded if use "time.sleep" in the plugin

proxy --plugin delay_plugin.SleepPlugin --threaded --port $PORT --hostname $HOSTNAME # --enable-dashboard