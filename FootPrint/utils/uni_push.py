import datetime
import random
import string
import requests
import asyncio
import traceback


def print_stack():
    # 获取当前的函数调用堆栈信息
    stack = traceback.format_stack()

    # 遍历每行堆栈信息并打印
    for line in stack:
        print(line)


def generate_random_string(length):
    letters = string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def gen_request_id():
    rid = str(datetime.datetime.now().timestamp()).replace('.', '') + generate_random_string(10)

    return rid


def send_push_request(cids, title, content, data, request_id, options):
    '''
    const uniPush = uniCloud.getPushManager({appId:"__UNI__XXXXXX"}) //注意这里需要传入你的应用appId
    exports.main = async (event, context) => {
        return await uniPush.sendMessage({
            "push_clientid": "xxx",     //填写上一步在uni-app客户端获取到的客户端推送标识push_clientid
            "force_notification":true,  //填写true，客户端就会对在线消息自动创建“通知栏消息”。
            "title": "通知栏显示的标题",
            "content": "通知栏显示的内容",
            "payload": {
                "text":"体验一下uni-push2.0"
            },
            "options":{
                "HW": {
                     // 值为int 类型。1 表示华为测试消息，华为每个应用每日可发送该测试消息500条。此 target_user_type 参数请勿发布至线上。
                      "/message/android/target_user_type":1
                  } ,
                "VV": {
                     //值为int 类型。0 表示正式推送；1 表示测试推送，不填默认为0。此 pushMode 参数请勿发布至线上。
                      "/pushMode":1
                  }
            }
        })
    };'''
    body = {
        "cids": cids,  # 设备id，支持多个以数组的形式指定多个设备，如["cid-1","cid-2"]，数组长度不大于1000
        "title": title,  # 标题
        "content": content,  # 内容
        "data": data,  # 数据
        "force_notification": True,  # 服务端推送 需要加这一句
        "request_id": request_id,  # 请求唯一标识号，10-32位之间；如果request_id重复，会导致消息丢失
        "options": options  # 消息分类，没申请可以不传这个参数
    }
    print(body)

    resp = requests.post("https://cf.h4ck.org.cn/babyUniPush", json=body)
    print('Push Resp:', resp.text)


def baby_send_push_message(cids, uid, mtype, title, content, request_id):
    options = {
        "HW": {
            "message.android.category": "HEALTH",
            "/message/android/target_user_type": 1
        }}
    data = {
        # "test": "123",
        "id": int(uid),
        "message": str(content),
        "type": mtype
    }
    send_push_request(cids, title, content, data, request_id, options)


if __name__ == "__main__":
    print(gen_request_id())
    # https://ask.dcloud.net.cn/article/40283
    # print(len('1708311188800778021900491'))

    opt = {
        "HW": {
            "/message/android/category": "DEVICE_REMINDER",
            "/message/android/target_user_type": 1
        }}
    data = {
        "test": "123",
        "id": 1,
        "message": " test message",
        "type": 0
    }
    # 554116722a512d32a84270285ab2f261 ios
    # 2e45d3dba35d3816a34e799bbe822f20 h5
    # baby_send_push_message(['827dd4df98c4bf976e502862cd2c20d4'], 1,1,'标题', '测试内容', gen_request_id())
    # ios 模拟器
    # baby_send_push_message(['554116722a512d32a84270285ab2f261'], 1,1,'标题', '测试内容', gen_request_id())
    # iphone
    baby_send_push_message(['554116722a512d32a84270285ab2f261'], 1,2,'标题', 'guimi', gen_request_id())
