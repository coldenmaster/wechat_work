
import frappe
import json
import logging
from wechat_work.utils import get_client

from wechatpy.enterprise import WeChatClient
# from wechatpy.session.redisstorage import RedisStorage


# endpoint: http://127.0.0.1:8000/api/method/wechat_work.api.send
@frappe.whitelist(allow_guest=True)
def send(*args,**kwargs):
    """
    此部分进行发送测试
    """

    frappe.publish_realtime(event='msgprint', message='Popup Msg As Test', user=frappe.session.user,doctype='Wechat Send Test')

    send2(**kwargs)

    return 'wechat_work.api.send'

def send2(**kwargs):
    """
    此部分进行发送测试
    1.获取数据库中agent信息
    2.构造wechat client
    3.构造message
    4.发送
    """
    print('----------')
    # print(kwargs)

    try:
        update_doc_dict = json.loads(kwargs.get('doc'))
        agent_doc = frappe.get_doc('Wechat Agent', update_doc_dict.get('agent_name'))
        corp_doc = frappe.get_doc('Wechat Corp', agent_doc.company)
        corpId = corp_doc.corp_id
        print(f'agent: { update_doc_dict.get("agent_name") }')
        agentId = agent_doc.agent_id
        secret = agent_doc.secret

        client = get_client(corpId, secret)
        print(client.access_token_key)
        print(f'access_token: { client.access_token }')

        user_ids = to_list(update_doc_dict.get('user_id'))
        party_ids = to_list(update_doc_dict.get('department'))
        tag_ids = to_list(update_doc_dict.get('tag'))

        content = update_doc_dict.get('content').replace('&gt;', '>')
        message_type = update_doc_dict.get('message_type')
        if message_type == 'Text':
            client.message.send_text(
                agentId, user_ids, content=content, party_ids=party_ids, tag_ids=tag_ids
                )
        elif message_type == 'Markdown':
            client.message.send_markdown(
                agentId, user_ids, content=content, party_ids=party_ids, tag_ids=tag_ids
                )
        elif message_type == 'Text Card':
            client.message.send_text(
                agentId, user_ids, content=content, party_ids=party_ids, tag_ids=tag_ids
                )
        else:
            client.message.send_text(agentId, "wangtao", content=content)


    except Exception as e:
        logging.exception(e)
    
    print('=== end ===')

def to_list(data):
   if not isinstance(data, str):
       data = ''
   return data.split(',')

