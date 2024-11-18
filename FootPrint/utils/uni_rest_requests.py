import datetime
import json
import random
import string
import requests
import asyncio
import traceback
import time

from reminder.utils.string_util import random_str
from reminder.utils.uni_sign import Sign as UniSign

requestAuthSecret = 'DayimarequestAuthSecr3t'
sign = UniSign(requestAuthSecret)

# https://doc.dcloud.net.cn/uniCloud/uni-id/cloud-object.html#external-register
'''
uni-id-nonce	string	是	随机字符串
uni-id-timestamp	string	是	当前时间戳; 单位毫秒
uni-id-signature	string	是	请求鉴权签名; 签名算法见下
POST /your-uni-id-co-path/externalRegister HTTP/1.1
Host: xxx.com
uni-id-nonce: xxxxxxx
uni-id-timestamp: 1676882808550
uni-id-signature: 11c965267a4a02c6978949c7135215b0a75aea22b2b84ed491e792365c8269efa
Content-Type: application/json
Cache-Control: no-cache

{"externalUid": "test externalUid", "nickname": "张三", "avatar": "xxxxxxx", "gender": 0}
externalUid	string	是	自身系统的用户id，必须保证唯一性。
nickname	string	否	用户昵称
avatar	string	否	用户头像
gender	number	否	用户性别；0 未知 1 男性 2 女性
'''


def external_register(external_uid, nickname, avatar, gender):
    body = {
        'externalUid': str(external_uid),
        'nickname': nickname,
        # 'avatar':'',
        # 'gender':''
    }
    timestamp = int(round(time.time() * 1000))
    nonce = random_str(16)
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'uni-id-nonce': nonce,
        'uni-id-timestamp': str(timestamp),
        'uni-id-signature': sign.get_signature(body, nonce, timestamp)
    }
    print(body)

    req_body = {
        "clientInfo": {'uniPlatform': 'app',
                       'appId': '__UNI__E8AEFF9'},
        "params": body
    }

    resp = requests.post("https://cf.h4ck.org.cn/uni-id-co/externalRegister", json=req_body, headers=headers)
    print('Reg Resp:', resp.text)
    return resp.text


'''
参数名	类型	必填	说明
uid	string	否	uni-id体系的用户Id；与externalUid 二选一
externalUid	string	否	自身系统的用户id；与 uid 二选一
'''


def external_login(uid, external_uid):
    body = {
        # 'uid':str(uid),
        'externalUid': str(external_uid),
        # 'nickname': nickname,
        # 'avatar':'',
        # 'gender':''
    }
    timestamp = int(round(time.time() * 1000))
    nonce = random_str(16)
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'uni-id-nonce': nonce,
        'uni-id-timestamp': str(timestamp),
        'uni-id-signature': sign.get_signature(body, nonce, timestamp)
    }
    print(body)

    req_body = {
        "clientInfo": {'uniPlatform': 'app',
                       'appId': '__UNI__E8AEFF9'},
        "params": body
    }

    resp = requests.post("https://cf.h4ck.org.cn/uni-id-co/externalLogin", json=req_body, headers=headers)
    print('Reg Resp:', resp.text)
    return resp.text


'''
uid	string	否	uni-id体系的用户Id；与externalUid 二选一
externalUid	string	否	自身系统的用户id；与 uid 二选一
username	string	否	用户名
password	string	否	密码
nickname	string	否	昵称
authorizedApp	Array<string>	否	允许登录的app列表
role	Array<string>	否	用户角色
mobile	string	否	手机号
email	string	否	邮箱
tags	array	否	用户标签
status	number	否	用户状态，参考：用户状态
avatar	string	否	用户头像
gender	number	否	用户性别；0 未知 1 男性 2 女性
'''
def external_update(uid, external_uid, username, password, nickname, mobile, email, status,
                    avatar, gender):
    body = {
        # 'uid':str(uid),
        'externalUid': str(external_uid),
        # # 'nickname': nickname,
        # # 'avatar':'',
        # # 'gender':''
        # 'username': username,
        # 'password': password,
        # 'nickname': nickname,
        # # 'authorizedApp': authorizedApp,
        # # 'role': role,
        # 'mobile': mobile,
        # 'email': email,
        # # 'tags': tags,
        # 'status': status,
        # 'avatar': avatar,
        # 'gender': gender,
    }
    if username and username != '':
        body['username'] = username
    if nickname and nickname != '':
        body['nickname'] = nickname
    if password and password != '':
        body['password'] = password
    if mobile and mobile != '':
        body['mobile'] = mobile
    if email and email != '':
        body['email'] = email
    if status and status != '':
        body['status'] = status
    if avatar and avatar != '':
        body['avatar'] = avatar
    if gender and gender != '':
        body['gender'] = gender

    timestamp = int(round(time.time() * 1000))
    nonce = random_str(16)
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'uni-id-nonce': nonce,
        'uni-id-timestamp': str(timestamp),
        'uni-id-signature': sign.get_signature(body, nonce, timestamp)
    }
    print(body)

    req_body = {
        "clientInfo": {'uniPlatform': 'app',
                       'appId': '__UNI__E8AEFF9'},
        "params": body
    }

    resp = requests.post("https://cf.h4ck.org.cn/uni-id-co/updateUserInfoByExternal", json=req_body, headers=headers)
    print('Reg Resp:', resp.text)
    return resp.text

# 注册，如果已经注册登录 获取 uid
def get_user_uni_id_and_token(uid, nickname, avatar, gender):
    reg_resp = external_register(uid,nickname,avatar,gender)
    reg_json = json.loads(reg_resp)
    if reg_json['errCode'] != 0:
        login_resp = external_login('',uid)
        login_json = json.loads(login_resp)
        if login_json['errCode'] != 0:
            # print('Login error')
            return None,None
        else:
            token = login_json['newToken']['token']
            uid = login_json['uid']
            # print(token)
            # print(uid)
            return token, uid

    return None, None

# 登录获取 token 如果没有账号创建
def uni_login(uid):
    login_resp = external_login('', uid)
    login_json = json.loads(login_resp)
    if login_json['errCode'] != 0:
        # print('Login error')
        reg_resp = external_register(uid, '', '', '')
        reg_json = json.loads(reg_resp)
        if reg_json['errCode'] != 0:
            print('register Failed')
            return None, None
        else:
            login_resp = external_login('', uid)
            login_json = json.loads(login_resp)
            if login_json['errCode'] != 0:
                return None, None
            else:
                token = login_json['newToken']['token']
                uid = login_json['uid']
                # print(token)
                # print(uid)
                return token, uid

    else:
        token = login_json['newToken']['token']
        uid = login_json['uid']
        # print(token)
        # print(uid)
        return token, uid

if __name__ == "__main__":
    print('uni rest request')
    # external_register('17', 'test', '', '')
    # external_login('', '17')
    # external_update('', '17','test','','','','','','', '')
    get_user_uni_id_and_token('17', '', '', '')

