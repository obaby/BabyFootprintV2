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


window.onload = function () {

    // 创建地图实例
    var map = new BMapGL.Map("map"); // "map"是地图容器的id
    // 设置地图中心点和缩放级别
    var point = new BMapGL.Point(103.8319522831, 36.0615585627); // 设置地图中心点坐标
    map.centerAndZoom(point, 5); // 设置地图中心和缩放级别
    map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
    var scaleCtrl = new BMapGL.ScaleControl(); // 添加比例尺控件
    map.addControl(scaleCtrl);
    var zoomCtrl = new BMapGL.ZoomControl(); // 添加缩放控件
    map.addControl(zoomCtrl);


    fetch('/api/location/get-my-location-list/')
        .then(response => {
            if (!response.ok) {
                throw new Error('HTTP error ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            // 处理返回的 JSON 数据
            var locations = data.data;
            console.log(locations);
            for (var i = 0; i < locations.length; i++) {
                // 创建闭包来保存城市名称和文本信息
                (function () {
                    var location = locations[i];
                    var city = locations[i].name;
                    var text = "\r\n <a target='_blank' href='" + "https://h4ck.org.cn/?s=" + locations[i].text + "'>  https://h4ck.org.cn/?s=" + locations[i].text + "</a>";
                    var mark = locations[i].mark;
                    var note = '这家伙很懒哦，感觉什么都不想写，也不想告诉你呢';
                    if (location.note != null && location.note !== '') {
                        note = location.note;
                    }
                    var picture_url = 'https://h4ck.org.cn/wp-content/uploads/2024/11/Jietu20241119-085453.jpg';
                    if (location.picture_url != null && location.picture_url !== '') {
                        picture_url = location.picture_url;
                    }
                    var post_url = 'https://oba.by';
                    if (location.post_url != null && location.post_url !== '') {
                        post_url = location.post_url;
                    }
                    var marker_image = "https://h4ck.org.cn/avatar/avatar_circle-256.png";
                    if (location.is_passed) {
                        marker_image = "https://h4ck.org.cn/avatar/avatar-2.png";
                    }
                    if (location.marker_image != null && location.marker_image !== '') {
                        marker_image = location.marker_image;
                    }
                    var myIcon = new BMapGL.Icon(marker_image, new BMapGL.Size(26, 26));


                    var sContent = `<h4 style='margin:0 0 5px 0;'>`+ city + `(` + mark + `)`+`</h4>
   <a target='_blank' href='`+picture_url+`'> <img alt='打卡照片' style='float:right;margin:0 4px 22px' id='imgDemo' src='`+picture_url+`' width='139' height='104'/> </a>
    <p style='margin:0;line-height:1.5;font-size:13px;text-indent:2em'>` +note+`</p>
    <p style='margin:0;line-height:1.5;font-size:13px;text-indent:0em'>相关文章：<a target='_blank' href='`+post_url+`'>`+post_url + `</a></p>
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