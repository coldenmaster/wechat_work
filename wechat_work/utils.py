# -*- coding: utf-8 -*-

# sys.path.append(str(Path(__file__).resolve().parents[2])) 
from wechatpy.enterprise import WeChatClient
from wechatpy.session.redisstorage import RedisStorage

import frappe

def get_corp_agent_secret(app_name):
    c, a, s = frappe.db.get_value("Wechat Agent", app_name, ["company", "agent_id", "secret"])
    c = frappe.get_doc("Wechat Corp", c).corp_id
    return c, a, s

def get_client(corp_id, secret):
    return WeChatClient(
        corp_id,
        secret,
        session = RedisStorage(frappe.cache())
    )

def send_str_to_admin(msg):
    send_str_to_wework(msg)

def send_str_to_wework(msg, app_name='TEST_APP',  user_ids='wangtao',
                  party_ids='', tag_ids='', safe=0):
    # print(f"app_name: {app_name}")
    try:
        corp_id, agent_id, secret = get_corp_agent_secret(app_name)
        client = get_client(corp_id, secret)
        client.message.send_text(agent_id, user_ids, msg, party_ids, tag_ids, safe)
    except Exception as e:
        frappe.log_error("send_str_to_wework except")
        # frappe.get_traceback(True)
        
    






