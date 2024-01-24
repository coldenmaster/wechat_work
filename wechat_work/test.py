
# import frappe

# from wechatpy.enterprise import WeChatClient
# from wechatpy.session.redisstorage import RedisStorage
# from redis import Redis


# # endpoint: http://127.0.0.1:8000/api/method/wechat_work.api.send
# @frappe.whitelist(allow_guest=True)
# def send(*args,**kwargs):
#     """
#     此部分进行发送测试
#     1.获取数据库中agent信息
#     2.构造wechat client
#     3.构造message
#     4.发送
#     """
#     print('----------')
#     print(kwargs)

#     agentDoc = frappe.get_doc('Wechat Agent',kwargs.get('agent_name'))
#     corpDoc = frappe.get_doc('Wechat Company', agentDoc.company)
#     corpId = corpDoc.company
#     agentId = agentDoc.agent_id
#     secret = agentDoc.secret
#     print(vars(agentDoc))

#     client = WeChatClient(
#         corpId,
#         secret,
#         # session = session_interface 
#     )
#     print(client.access_token)

#     return 'wechat_work.api.send'