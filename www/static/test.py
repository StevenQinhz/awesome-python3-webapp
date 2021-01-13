#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试'

__author__ = 'BWone'

import asyncio
import ORM as orm
from model import User, Comment

loop = asyncio.get_event_loop()
async def test():
	# 数据库参数@
    await orm.create_pool(user='root', password='root', db='test', loop=loop)
    # 传入事件循环
    await orm.create_pool(loop=loop)

    # 新增：当我们创建类时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类
    u = User(s_username='test', s_pwd='test', s_gender=1, s_age=11)
    u.save()

    # 查询
    u = User()
    # 条件查询
    find1 =await u.findAll("s_username='test'")
    print(find1)
    # 多个关键字查询：两种方式
    # find2 = await u.findAll("s_username='test' order by id desc limit 2")
    # find3 = await u.findAll("s_username='test'", None, orderBy='id desc', limit=2)
    # 数据数量查询
    # find4 = await u.findNumber('count(*)')
    # 求和查询：需要去掉_num_
    # find5 = await u.findNumber('sum(s_age) age')
    # 主键查询：find方法通过cls.__primary_key__获取，调用时只传入参数即可
    # find6 = await u.find(1)
    # print(find2)

    # 更新
    # u = User(id=4, s_username='testUpdate', s_pwd='123', s_gender=0, s_age=0)
    # update1 = await u.update()

    # 删除
    # u = User(id=15)
    # remove1 = await u.remove()


loop.run_until_complete(test())