# autoheal
# How to use
```
docker run -d \
    --name autoheal \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
   xiaocaicai/autoheal
```