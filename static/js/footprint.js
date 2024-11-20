////////////////////////////////////////////////////////////////////////////
// 我的足迹
// by:obaby
// https://oba.by
// https://github.com/obaby
// https://h4ck.org.cn
// 在页面加载完成后执行代码
////////////////////////////////////////////////////////////////////////////
function isValidLongitude(longitude) {
    return longitude >= -180 && longitude <= 180;
}

function isValidLatitude(latitude) {
    return latitude >= -90 && latitude <= 90;
}

// 或者使用一个函数来判断经纬度是否有效
function isValidCoordinate(longitude, latitude) {
    return isValidLongitude(longitude) && isValidLatitude(latitude);
}

async function getMyMapSettings() {
    try {
        const response = await fetch('/api/location/get-my-map-settings/');
        if (!response.ok) {
            // throw new Error('Network response was not ok ' + response.statusText);
            return null;
        }
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Fetch error:', error);
        return null;
    }
}

function xmlgetMapSetting() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/location/get-my-map-settings/', false); // 第三个参数为 false 表示同步请求
    xhr.send();

    if (xhr.status === 200) {
        const data = JSON.parse(xhr.responseText);
        console.log(data);
        return data;
    } else {
        console.error('Error:', xhr.statusText);
    }
    return null;
}


window.onload = function () {

    // 创建地图实例
    var map = new BMapGL.Map("map"); // "map"是地图容器的id

    var global_marker_image_url = "https://h4ck.org.cn/avatar/avatar_circle-256.png";
    var global_passed_marker_image_url = "https://h4ck.org.cn/avatar/avatar-2.png";
    var global_picture_url = "https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241119-085453.jpg";
    var global_marker_width = 26;
    var global_marker_height = 26;
    var global_blog_url = "https://oba.by/";
    var global_is_enable_3d = true;

    var global_map_zoom = 5;

    var point = new BMapGL.Point(103.8319522831, 36.0615585627); // 地图中心点坐标
    var scaleCtrl = new BMapGL.ScaleControl(); // 添加比例尺控件
    var zoomCtrl = new BMapGL.ZoomControl(); // 添加缩放控件
    var navi3DCtrl = new BMapGL.NavigationControl3D();  // 添加3D控件

    var cr = new BMapGL.CopyrightControl({
        anchor: BMAP_ANCHOR_TOP_LEFT,
        offset: new BMapGL.Size(20, 20)
    });   //设置版权控件位置

    var data = xmlgetMapSetting();
    if (data !== null) {
        console.log('Map settings:');
        console.log(data);
        var config_data = data.data;
        // 设置地图中心点
        if (config_data.map_setting != null) {
            if (config_data.map_setting.map_zoom !== null && config_data.map_setting.map_zoom > 0) {
                global_map_zoom = config_data.map_setting.map_zoom;
            }
            if (config_data.map_setting.center_latitude !== null
                && config_data.map_setting.center_longitude !== null
                && isValidCoordinate(config_data.map_setting.center_longitude, config_data.map_setting.center_latitude)) {
                point = new BMapGL.Point(config_data.map_setting.center_longitude, config_data.map_setting.center_latitude);
                // 设置地图中心点坐标
                map.centerAndZoom(point, global_map_zoom); // 设置地图中心和缩放级别

                map.addControl(cr); //添加版权控件
                var bs = map.getBounds();   //返回地图可视区域
                cr.addCopyright({
                    id: 1,
                    content: "<a target='_blank' href='https://h4ck.org.cn/' style='font-size:12px;color:#ff7aa4'>obaby@mars</a></br><img style='float:left;margin:0 4px 22px' alt='obaby@mars' src='https://h4ck.org.cn/img/logo_fox.png' width='50px' height='50px'/>",
                    bounds: bs
                });
            }
            // 设置地图样式
            if (config_data.map_setting.map_type === 1) {
                map.setMapType(BMAP_NORMAL_MAP);
            } else if (config_data.map_setting.map_type === 2) {
                map.setMapType(BMAP_EARTH_MAP);
            } else {
                map.setMapType(BMAP_SATELLITE_MAP);
            }
            if (config_data.map_setting.is_add_scaleCtrl === true) {
                map.addControl(scaleCtrl);
            }
            if (config_data.map_setting.is_enable_scroll_wheel_zoom === true) {
                map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
            }
            if (config_data.map_setting.is_add_control === true) {
                //添加缩放控件
                map.addControl(zoomCtrl);
            }
            if (config_data.map_setting.is_enable_3d === true){
                map.addControl(navi3DCtrl);
            }
        } else {
            // 设置地图中心点和缩放级别
            map.centerAndZoom(point, global_map_zoom); // 设置地图中心和缩放级别

            map.addControl(cr); //添加版权控件
            var bs = map.getBounds();   //返回地图可视区域
            cr.addCopyright({
                id: 1,
                content: "<a target='_blank' href='https://h4ck.org.cn/' style='font-size:12px;color:#ff7aa4'>obaby@mars</a></br><img style='float:left;margin:0 4px 22px' alt='obaby@mars' src='https://h4ck.org.cn/img/logo_fox.png' width='50px' height='50px'/>",
                bounds: bs
            });
            map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
            // 比例尺
            map.addControl(scaleCtrl);

            map.addControl(zoomCtrl);
            map.setMapType(BMAP_EARTH_MAP);
        }
        // 处理 marker image
        if (config_data.marker !== null) {
            if (config_data.marker.normal_image !== null && config_data.marker.normal_image !== '') {
                global_marker_image_url = config_data.marker.normal_image;
            }
            if (config_data.marker.passed_image !== null && config_data.marker.passed_image !== '') {
                global_passed_marker_image_url = config_data.marker.passed_image;
            }
            if (config_data.marker.place_holder_image_url !== null && config_data.marker.place_holder_image_url !== '') {
                global_picture_url = config_data.marker.place_holder_image_url;
            }
            if (config_data.marker.size_width !== null && config_data.marker.size_width > 0) {
                global_marker_width = config_data.marker.size_width;
            }
            if (config_data.marker.size_height !== null && config_data.marker.size_height > 0) {
                global_marker_height = config_data.marker.size_height;
            }
            if (config_data.marker.blog_url !== null && config_data.marker.blog_url !== '') {
                global_blog_url = config_data.marker.blog_url;
            }
        }

    } else {
        // 处理错误 如果接口失败，继续初始化数据
        // 设置地图中心点和缩放级别
        // var point = new BMapGL.Point(103.8319522831, 36.0615585627); // 设置地图中心点坐标
        map.centerAndZoom(point, 5); // 设置地图中心和缩放级别

        map.addControl(cr); //添加版权控件
        var bs = map.getBounds();   //返回地图可视区域
        cr.addCopyright({
            id: 1,
            content: "<a target='_blank' href='https://h4ck.org.cn/' style='font-size:12px;color:#ff7aa4'>obaby@mars</a></br><img style='float:left;margin:0 4px 22px' alt='obaby@mars' src='https://h4ck.org.cn/img/logo_fox.png' width='50px' height='50px'/>",
            bounds: bs
        });
        map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
        // var scaleCtrl = new BMapGL.ScaleControl(); // 添加比例尺控件
        map.addControl(scaleCtrl);
        // var zoomCtrl = new BMapGL.ZoomControl(); // 添加缩放控件
        map.addControl(zoomCtrl);
        console.error('Error:', error);
    }


    fetch('/api/location/get-my-location-list/')
        .then(response => {
            if (!response.ok) {
                throw new Error('HTTP error ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log('Locations:');
            console.log(data);
            // 处理返回的 JSON 数据
            var locations = data.data;
            console.log(locations);
            for (var i = 0; i < locations.length; i++) {
                // 创建闭包来保存城市名称和文本信息
                (function () {
                    var location = locations[i];
                    var city = locations[i].name;
                    // var text = "\r\n <a target='_blank' href='" + "https://h4ck.org.cn/?s=" + locations[i].text + "'>  https://h4ck.org.cn/?s=" + locations[i].text + "</a>";
                    var mark = locations[i].mark;
                    var note = '这家伙很懒哦，感觉什么都不想写，也不想告诉你呢';
                    if (location.note != null && location.note !== '') {
                        note = location.note;
                    }
                    var picture_url = global_picture_url;
                    if (location.picture_url != null && location.picture_url !== '') {
                        picture_url = location.picture_url;
                    }
                    var post_url = global_blog_url;
                    if (location.post_url != null && location.post_url !== '') {
                        post_url = location.post_url;
                    }
                    var marker_image = global_marker_image_url;
                    if (location.is_passed) {
                        marker_image = global_passed_marker_image_url;
                    }
                    if (location.marker_image != null && location.marker_image !== '') {
                        marker_image = location.marker_image;
                    }
                    var myIcon = new BMapGL.Icon(marker_image, new BMapGL.Size(global_marker_width, global_marker_height));


                    var sContent = `<h4 style='margin:0 0 5px 0;color: #ff7aa4'>` + city + `(` + mark + `)` + `</h4>
   <a target='_blank' href='` + picture_url + `'> <img alt='打卡照片' style='float:right;margin:0 4px 22px' id='imgDemo' src='` + picture_url + `' width='139' height='104'/> </a>
    <p style='margin:0;line-height:1.5;font-size:13px;text-indent:2em'>` + note + `</p>
    <hr><p style='margin:0;line-height:1.5;font-size:12px;text-indent:0em'>相关文章：<a target='_blank' href='` + post_url + `'>` + post_url + `</a></p>
    </div>`;
                    var infoWindow = new BMapGL.InfoWindow(sContent);
                    // var opts = {
                    //     width: 200,
                    //     // 信息窗口宽度
                    //     height: 80,
                    //     // 信息窗口高度
                    //     title: city + "(" + mark + ")",
                    //     // 信息窗口标题
                    //     message: text
                    // }
                    // var infoWindow = new BMapGL.InfoWindow("相关文章：" + text, opts); // 创建信息窗口对象

                    if (location.latitude !== null && location.lontitude !== null && isValidCoordinate(location.lontitude, location.latitude)) {
                        var point = new BMapGL.Point(location.lontitude, location.latitude);
                        // 创建Marker标注，使用小车图标
                        // var pt = new BMapGL.Point(116.417, 39.909);
                        var marker = new BMapGL.Marker(point, {
                            icon: myIcon
                        });
                        //   var marker = new BMap.Marker(point);
                        //   marker.color = "pink";
                        map.addOverlay(marker);


                        // 绑定点击事件
                        marker.addEventListener("click",
                            function () {
                                this.openInfoWindow(infoWindow);
                            });
                    } else {
                        // 使用地理编码将城市名称转换为经纬度
                        var geoc = new BMapGL.Geocoder();
                        geoc.getPoint(city,
                            function (point) {
                                if (point) {
                                    // 添加标注
                                    // 创建Marker标注，使用图标
                                    // var pt = new BMapGL.Point(116.417, 39.909);
                                    var marker = new BMapGL.Marker(point, {
                                        icon: myIcon
                                    });
                                    //   var marker = new BMap.Marker(point);
                                    //   marker.color = "pink";
                                    map.addOverlay(marker);
                                    // 绑定点击事件
                                    marker.addEventListener("click",
                                        function () {
                                            this.openInfoWindow(infoWindow);
                                        });
                                } else {
                                    console.log("decode failed");
                                }
                            },
                            city);
                    }


                })();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    // 定义城市名称和文本信息数组

};