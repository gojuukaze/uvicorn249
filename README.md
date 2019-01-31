# recreate [#249](https://github.com/encode/uvicorn/pull/249)



# run 

```bash

# run redis 127.0.0.1 6379
redis-server &

pip install -r requirements.txt

uvicorn uvicorn249.asgi:application --host 0.0.0.0 --port 8000 --ws wsproto --debug


```

# connect ws
```bash
python client_ws.py

```

# run with docker

```bash
docker-compose -f docker-compose.yml up -d
docker logs -f uvicorn249

```



