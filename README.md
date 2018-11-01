# vjudge-rank-crawler
一个爬取、自动统计vjudge单场比赛数据的爬虫。

## 开发者
zhaoyw1999(Yuwei Zhao)。

## 用法
+ 首先需要将`origin.json`放在`get_user_id`同目录下，格式如下[已经有`acmer.json`请忽略次步骤]
```json
[
    {
        "order_id": "1", 
        "student_id": "xxx", 
        "student_name": "xxx", 
        "vjudge_account": "xxx", 
        "group": "提高组"
    }, 
    {
        "order_id": "2", 
        "student_id": "xxx", 
        "student_name": "xxx", 
        "vjudge_account": "xxx", 
        "group": "提高组"
    }, 
]
```
+ 然后运行`get_user_id.py`生成`acmer.json`[已经有`acmer.json`请忽略次步骤]
+ 将`acmer.json`放在`main.py`同目录下，格式如下
```json
[
    {
        "order_id": "1", 
        "student_id": "xxx", 
        "student_name": "xxx", 
        "vjudge_account": "xxx", 
        "group": "提高组", 
        "vjudge_id": "xxx"
    }, 
    {
        "order_id": "2", 
        "student_id": "xxx", 
        "student_name": "xxx", 
        "vjudge_account": "xxx", 
        "group": "普及组", 
        "vjudge_id": "xxx"
    }
]
```
+ 运行`main.py`，按照提示操作即可，最终生成的txt可贴入excel表格，json保存为日后统计使用
