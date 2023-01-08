# 导包
from elasticsearch import Elasticsearch

# 在创建es对象的时候什么都不写,连接的是127.0.0.1：9200
# es = Elasticsearch()
# es = Elasticsearch(hosts="127.0.0.1:9200")
es = Elasticsearch(hosts=["192.168.0.101:9200"])
# print(es.ping())
# print(es.info())

# 创建索引
# print(es.indices.create(index="imooc"))

# 查看索引
# print(es.cat.indices())
# print(es.indices.delete(index="imooc"))
# print(es.cat.indices())

# 创建索引并插入数据
# print(es.index(index="imooc", body={"name": "大壮", "age": 18}))
# print(es.index(index="imooc", body={"name": "张三", "age": 20}, id=1))
# print(es.search(index="imooc"))
# print(es.get(index="imooc", id=1))
# print(es.search({
#     "query": {
#         "match": {
#             "name": "大壮"
#         }
#     }
# }))

# 数据的更新
# body = {
#     "doc": {
#         "tags": "imooc"
#     }
# }
# print(es.get(index="imooc", id=1))
# print(es.update(index="imooc", id=1, body=body))
# print(es.get(index="imooc", id=1))

# 数据的删除
# es.delete(index="imooc", id=1)
print(es.get(index="imooc", id=1))
