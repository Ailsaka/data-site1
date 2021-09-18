(function() {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".map .chart"));
  // 2. 指定配置和数据
  // 2. 指定配置和数据
  var geoCoordMap = {
    上海: [121.4648, 31.2891],
    东莞: [113.8953, 22.901],
    东营: [118.7073, 37.5513],
    中山: [113.4229, 22.478],
    临汾: [111.4783, 36.1615],
    临沂: [118.3118, 35.2936],
    丹东: [124.541, 40.4242],
    丽水: [119.5642, 28.1854],
    乌鲁木齐: [87.9236, 43.5883],
    喀什: [74.9236, 39.5883],
    佛山: [112.8955, 23.1097],
    保定: [115.0488, 39.0948],
    兰州: [103.5901, 36.3043],
    包头: [110.3467, 41.4899],
    北京: [116.4551, 40.2539],
    北海: [109.314, 21.6211],
    南京: [118.8062, 31.9208],
    芜湖: [118.5062, 31.0208],
    南宁: [109.979, 23.4152],
    南昌: [116.0046, 28.6633],
    向塘: [116.0045, 28.6631],
    樟树: [115.5046, 27.6633],
    南通: [121.1023, 32.1625],
    厦门: [118.1689, 24.6478],
    台州: [121.1353, 28.6688],
    合肥: [117.29, 32.0581],
    呼和浩特: [111.4124, 40.4901],
    咸阳: [108.4131, 34.8706],
    哈尔滨: [127.9688, 45.368],
    唐山: [118.4766, 39.6826],
    嘉兴: [120.9155, 30.6354],
    大同: [113.7854, 39.8035],
    大连: [122.2229, 39.4409],
    天津: [117.4219, 39.4189],
    杨村: [117.0000, 39.2222],
    廊坊: [116.521, 39.0509],
    太原: [112.3352, 37.9413],
    威海: [121.9482, 37.1393],
    宁波: [121.5967, 29.6466],
    宝鸡: [107.1826, 34.3433],
    宿迁: [118.5535, 33.7775],
    常州: [119.4543, 31.5582],
    广州: [113.5107, 23.2196],
    湛江: [110.1107, 21.0996],
    延安: [109.1052, 36.4252],
    张家口: [115.1477, 40.8527],
    徐州: [117.5208, 34.3268],
    德州: [116.6858, 37.2107],
    惠州: [114.6204, 23.1647],
    成都: [103.9526, 30.7617],
    扬州: [119.4653, 32.8162],
    承德: [117.5757, 41.4075],
    赤峰: [118.6757, 42.8075],
    拉萨: [90.1865, 30.1465],
    日喀则: [88.1865, 28.9995],
    无锡: [120.3442, 31.5527],
    日照: [119.2786, 35.5023],
    昆明: [102.9199, 25.4663],
    陆良: [103.9199, 25.4663],
    杭州: [119.5313, 29.8773],
    笕桥: [119.5313, 29.9993],
    枣庄: [117.323, 34.8926],
    柳州: [108.3799, 24.1774],
    桂林: [109.9799, 25.0774],
    南宁: [106.3799, 22.9774],
    株洲: [113.5327, 27.0319],
    武汉: [114.3896, 30.6628],
    汕头: [117.1692, 23.3405],
    江门: [112.6318, 22.1484],
    沈阳: [123.1238, 42.1216],
    沧州: [116.8286, 38.2104],
    河源: [114.917, 23.9722],
    泉州: [118.3228, 25.1147],
    泰安: [117.0264, 36.0516],
    泰州: [120.0586, 32.5525],
    济南: [117.1582, 36.8701],
    济宁: [116.8286, 35.3375],
    海口: [110.3893, 19.8516],
    淄博: [118.0371, 36.6064],
    淮安: [118.927, 33.4039],
    深圳: [114.5435, 22.5439],
    清远: [112.9175, 24.3292],
    温州: [120.498, 27.8119],
    渭南: [109.7864, 35.0299],
    湖州: [119.8608, 30.7782],
    湘潭: [112.5439, 27.7075],
    滨州: [117.8174, 37.4963],
    潍坊: [119.0918, 36.524],
    烟台: [120.7397, 37.5128],
    玉溪: [101.9312, 23.8898],
    珠海: [113.7305, 22.1155],
    盐城: [120.2234, 33.5577],
    盘锦: [121.9482, 41.0449],
    石家庄: [114.4995, 38.1006],
    福州: [119.4543, 25.9222],
    霞浦: [120.2543, 26.9222],
    连城: [117.4543, 25.9222],
    秦皇岛: [119.2126, 40.0232],
    绍兴: [120.564, 29.7565],
    聊城: [115.9167, 36.4032],
    肇庆: [112.1265, 23.5822],
    舟山: [122.2559, 30.2234],
    苏州: [120.6519, 31.3989],
    莱芜: [117.6526, 36.2714],
    菏泽: [115.6201, 35.2057],
    营口: [122.4316, 40.4297],
    葫芦岛: [120.1575, 40.578],
    衡水: [115.8838, 37.7161],
    衢州: [118.6853, 28.8666],
    西宁: [101.4038, 36.8207],
    西安: [109.1162, 34.2004],
    武功: [108.5162, 34.1904],
    临潼: [110.1162, 35.4004],
    贵阳: [106.6992, 26.7682],
    连云港: [119.1248, 34.552],
    邢台: [114.8071, 37.2821],
    邯郸: [114.4775, 36.535],
    郑州: [113.4668, 34.6234],
    鄂尔多斯: [108.9734, 39.2487],
    重庆: [107.7539, 30.1904],
    金华: [120.0037, 29.1028],
    铜川: [109.0393, 35.1947],
    鼎新: [99.3586, 40.1775],
    银川: [106.3586, 38.1775],
    镇江: [119.4763, 31.9702],
    长春: [125.8154, 44.2584],
    齐齐哈尔: [128.5154, 47.1584],
    四平: [124.8154, 43.2584],
    长沙: [113.0823, 28.2568],
    耒阳: [113.0823, 26.2568],
    长治: [112.8625, 36.4746],
    阳泉: [113.4778, 38.0951],
    青岛: [120.4651, 36.3373],
    韶关: [113.7964, 24.7028]
  };

  var XAData = [
    [{ name: "桂林" }, { name: "潍坊", value: 100, institution: '空15旅', count: 61, hit: 47, }],
    [{ name: "桂林" }, { name: "芜湖", value: 100, institution: '***部队', count: 12, hit: 7, }],
    [{ name: "桂林" }, { name: "湛江", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "鼎新", value: 100, institution: '鼎新基地(评估中心)', count: 3, hit: 2, }],
    [{ name: "桂林" }, { name: "临潼", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "海口", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "衢州", value: 100, institution: '空85旅', count: 72, hit: 42, }],
    [{ name: "桂林" }, { name: "喀什", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "耒阳", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "樟树", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "陆良", value: 100, institution: '空131旅', count: 13, hit: 9, }],
    [{ name: "桂林" }, { name: "四平", value: 100, institution: '空31旅', count: 64, hit: 46, }],
    [{ name: "桂林" }, { name: "笕桥", value: 100, institution: '空83旅', count: 108, hit: 83, }],
    [{ name: "桂林" }, { name: "赤峰", value: 100, institution: '空2旅', count: 13, hit: 10, }],
    [{ name: "桂林" }, { name: "杨村", value: 100, institution: '空72旅', count: 11, hit: 7, }],
    [{ name: "桂林" }, { name: "银川", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "武功", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "拉萨", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "大同", value: 100, institution: '空43旅', count: 16, hit: 13, }],
    [{ name: "桂林" }, { name: "连城", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "霞浦", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "柳州", value: 100, institution: '空126旅', count: 28, hit: 18, }],
    [{ name: "桂林" }, { name: "南京", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "长沙", value: 100, institution: '空54旅', count: 29, hit: 20, }],
    [{ name: "桂林" }, { name: "郑州", value: 100, institution: '空56旅', count: 28, hit: 24, }],
    [{ name: "桂林" }, { name: "惠州", value: 100, institution: '空26旅', count: 27, hit: 18, }],
    [{ name: "桂林" }, { name: "威海", value: 100, institution: '空34旅', count: 8, hit: 8, }],
    [{ name: "桂林" }, { name: "向塘", value: 100, institution: '空40旅', count: 2, hit: 2, }],
    [{ name: "桂林" }, { name: "重庆", value: 100, institution: '空98旅', count: 2, hit: 2, }],
//    [{ name: "桂林" }, { name: "和田", value: 100, institution: '空99旅', count: "*", hit: 1, }],
    [{ name: "桂林" }, { name: "日喀则", value: 100, institution: '***部队', count: "*", hit: "*", }],
    [{ name: "桂林" }, { name: "乌鲁木齐", value: 100, institution: '空110旅', count: 90, hit: 64, }],
    [{ name: "桂林" }, { name: "齐齐哈尔", value: 100, institution: '空3旅', count: 7, hit: 6, }],
  ];

  var XNData = [
    [{ name: "南宁" }, { name: "桂林", value: 100, institution: '空5旅', count: 20, hit: 12, }],
  ];

  var YCData = [
//    [{ name: "日喀则" }, { name: "海口", value: 100 }]
  ];

  var planePath =
    "path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z";
  //var planePath = 'arrow';
  var convertData = function(data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
      var dataItem = data[i];

      var fromCoord = geoCoordMap[dataItem[0].name];
      var toCoord = geoCoordMap[dataItem[1].name];
      if (fromCoord && toCoord) {
        res.push({
          fromName: dataItem[0].name,
          toName: dataItem[1].name,
          coords: [fromCoord, toCoord],
          value: dataItem[1].value
        });
      }
    }
    return res;
  };

  var color = ["#fff", "#fff", "#fff"]; //航线的颜色
  var series = [];
  [
    ["桂林", XAData],
    ["南宁", XNData],
    ["日喀则", YCData]
  ].forEach(function(item, i) {
    series.push(
      {
        name: item[0] + " []",
        type: "effectScatter",
        coordinateSystem: "geo",
        zlevel: 2,
        rippleEffect: {
          brushType: "stroke"
        },
        label: {
          normal: {
            show: true,
            position: "right",
            formatter: "{b}"
          }
        },
        symbolSize: function(val) {
//          return val[2] / 16;
            return 12;
        },
        itemStyle: {
          normal: {
            color: color[i]
          },
          emphasis: {
            areaColor: "#2B91B7"
          }
        },
        data: item[1].map(function(dataItem) {
          return {
            name: dataItem[1].name,
            value: geoCoordMap[dataItem[1].name].concat([dataItem[1].value]),
            institution: dataItem[1].institution,
            count: dataItem[1].count,
            hit: dataItem[1].hit,
          };
        })
      }
    );
  });
  var option = {
    tooltip: {
//      formatter: '{a0}<br>{a1}<br>{b0}<br>{b1}<br>{c}<br>{d}<br>',
      trigger: "item",
      triggerOn: "mousemove|click",
      formatter: function(params, ticket, callback) {
        if (params.seriesType == "effectScatter") {
//          return "|" + params.data.name + "|" + params.data.value[2];
        console.log(params);
        $.ajax({
        url:'http://192.168.12.39:8000/data/pic/',
        type:'POST',
        async:false,
        data:{
            'city':params.name,
        },
        dataType:'json',
        success:function(get){
            console.log('ajax');
            console.log(get);
            pro_detail = get.data;
        },
        });
//          return pro_detail + params.data.institution + "<br>保障" + params.data.count + "次|命中" + params.data.hit + "次";
          return pro_detail;
//        } else if (params.seriesType == "lines") {
//          return (
//            params.data.fromName +
//            ">" +
//            params.data.toName +
//            "<br />" +
//            params.data.value
//          );
//        } else {
//          return params.name;
        }
      }
    },

    geo: {
      map: "china",
      label: {
        emphasis: {
          show: true,
          color: "#fff"
        }
      },
      roam: false,
      //   放大我们的地图
      zoom: 1,
      itemStyle: {
        normal: {
          areaColor: "rgba(43, 196, 243, 0.42)",
          borderColor: "rgba(43, 196, 243, 1)",
          borderWidth: 1
        },
        emphasis: {
          areaColor: "#2B91B7"
        }
      }
    },
    series: series
  };
  myChart.setOption(option);



//  myChart.on('click', function(param){
//    console.log(param.name);
//    $.ajax({
//        url:'http://192.168.12.39:8000/data/pic/',
//        type:'POST',
//        data:{
//            'pro':param.name,
//        },
//        dataType:'json',
//        success:function(get){
//            console.log(get);
//            console.log(param);
//            alert(get.data + '\n____________\n场站：\n' + param + '\n部队：\n');
//        },
//    });
//    });


  window.addEventListener("resize", function() {
    myChart.resize();
  });
})();
