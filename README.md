# iHR_auto_sign
i人事自动签到方案  

fiddler 抓包获取请求信息，requests 模拟请求 

详细： https://www.iots.vip/post/python-ihr360-auto-doSign.html


fiddler 配置过滤器
　　打开 Fiddler 后，选择 “Filters”并勾选，选择 “Use Filters”，在 “Hosts” 项目中，选择 “Show only the following Hosts”，并填入 “www.ihr360.com” ，同时，在 “Request Headers” 中，勾选 “Show only if URL contains”，填入 “gateway/attendance/aggregate/attendance/api/sign/doSign” ，点击右上角的 Actions，选择 “Run Filterset now” 以生效过滤器。在 Fiddler 左侧的流量信息栏中，使用 Ctrl + X 清除当前所有流量信息。
