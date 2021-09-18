// 柱状图1模块
(function () {
  // 实例化对象
  var myChart = echarts.init(document.querySelector(".bar .chart"));
  // 指定配置和数据
  var option = {
    color: ["#67b55b", "#ffd700", "#d9c9ea", "#e05423", "#ccffff", "#ffff00", "#ffffcc"],
    tooltip: {
      trigger: "axis",
      axisPointer: {
        // 坐标轴指示器，坐标轴触发有效
        type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
      }
    },
    grid: {
      left: "0%",
      top: "10px",
      right: "0%",
      bottom: "4%",
      containLabel: true
    },
    dataset:{
        source:[],
    },
    xAxis: [
      {
        type: "category",
        axisTick: {
          alignWithLabel: true
        },
        axisLabel: {
          boundaryGap:false,
          interval:0,
          rotate:90,
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "10"
          },
        },
        axisLine: {
          show: false
        }
      }
    ],
    yAxis: [
      {
        type: "value",
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
            // width: 1,
            // type: "solid"
          }
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: [    ],
  };

  option.dataset.source.push(['失利原因', ]);
  option.dataset.source[0].push.apply(    option.dataset.source[0], reasons  );
  for(var i=0,len=missiles.length;i<len;i++){
    option.dataset.source.push([missiles[i], ]);
    for(var j=0, len1=reasons.length; j<len1; j++){
        // 假的
//        if(missiles[i]=='YJ-91'&&reasons[j]=='设计不足'){
//            option.dataset.source[i+1].push(9);
//        }
//        else if(missiles[i]=='YJ-91'||missiles[i]=='Х-31П'){
//            console.log('跳过');
//        }
//        else{
//        option.dataset.source[i+1].push(
//                                barDataAllSeriesForMR[missiles[i]][reasons[j]]
//                                );
//        };
        option.dataset.source[i+1].push(
                                barDataAllSeriesForMR[missiles[i]][reasons[j]]
                                );
        if(i==0){
            option.series.push(
            { type: 'bar',
//                barCategoryGap: 50,
//                barWidth: 5,
            }
            );
        };
    };
  };

//  option.dataset.source.push(['YJ-91', ]);
//  option.dataset.source.push(['Х-31П', ]);
//  for(var j=0, len1=reasons.length; j<len1; j++){
//    option.dataset.source[12].push(
//                                barDataAllSeriesForMR['YJ-91'][reasons[j]]
//                                );
//    option.dataset.source[13].push(
//                                barDataAllSeriesForMR['Х-31П'][reasons[j]]
//                                );
//  };
  console.log('option.dataset.source');
  console.log(option.dataset.source);

  // 把配置给实例对象
  myChart.showLoading();
  myChart.setOption(option);
  myChart.hideLoading();
  window.addEventListener("resize", function () {
    myChart.resize();
  });

// 柱形图1 两个筛选条件
//  document.querySelector(".bar h2 #select-bar1").addEventListener("change", function (e) {
//    console.log("select1-change");
//    var i = e.target.selectedIndex - 1;
//    if(i < 0){
//        i = 0;
//    };
//    option.series[0].data = dataAll[i].data;
//    myChart.showLoading();
//    myChart.setOption(option);
//    myChart.hideLoading();
//});
//
//    document.querySelector(".bar h2 #select-bar2").addEventListener("change", function (e) {
//        console.log("select2-change for:year、reason");
//        var i = e.target.selectedIndex - 1;
//        if(i < 0){
//            i = 0;
//        };
//        var y = document.querySelector(".bar h2 #select-bar1").value.replace('年', '');
//        var r = e.target.value;
//        console.log(barDataAllSeriesForR.y);
//        option.series[0].data = barDataAllSeriesForR[y][r];
//        myChart.showLoading();
//        myChart.setOption(option);
//        myChart.hideLoading();
//    });

  myChart.on('click', function(param){    console.log(param);  });

})();

// 折线图1
(function () {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".line .chart"));

  // (1)准备数据
//  [
//      [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
//      [21, 22, 23, 24, 25, 36, 37, 28, 9, 60, 31, 92]
//    ]
  var data = {
    lines: [
        lineData1TempJson[1],
        lineData1TempJson[2],
        lineData1TempJsonSum[0],
    ],
  };

  // 2. 指定配置和数据
  var option = {
    color: ["#FFFFCC", "#00d887", "#ed3f35"],
    tooltip: {
      // 通过坐标轴来触发
      trigger: "axis"
    },
    legend: {
      // 距离容器10%
      right: "10%",
      // 修饰图例文字的颜色
      textStyle: {
        color: "#4c9bfd"
      }
      // 如果series 里面设置了name，此时图例组件的data可以省略
    },
    grid: {
      top: "20%",
      left: "3%",
      right: "4%",
      bottom: "3%",
      show: true,
      borderColor: "#012f4a",
      containLabel: true
    },

    xAxis: {
      type: "category",
      boundaryGap: false,
      // 修饰刻度标签的颜色
      axisLabel: {
        interval:0,
        rotate:60,
        color: "rgba(255,255,255,.7)"
      },
      // 去除刻度
      axisTick: {
        show: true,
      },
      // 去除x坐标轴的颜色
      axisLine: {
        show: false
      },
      data: lineData1TempJson[0],
    },
    yAxis: {
      type: "value",
      // 去除刻度
      axisTick: {
        show: false
      },
      // 修饰刻度标签的颜色
      axisLabel: {
        color: "rgba(255,255,255,.7)"
      },
      // 修改y轴分割线的颜色
      splitLine: {
        lineStyle: {
          color: "#012f4a"
        }
      }
    },
    series: [
      {
        name: "俄制弹药",
        type: "line",
        stack: "111",
        // 是否让线条圆滑显示
        smooth: true,
        data: data.lines[0],
      },
      {
//        name: "空地弹药",
        name: "国产弹药",
        type: "line",
        stack: "222",
        smooth: true,
        data: data.lines[1],
      },
      {
        name: "总数",
        type: "line",
        stack: "333",
        smooth: true,
        data: data.lines[2],
      }
    ]
  };

//        label: {
//            normal:{
//                show: true,
//                position: 'top',
//                textStyle:{
//                    color:'#0000',
//                },
//                formatter:'',
//            },
//        },
//  var series = option['series'];
//  var fun = function(params){
//    var data3 = 0;
//    for(var i=1, l = series.length; i<l.length; i=i+1){
//        data3 += series[i].data[params.dataIndex][l];
//    };
//    return data3;
//  };
//  series[series.length-1]["label"]["formatter"] = fun;

  // 3. 把配置和数据给实例对象
  myChart.showLoading();
  myChart.setOption(option);
  myChart.hideLoading();

  // 重新把配置好的新数据给实例对象
  myChart.showLoading();
  myChart.setOption(option);
  myChart.hideLoading();
  window.addEventListener("resize", function () {
    myChart.resize();
  });

  //选择原因 重新绘图
  document.querySelector(".line h2 #select-line1").addEventListener("change", function(e){
    console.log("select-change");
    var i = e.target.selectedIndex;
    if(i == 0){
        i = 1;
    };
    option.series[0].data = lineData1TempJson[i*2-1];
    option.series[1].data = lineData1TempJson[i*2];
    option.series[2].data = lineData1TempJsonSum[i - 1];
    console.log("e");
    console.log(option.series[0].data);
    console.log("zh");
    console.log(option.series[1].data);
    console.log("sum");
    console.log(option.series[2].data);
    myChart.showLoading();
    myChart.setOption(option);
    myChart.hideLoading();
  });

})();

// 饼图1定制
(function () {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".pie .chart"));

  option = {
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)",
      position: function (p) {
        //其中p为当前鼠标的位置
        return [p[0] + 10, p[1] - 10];
      }
    },
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      data: pieKey1,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "10"
      }
    },
    series: [
      {
        name: "型号统计",
        type: "pie",
        center: ["50%", "42%"],
        radius: ["40%", "60%"],
        color: [
          "#065aab",
          "#066eab",
          "#0682ab",
          "#0696ab",
          "#06a0ab",
          "#06b4ab",
          "#06c8ab",
          "#06dcab",
          "#06f0ab"
        ],
        label: {
            show: true,
            fontSize: 10
            },
        labelLine: { show: true },
        data: pieData1,
      }
    ]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart.showLoading();
  myChart.setOption(option);
  myChart.hideLoading();
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();


// 横向柱状图模块
(function () {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".bar1 .chart"));

  //data需要按大->小排好顺序
  var data = barData2;
  var titlename = barName;
  var valdata = barData2Hans;
  var dataNum =  new Array();
  for(var i=0; i<barName.length; i++)
  {
    dataNum.push(100);
  }
  var myColor = ["#1089E7", "#F57474", "#56D0E3", "#F8B448", "#8B78F6", "#56D0E3"];
  option = {
    //图标位置
    grid: {
      top: "10%",
      left: "22%",
      bottom: "10%"
    },
    xAxis: {
      show: false
    },
    yAxis: [
      {
        show: true,
        data: titlename,
        inverse: true,
        axisLine: {
          show: false
        },
        splitLine: {
          show: false
        },
        axisTick: {
          show: false
        },
        axisLabel: {
          color: "#fff",
          interval:0,
          fontSize:8,
          rich: {
            lg: {
              backgroundColor: "#339911",
              color: "#fff",
              borderRadius: 15,
              // padding: 5,
              align: "center",
              width: 15,
              height: 15
            }
          }
        }
      },
      {
        show: true,
        inverse: true,
        data: valdata,
        axisLabel: {
          textStyle: {
            fontSize: 12,
            color: "#fff"
          }
        }
      }
    ],
    series: [
      {
        name: "条",
        type: "bar",
        yAxisIndex: 0,
        data: data,
        barCategoryGap: 50,
        barWidth: 10,
        itemStyle: {
          normal: {
            barBorderRadius: 20,
            color: function (params) {
              var num = myColor.length;
              return myColor[params.dataIndex % num];
            }
          }
        },
        label: {
          normal: {
            show: true,
            position: "inside",
            formatter: "{c}%"
          }
        }
      },
//      {
//        name: "框",
//        type: "bar",
//        yAxisIndex: 1,
//        barCategoryGap: 50,
//        data: dataNum,
//        barWidth: 10,
//        itemStyle: {
//          normal: {
//            color: "none",
//            borderColor: "#00c1de",
//            borderWidth: 3,
//            barBorderRadius: 15
//          }
//        }
//      }
    ]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart.showLoading();
  myChart.setOption(option);
  myChart.hideLoading();
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();


// 折线图2
(function () {
  // 基于准备好的dom，初始化echarts实例
  var myChart = echarts.init(document.querySelector(".line1 .chart"));

  var data = {
    lines: [
        lineData2[0],
        lineData2[1],
        lineData2[2],
    ]
  };

  option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        lineStyle: {
          color: "#dddc6b"
        }
      }
    },
    legend: {
      top: "0%",
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    grid: {
      left: "10",
      top: "30",
      right: "10",
      bottom: "10",
      containLabel: true
    },

    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        axisLabel: {
          interval:0,
          rotate:60,
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.2)"
          }
        },
        data: data.lines[2],
      },
      {
        axisPointer: { show: false },
        axisLine: { show: false },
        position: "bottom",
        offset: 20
      }
    ],

    yAxis: [
      {
        type: "value",
        axisTick: { show: false },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        },
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
          }
        },

        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: [
      {
        name: "俄制弹药",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 5,
        showSymbol: false,
        lineStyle: {
          normal: {
            color: "#0184d5",
            width: 2
          }
        },
        areaStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                {
                  offset: 0,
                  color: "rgba(1, 132, 213, 0.4)"
                },
                {
                  offset: 0.8,
                  color: "rgba(1, 132, 213, 0.1)"
                }
              ],
              false
            ),
            shadowColor: "rgba(0, 0, 0, 0.1)"
          }
        },
        itemStyle: {
          normal: {
            color: "#0184d5",
            borderColor: "rgba(221, 220, 107, .1)",
            borderWidth: 12
          }
        },
        data: data.lines[0],
      },
      {
//        name: "空地弹药",
        name: "国产弹药",
        type: "line",
        smooth: true,
        symbol: "circle",
        symbolSize: 5,
        showSymbol: false,
        lineStyle: {
          normal: {
            color: "#00d887",
            width: 2
          }
        },
        areaStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                {
                  offset: 0,
                  color: "rgba(0, 216, 135, 0.4)"
                },
                {
                  offset: 0.8,
                  color: "rgba(0, 216, 135, 0.1)"
                }
              ],
              false
            ),
            shadowColor: "rgba(0, 0, 0, 0.1)"
          }
        },
        itemStyle: {
          normal: {
            color: "#00d887",
            borderColor: "rgba(221, 220, 107, .1)",
            borderWidth: 12
          }
        },
        data: data.lines[1],
      }
    ]
  };

  // 使用刚指定的配置项和数据显示图表。
  myChart.showLoading();
  myChart.setOption(option);
  myChart.hideLoading();
  window.addEventListener("resize", function () {
    myChart.resize();
  });
})();

// 饼图2
(function () {
  // 1. 实例化对象
  var myChart = echarts.init(document.querySelector(".pie1  .chart"));
  // 2. 指定配置项和数据
  var option = {
    legend: {
      top: "90%",
      itemWidth: 10,
      itemHeight: 10,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "10"
      }
    },
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // 注意颜色写的位置
    color: [
      "#006cff",
      "#60cda0",
      "#ed8884",
      "#ff9f7f",
      "#0096ff",
      "#9fe6b8",
      "#32c5e9",
      "#1d9dff"
    ],
    series: [
      {
        name: "型号统计",
        type: "pie",
        // 如果radius是百分比则必须加引号
        radius: ["10%", "70%"],
        center: ["50%", "42%"],
        roseType: "radius",
        data: pieData2,
        // 修饰饼形图文字相关的样式 label对象
        label: {
          fontSize: 10
        },
        // 修饰引导线样式
        labelLine: {
          // 连接到图形的线长度
          length: 10,
          // 连接到文字的线长度
          length2: 10
        }
      }
    ]
  };

  // 3. 配置项和数据给我们的实例化对象
  myChart.setOption(option);
  // 4. 当我们浏览器缩放的时候，图表也等比例缩放
  window.addEventListener("resize", function () {
    // 让我们的图表调用 resize这个方法
    myChart.resize();
  });
})();


//(function (){
//
//    document.querySelector("#dataOut").addEventListener("click", function (e){
//        console.log("点击导出");
//    });
//
//})();
