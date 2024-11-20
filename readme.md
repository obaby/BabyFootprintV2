# Baby 足迹地图  


## 简介：  
基于百度地图的足迹地图。

## 功能(marker以及地图配置可以创建多条，默认生效为最后一条配置信息)  
* 支持后台添加位置信息
* 支持添加带gps坐标的位置信息  
* 支持全局自定义marker图标  
* 支持配置地图模式，# 1.标准地图：BMAP_NORMAL_MAP# 2.地球模式：BMAP_EARTH_MAP# 3.普通卫星地图：BMAP_SATELLITE_MAP
* 支持单个 marker 设置图标
* 支持全局设置弹窗默认图片
* 支持全局设置默认博客链接
* 支持设置地图中心点坐标


## 安装运行：  
python 3.8 - 3.10   
  
`pip install -r requirements.pip`  

## 启动服务 建议使用nginx反代：  
` python3 manage.py runserver 0.0.0.0:10086`  

  
### 后台登录地址：  
http://127.0.0.1:10086/admin/  


登录账号：obaby  
默认密码：123456   


## 修改：
前端页面修改js，static/js/footprint.js 编辑以下代码替换默认图标：  

```
var location = locations[i];
var city = locations[i].name;
var text = "\r\n <a target='_blank' href='" + "https://h4ck.org.cn/?s=" + locations[i].text + "'>  https://h4ck.org.cn/?s=" + locations[i].text + "</a>";
var mark = locations[i].mark;
var marker_image = "https://h4ck.org.cn/avatar/avatar_circle-256.png";
if (location.is_passed ){
    marker_image = "https://h4ck.org.cn/avatar/avatar-2.png";
}
```  
* marker_image 默认图标  
* https://h4ck.org.cn/avatar/avatar-2.png 经停点图标
* https://h4ck.org.cn/?s= 弹出卡片搜索地址以及链接地址  

## 截图：  

### 后台首页： 
![admin](screenshots/admin.png)  

### 添加地点：
![add](screenshots/add.png)  

**（如果不带gps坐标或者坐标无效，将会通过百度地图api解析gps坐标）**

### 列表：  
![list](screenshots/list.png)

### 首页：
![首页](screenshots/home.png)  


## 扩展内容 nginx反代： 

```
server
    {
        listen 443 ssl http2;
        #listen [::]:443 ssl http2;
        server_name footprint.h4ck.org.cn ;
        index index.html index.htm index.php default.html default.htm default.php;
        root  /home/wwwroot/footprint.h4ck.org.cn;

        ssl_certificate /home/lighthouse/footprint.h4ck.org.cn_nginx/footprint.h4ck.org.cn_bundle.pem;
        ssl_certificate_key /home/lighthouse/footprint.h4ck.org.cn_nginx/footprint.h4ck.org.cn.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
        ssl_ciphers "TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-128-CCM-8-SHA256:TLS13-AES-128-CCM-SHA256:EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5";
        ssl_session_cache builtin:1000 shared:SSL:10m;
        # openssl dhparam -out /usr/local/nginx/conf/ssl/dhparam.pem 2048
        ssl_dhparam /usr/local/nginx/conf/ssl/dhparam.pem;

        include rewrite/none.conf;
        #error_page   404   /404.html;

        # Deny access to PHP files in specific directory
        #location ~ /(wp-content|uploads|wp-includes|images)/.*\.php$ { deny all; }
location /static/ {
       alias    /home/wwwroot/babyfootprint/static/;
}

location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;

        proxy_pass http://127.0.0.1:10086;
        proxy_http_version 1.1;
proxy_set_header Accept-Encoding "";
}
        access_log  /home/wwwlogs/footprint.h4ck.org.cn.log;
    }
                    
```

预览地址：  

<a href="https://footprint.h4ck.org.cn" target="_blank">https://footprint.h4ck.org.cn</a>

博客地址：  
<a href="https://h4ck.org.cn" target="_blank">https://h4ck.org.cn</a>


 