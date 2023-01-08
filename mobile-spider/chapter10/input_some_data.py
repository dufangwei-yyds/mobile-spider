import time
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(hosts="192.168.0.101:9200")
print(es.ping())


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print("共消耗%.3f秒" % (time.time() - start_time))
        return res

    return wrapper


@timer
def handle_es():
    # 传统插入数据方式,通过遍历的方式进行插入,共消耗122.611秒
    # for value in range(10000):
    #     es.index(index="value_demo", body={"value": value})

    # 通过helpers.bulk方法插入数据，一个大的列表共消耗6.400秒
    # data = [{"_index": "value_demo", "_source": {"value": value}} for value in range(10000)]
    # 通过helpers插入数据
    # helpers.bulk(es, data)

    # 共消耗0.000秒
    for value in range(10000):
        yield {"_index": "value_demo", "_source": {"value": value}}


if __name__ == '__main__':
    # handle_es()

    helpers.bulk(es, actions=handle_es())
    print(es.count(index="value_demo"))