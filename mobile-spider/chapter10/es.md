# es基本的增删改查
PUT test1

GET _cat/indices

DELETE test1

PUT test1/_doc/1
{
  "name": "大壮",
  "age": 18,
  "location": "北京"
}

GET test1/_doc/1

PUT test1/_doc/2
{
  "name": "张三",
  "age": 19,
  "location": "上海"
}

PUT test1/_doc/3
{
  "name": "李四",
  "age": 20,
  "location": "广州"
}

GET test1/_search

POST test1/_update/1
{
  "doc": {
    "location":"北京市朝阳区"
  }
}

DELETE test1/_doc/1

DELETE test1

# es查询进阶
PUT test1/_doc/1
{
  "name": "曹操",
  "gender": "男",
  "age": 50,
  "country": "魏国",
  "tags": "权谋狡诈"
}

PUT test1/_doc/2
{
  "name": "刘备",
  "gender": "男",
  "age": 40,
  "country": "蜀国",
  "tags": "收买人心"
}


PUT test1/_doc/3
{
  "name": "孙权",
  "gender": "男",
  "age": 30,
  "country": "吴国",
  "tags": "权力制衡"
}

PUT test1/_doc/4
{
  "name": "司马懿",
  "gender": "男",
  "age": 41,
  "country": "魏国",
  "tags": "暗藏韬略"
}

PUT test1/_doc/5
{
  "name": "诸葛亮",
  "gender": "男",
  "age": 39,
  "country": "蜀国",
  "tags": "智谋超群"
}

PUT test1/_doc/6
{
  "name": "周瑜",
  "gender": "男",
  "age": 38,
  "country": "吴国",
  "tags": "气量狭小"
}

PUT test1/_doc/7
{
  "name": "许诸",
  "gender": "男",
  "age": 20,
  "country": "魏国",
  "tags": "力大无穷"
}

PUT test1/_doc/8
{
  "name": "关羽",
  "gender": "男",
  "age": 21,
  "country": "蜀国",
  "tags": "青龙偃月"
}

PUT test1/_doc/9
{
  "name": "吕蒙",
  "gender": "男",
  "age": 19,
  "country": "吴国",
  "tags": "吴下阿蒙"
}

PUT test1/_doc/10
{
  "name": "大乔",
  "gender": "女",
  "age": 18,
  "country": "吴国",
  "tags": "沉鱼落雁"
}

PUT test1/_doc/11
{
  "name": "小乔",
  "gender": "女",
  "age": 17,
  "country": "吴国",
  "tags": "闭月羞花"
}

GET test1/_doc/1

GET test1/_search

GET test1/_search?q=country="魏国"

GET test1/_search
{
  "query": {
    "match": {
      "country": "魏国"
    }
  }
}

#country text 以or的形式进行匹配
#country.keyword 不会进行分词
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "魏国"
    }
  }
}

#select * from tables
GET test1/_search
{
  "query": {
    "match_all": {}
  }
}

# es查询排序
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "魏国"
    }
  },
  "sort": [
    {
      "age": {
        "order": "desc"
      }
    }
  ]
}
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "魏国"
    }
  },
  "sort": [
    {
      "age": {
        "order": "asc"
      }
    }
  ]
}

# es分页查询
GET test1/_search
{
  "query": {
    "match_all": {}
  },
  "from": 0,
  "size": 2
}

# es布尔查询
GET test1/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "country": "蜀国"
          }
        },
        {
          "match": {
            "gender": "男"
          }
        },
        {
          "match": {
            "age": "39"
          }
        }
      ]
    }
  }
}
GET test1/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "age": "39"
          }
        },
        {
          "match": {
            "tags.keyword": "闭月羞花"
          }
        }
      ]
    }
  }
}
GET test1/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "match": {
            "age": "39"
          }
        },
        {
          "match": {
            "gender": "男"
          }
        },
        {
          "match": {
            "tags.keyword": "闭月羞花"
          }
        }
      ]
    }
  }
}
GET test1/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "country.keyword": "魏国"
          }
        }
      ],
      "filter": [
        {
          "range": {
            "age": {
              "gt": 39
            }
          }
        }
      ]
    }
  }
}

# es结果过滤
GET test1/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "country.keyword": "魏国"
          }
        }
      ],
      "filter": [
        {
          "range": {
            "age": {
              "gt": 39
            }
          }
        }
      ]
    }
  },
  "_source": "name"
}
GET test1/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "country.keyword": "魏国"
          }
        }
      ],
      "filter": [
        {
          "range": {
            "age": {
              "gt": 39
            }
          }
        }
      ]
    }
  },
  "_source": ["name","age"]
}

# es高亮显示
GET test1/_search
{
  "query": {
    "match": {
      "tags": "沉鱼落雁"
    }
  },
  "highlight": {
    "fields": {
      "tags": {}
    }
  }
}
GET test1/_search
{
  "query": {
    "match": {
      "tags": "沉鱼落雁"
    }
  },
  "highlight": {
    "pre_tags": "<b>",
    "post_tags": "</b>", 
    "fields": {
      "tags": {}
    }
  }
}
GET test1/_search
{
  "query": {
    "match": {
      "tags": "沉鱼落雁"
    }
  },
  "highlight": {
    "pre_tags": "<b style='color:red'>",
    "post_tags": "</b>", 
    "fields": {
      "tags": {}
    }
  }
}

# es聚合函数查询
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "吴国"
    }
  },
  "aggs": {
    "age_avg": {
      "avg": {
        "field": "age"
      }
    }
  },
  "_source": ["name","age"]
}
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "吴国"
    }
  },
  "aggs": {
    "age_avg": {
      "avg": {
        "field": "age"
      }
    }
  },
  "_source": ["name","age"],
  "size": 0
}
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "吴国"
    }
  },
  "aggs": {
    "age_max": {
      "max": {
        "field": "age"
      }
    }
  },
  "_source": ["name","age"],
  "size": 1
}
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "吴国"
    }
  },
  "aggs": {
    "age_min": {
      "min": {
        "field": "age"
      }
    }
  },
  "_source": ["name","age"],
  "size": 1
}
GET test1/_search
{
  "query": {
    "match": {
      "country.keyword": "吴国"
    }
  },
  "aggs": {
    "age_sum": {
      "sum": {
        "field": "age"
      }
    }
  },
  "_source": ["name","age"],
  "size": 1
}

# es分组查询
GET test1/_search
{ "size": 0, 
  "query": {
    "match_all": {}
  },
  "aggs": {
    "agg_group": {
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 10,
            "to": 20
          },
            {
            "from": 20,
            "to": 30
          },
            {
            "from": 30,
            "to": 40
          },
            {
            "from": 40,
            "to": 50
          }
        ]
      }
    }
  }
}
GET test1/_search
{ "size": 0, 
  "query": {
    "match_all": {}
  },
  "aggs": {
    "agg_group": {
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 10,
            "to": 20
          },
            {
            "from": 20,
            "to": 30
          },
            {
            "from": 30,
            "to": 40
          },
            {
            "from": 40,
            "to": 50
          }
        ]
      },
      "aggs": {
        "age_avg": {
          "avg": {
            "field": "age"
          }
        }
      }
    }
  }
}

# es mappings的三种模式
PUT test2/_doc/1
{
  "name":"王百万"
}

GET test2

PUT test2/_doc/2
{
  "name":"赵金条",
  "age":18
}
PUT mappings_test1
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "long"
      }
    }
  }
}
PUT mappings_test1/_doc/1
{
  "name":"大壮",
  "age":20
}

GET mappings_test1

GET mappings_test1/_search

PUT mappings_test1/_doc/2
{
  "name":"大壮",
  "age":20,
  "company": "imooc"
}
GET mappings_test1/_search
{
  "query": {
    "match": {
      "company": "imooc"
    }
  }
}

PUT mappings_test2
{
  "mappings": {
    "dynamic": false,
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "long"
      }
    }
  }
}

GET mappings_test2

PUT mappings_test2/_doc/1
{
  "name":"张三",
  "age":19
}

PUT mappings_test2/_doc/2
{
  "name":"李四",
  "age":18,
  "company":"imooc"
}
GET mappings_test2/_search
{
  "query": {
    "match_all": {}
  }
}
GET mappings_test2
GET mappings_test2/_search
{
  "query": {
    "match": {
      "company": "imooc"
    }
  }
}
PUT mappings_test3
{
  "mappings": {
    "dynamic": "strict",
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "long"
      }
    }
  }
}

GET mappings_test3

PUT mappings_test3/_doc/1
{
  "name": "王五",
  "age":21
}

PUT mappings_test3/_doc/1
{
  "name": "赵六",
  "age":22,
  "company":"imooc"
}

# es的分词器
POST _analyze
{
  "analyzer": "standard",
  "text": "Hello World&端午节"
}
POST _analyze
{
  "analyzer": "simple",
  "text": "Hello World&端午节"
}
POST _analyze
{
  "analyzer": "whitespace",
  "text": "Hello World&端午节"
}
POST _analyze
{
  "analyzer": "standard",
  "text": "八百标兵奔北坡"
}
POST _analyze
{
  "analyzer": "simple",
  "text": "八百标兵奔北坡"
}
POST _analyze
{
  "analyzer": "whitespace",
  "text": "八百标兵奔北坡"
}

POST _analyze
{
  "analyzer": "ik_smart",
  "text": "八百标兵奔北坡"
}
POST _analyze
{
  "analyzer": "ik_max_word",
  "text": "八百标兵奔北坡"
}

POST _analyze
{
  "analyzer": "ik_smart",
  "text": "Hello World&端午节"
}

POST _analyze
{
  "analyzer": "ik_max_word",
  "text": "Hello World&端午节"
}

# 修改es的分词器
PUT test3
PUT test4
{
  "mappings": {
    "properties": {
      "title":{
        "type": "text",
        "analyzer": "ik_max_word"
      }
    }
  }
}
GET _cat/indices
PUT test3/_doc/1
{
  "title":"八百标兵奔北坡"
}
PUT test3/_doc/2
{
  "title":"炮兵并排北边跑"
}
PUT test3/_doc/3
{
  "title":"炮兵怕把标兵碰"
}
PUT test3/_doc/4
{
  "title":"标兵怕碰炮兵炮"
}
PUT test4/_doc/1
{
  "title":"八百标兵奔北坡"
}
PUT test4/_doc/2
{
  "title":"炮兵并排北边跑"
}
PUT test4/_doc/3
{
  "title":"炮兵怕把标兵碰"
}
PUT test4/_doc/4
{
  "title":"标兵怕碰炮兵炮"
}
GET test3/_search
{
  "query": {
    "match_all": {}
  }
}
GET test4/_search
{
  "query": {
    "match_all": {}
  }
}
GET test3/_search
{
  "query": {
    "match": {
      "title": "标兵"
    }
  }
}
GET test4/_search
{
  "query": {
    "match": {
      "title": "标兵"
    }
  }
}

# 向es导入示例数据
PUT /shakespeare
{
 "mappings": {
   "properties": {
    "speaker": {"type": "keyword"},
    "play_name": {"type": "keyword"},
    "line_id": {"type": "integer"},
    "speech_number": {"type": "integer"}
  }
 }
}
GET shakespeare/_count
GET bank/_count
PUT /logstash-2015.05.18
{
  "mappings": {
      "properties": {
        "geo": {
          "properties": {
            "coordinates": {
              "type": "geo_point"
            }
          }
        }
      }
    }
}

PUT /logstash-2015.05.19
{
  "mappings": {
      "properties": {
        "geo": {
          "properties": {
            "coordinates": {
              "type": "geo_point"
            }
          }
        }
    }
  }
}

PUT /logstash-2015.05.20
{
  "mappings": {
      "properties": {
        "geo": {
          "properties": {
            "coordinates": {
              "type": "geo_point"
            }
          }
        }
      }
  }
}
GET logstash-2015.05.18/_count
GET logstash-2015.05.19/_count
GET logstash-2015.05.19/_count
GET _cat/indices

# es聚合分析-pipeline
GET employees/_search
{
  "query": {
    "match_all": {}
  }
}
GET employees/_search
{
  "size": 0,
  "aggs": {
    "job_terms": {
      "terms": {
        "field": "job.keyword",
        "size": 10
      }
    }
  }
}
GET employees/_search
{
  "size": 0,
  "aggs": {
    "job_terms": {
      "terms": {
        "field": "job.keyword",
        "size": 10
      },
      "aggs": {
        "avg_salary": {
          "avg": {
            "field": "salary"
          }
        }
      }
    }
  }
}
GET employees/_search
{
  "size": 0,
  "aggs": {
    "job_terms": {
      "terms": {
        "field": "job.keyword",
        "size": 10
      },
      "aggs": {
        "avg_salary": {
          "avg": {
            "field": "salary"
          }
        }
      }
    },
    "min_salary_by_job":{
      "min_bucket": {
        "buckets_path":"job_terms>avg_salary"
      }
    }
  }
}
GET employees/_search
{
  "size": 0
  , "aggs": {
    "age": {
      "histogram": {
        "field": "age",
        "interval": 5
      }
    }
  }
}
GET employees/_search
{
  "size": 0
  , "aggs": {
    "age": {
      "histogram": {
        "field": "age",
        "interval": 5
      },
      "aggs": {
        "avg_salary": {
          "avg": {
            "field": "salary"
          }
        }
      }
    }
  }
}
GET employees/_search
{
  "size": 0
  , "aggs": {
    "age": {
      "histogram": {
        "field": "age",
        "interval": 5
      },
      "aggs": {
        "avg_salary": {
          "avg": {
            "field": "salary"
          }
        },
        "sum_avg_salary":{
          "cumulative_sum": {
            "buckets_path": "avg_salary"
          }
        }
      }
    }
  }
}





