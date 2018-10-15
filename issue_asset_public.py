#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""发行资产."""
from stellar_base.asset import Asset
from stellar_base.builder import Builder
from stellar_base.keypair import Keypair

# 发行(issue)账号
issue_secret = ''
issue_public = 'GC55P5MTVPOPPY7NBBS5RPRUF5K3667ZQ2GN4J5GGE6AZVLPC72S5K46'
# 分配(distribute)账号
distribute_secret = ''
distribute_public = 'GD7C4MQJDM3AHXKO2Z2OF7BK3FYL6QMNBGVEO4H2DHM65B7JMHD2IU2E'

# print 'issue_public     : %s' % issue_public
# print 'distribute_public: %s' % distribute_public

# 资产的表示
my_asset = Asset('MFN', issue_public)

# 创建一个从分配账号到发行账号的trustline.
builder = Builder(distribute_secret, network='PUBLIC').append_trust_op(destination=my_asset.issuer, code=my_asset.code, limit=10000000000)
builder.sign()
# 向Horizon发送交易, 返回一个dict表示JSON格式的回复.
resp = builder.submit()
print(resp)
print '-----------------------------------------------------------------'

# 发行账号用新建的资产向分配账号支付(即转账).
builder = Builder(issue_secret, network='PUBLIC').append_payment_op(
        destination=distribute_public,
        amount=10000000000,            # 可以是字符串, 也可以是整数或者浮点类型.
        asset_type=my_asset.code,      # 新版API的参数不是'asset_code'
        asset_issuer=my_asset.issuer)
builder.sign()
resp = builder.submit()
print(resp)


# vim: et sta sw=4 sts=4
