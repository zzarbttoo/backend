### 운영 
---
- 직접 실행 명령어(fast api)
   - 프로젝트 최상단에서 하위 명령어로 실행 
   - port와 env 파일은 명령어로 지정해주시면 됩니다 (하위는 port : ramdome , env : local 실행 )
```
python3 -m uvicorn app.main:app --reload --port 8080 --env-file app/config/local.env
```

<br/>

- docker build, running 
```
# docker build 
docker build --tag {컨테이너명}:1.0 .

#docker running 
docker run --network host --name {컨테이너명} -p 0:0  --env-file={}/app/config/dev.env {}:1.0 
``` 
