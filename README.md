# python-final
# 项目主题：各国营养不良发生率和地方经济的发展关系
### 小组成员：周雅卿，陈淑铧
### 研究结论
#### 2007年到2017年世界各国营养不良的发生率在逐年降低
#### 中国从2007年的12降低到2017年的8.6
#### 变化最大的是非洲大陆的部分国家，Angola从2007年48.6降到2017年的25.

### 代码URL如下所示，项目包含5个URL，包括首页、3个跳转交互图表页以及1个地图跳转页。
本人与一名17级同学组成两人小组，主要负责建立flask框架、将图表导入flask内并使其具有可交互性，以及最后部署到pythonanywhere上。
## [pythonanywhere部署URL](http://heyyaqingzhou.pythonanywhere.com)
## [Github代码URL](https://github.com/YaQingZhou/python-final)


---
### CSS样式：使用boostrap样式
### HTML文档描述
- 使用div标签给Echart图规定样式及初始化图例让其显示
- 通过get的方法在首页引入按钮以及对应页面，让首页按钮通过SUBMIT类型提交实现页面跳转
- 6个URL: 
1. [首页](http://heyyaqingzhou.pythonanywhere.com)
2. [总体筛选页](http://heyyaqingzhou.pythonanywhere.com/raw)
3. [各国营养不良发生率情况页](http://heyyaqingzhou.pythonanywhere.com/new)
4. [各国营养不良发生率与GDP关系页](http://heyyaqingzhou.pythonanywhere.com/MG)
5. [各国人均GDP变化情况页](http://heyyaqingzhou.pythonanywhere.com/world)
6. [地图页](http://heyyaqingzhou.pythonanywhere.com/map)


### Python档描述
- 使用@app.route编写路径在首页上引用html格式地图
- 插入pyechart, pyecharts.charts, pandas, cufflinks, plotly, pyecharts.faker, pyecharts.globals模块，实现数据可视化、表格查看和交互获取数据
- 运用flask框架for循环代码实现首页的图表交互以及跳转页面的表格交互
- 使用return render_template引入模板对html进行修改渲染
- 在数据处理中共使用了4个csv文件，导入了3个数据图


### Web App动作描述
- 通过点击首页的“show”按钮，可以筛选查看同一年份不同国家营养不良发生率和地方经济发展的数值。
- 分别点击首页中“各国营养不良发生率变化情况”，“各国营养不良发生率”，“各国人均GDP变化”三个按钮，可以进入对应图表页，并在这个页面上进行数据交互筛选，并查看返回条形图及表格。
- 通过点击首页的“地图”按钮，可以查看世界各国营养不良率地图。
