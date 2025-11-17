echo "Before request"
date
http_proxy=http://127.0.0.1:8880 curl http://127.0.0.1:8777
echo "After request"
date