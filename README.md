### Порядок действий

1. После создания проекта, создаем файл с описанием glossary.proto <br/>
2. Устанавливаем virtualenv <br/>
3. Активвируем виртуальное окружение ```virtualenv env . env/bin/activate``` <br/>
4. Устанавливаем
```python -m pip install --upgrade pip``` <br/>
```python -m pip install grpcio``` <br/>
```python -m pip install grpcio-tools``` <br/>
5. Запускаем команду<br/>
```python -m grpc_tools.protoc -I./protobufs --python_out=. --pyi_out=. --grpc_python_out=. ./protobufs/glossary.proto```<br/>
Появляются три файла glossary_pb2.py glossary_pb2.pyi glossaryd_pb2_grpc.py.<br/>
6.Создаем dictionaryClient.py и dictionaryServer.py <br/>
7.Запускаем сначала север (python glossaryServer.py), потом клиент (python glossaryClient.py)<br/>
