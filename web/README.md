### 开发

```shell
python app.py
```

Flask 文档 https://flask.palletsprojects.com/en/2.2.x/

操作 docx 文档：https://python-docx.readthedocs.io/en/latest/

### Deploy

```shell
docker build -t law:latest .
docker save -o law.tar law:latest
scp law.tar root@xx.xx.xx.xx:/tmp
# ssh to remote
docker load < /tmp/law.tar
docker stop lay
docker run --rm -p 80:80 --name=law -d law:latest
```