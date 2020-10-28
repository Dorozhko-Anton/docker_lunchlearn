# docker_lunchlearn


```
docker build -t fast:1.0 .

docker run -it --rm --name fast fast:1.0 bash

docker run -it --rm --name fast fast:1.0


docker run -it --rm --name fast fast:1.0 -v `pwd`:/app/ 


docker run -it --rm --name fast fast:1.0 -p 8888:8000 -v `pwd`:/app/
```