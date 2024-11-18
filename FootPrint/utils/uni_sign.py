import hmac
import hashlib
import time

# https://doc.dcloud.net.cn/uniCloud/uni-id/cloud-object.html#http-reqeust-auth
class Sign:
    def __init__(self, requestAuthSecret):
        self.requestAuthSecret = requestAuthSecret

    def get_signature(self, params, nonce, timestamp):
        params_str = self.get_params_string(params)
        signature = hmac.new(bytes("%s%s" % (self.requestAuthSecret, nonce), 'utf-8'),
                             bytes("%s%s" % (timestamp, params_str), 'utf-8'),
                             digestmod=hashlib.sha256).hexdigest().upper()

        return signature

    def get_params_string(self, params):
        params_str = []
        for k in sorted(params):
            if isinstance(params[k], (list, dict)):
                continue
            params_str.append("%s=%s" % (k, params[k]))

        return "&".join(params_str)


if __name__ == "__main__":
    requestAuthSecret = "testSecret"
    nonce = "xxxxxxx"
    timestamp = int(round(time.time() * 1000))

    params = {
        "foo": 1,
        "bar": 2,
        "foobar": 4,
        "foo_bar": 3,
    }

    sign = Sign(requestAuthSecret)
    signature = sign.get_signature(params, nonce, timestamp)

    print(nonce, timestamp, signature)
