# coding=utf-8
from flask import Flask, render_template, request,url_for, redirect
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line,EffectScatter
from pyecharts.charts import Bar,Page,Map,Timeline,Scatter
from  jinja2 import Markup
from pyecharts.faker import Faker
from pyecharts.globals import ChartType, SymbolType

df1 = pd.read_csv("final_data.csv",encoding = 'gbk')
df2 = pd.read_csv("malnutrition.csv",encoding = 'gbk')
df3 = pd.read_csv("MG_data.csv",encoding = 'gbk')
df4 = pd.read_csv("The_world_per_capita_GDP.csv",encoding = 'gbk')
dfc1=df2.set_index('country')


app = Flask(__name__)
app = Flask(__name__, static_folder="templates")
# 准备工作

regions_available = list(df1.Year.dropna().unique())
# cf.set_config_file(offline=True, theme="ggplot")
# py.offline.init_notebook_mode()
mal_rate = list(df2.country.dropna().unique())
mg_rate = list(df3.country.dropna().unique())
world_per = list(df4.country.dropna().unique())
China = list(dfc1.loc["China"].values)[1:]
Angola = list(dfc1.loc["Angola"].values)[1:]
Ethiopia = list(dfc1.loc["Ethiopia"].values)[1:]
Zambia = list(dfc1.loc["Zambia"].values)[1:]



@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df1.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)

#图表联合
@app.route('/new',methods=['GET'])
def mal_rate1():
    data_str=df2.to_html()
    c = (
        Line()
            .add_xaxis(
            ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
             '2014', '2015', '2016', '2017', '2018', '2019'])
            .add_yaxis("China", China)
            .add_yaxis("Angola", Angola)
            .add_yaxis("Ethiopia", Ethiopia)
            .add_yaxis("Zambia", Zambia)
            .set_global_opts(title_opts=opts.TitleOpts(title="营养不良发生率"))
    )
    return render_template('results1.html',
                           bar_data=c.dump_options(),
                           the_select_region1=mal_rate,
                           the_res = data_str)


@app.route('/world',methods=['GET'])
def world_per1():
    data_str = df4.to_html()
    d = (
        EffectScatter()
            .add_xaxis(
            ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
             '2014', '2015', '2016', '2017'])
            .add_yaxis("China", China)
            .add_yaxis("Angola", Angola)
            .add_yaxis("Ethiopia", Ethiopia)
            .add_yaxis("Zambia", Zambia)
            .set_global_opts(title_opts=opts.TitleOpts(title="四国人均GDP"))
    )
    return render_template('results4.html',
                           bar_data3=d.dump_options(),
                           the_select_region2=world_per,
                           the_res = data_str)

@app.route('/MG',methods=['GET'])
def mg_rate1():
    data_str = df3.to_html()
    return render_template('results3.html',
                           the_select_region3=mg_rate,
                           the_res = data_str)

@app.route('/map',methods=['GET'])
def timeline_map() -> Timeline:
        return render_template('render.html')
#链接地图html页面

#筛选代码
@app.route('/raw',methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df1.query("Year=='{}'".format(the_region))
#     df_summary = dfs.groupby("行业").agg({"企业名称":"count","估值（亿人民币）":"sum","成立年份":"mean"}).sort_values(by = "企业名称",ascending = False )
#     print(df_summary.head(5)) # 在后台检查描述性统计
#     ## user select
    # print(dfs)
#     # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="Year", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results2.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )
#     # plotly.offline.plot(data, filename='file.html')
	
#     with open("render.html", encoding="utf8", mode="r") as f:
#         plot_all = "".join(f.readlines())

@app.route('/new',methods=['POST'])
def mal_rate_select() -> 'html':
    mal_rate = request.form["the_region_selected1"]
    print(mal_rate) # 检查用户输入
    dfs = df2.query("country=='{}'".format(mal_rate))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results1.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region1=mal_rate,
                           )

@app.route('/world',methods=['POST'])
def world_per_select() -> 'html':
    world_per = request.form["the_region_selected2"]
    print(world_per) # 检查用户输入
    dfs = df4.query("country=='{}'".format(world_per))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results4.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region2=world_per,
                           )


@app.route('/MG',methods=['POST'])
def mg_rate_select() -> 'html':
    mg_rate = request.form["the_region_selected3"]
    print(mg_rate) # 检查用户输入
    dfs = df3.query("country=='{}'".format(mg_rate))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results4.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region3=mg_rate,
                           )

#制作单一页面图
@app.route("/showchart1")
def line_base() -> Line:
    China = list(dfc1.loc["China"].values)[1:]
    Angola = list(dfc1.loc["Angola"].values)[1:]
    Ethiopia = list(dfc1.loc["Ethiopia"].values)[1:]
    Zambia = list(dfc1.loc["Zambia"].values)[1:]
    c = (
        Line()
        .add_xaxis(['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
        .add_yaxis("China", China)
        .add_yaxis("Angola",Angola)
        .add_yaxis("Ethiopia", Ethiopia)
        .add_yaxis("Zambia", Zambia)
        .set_global_opts(title_opts=opts.TitleOpts(title="营养不良发生率"))
    )
    return render_template(
        "showchart1.html",
        bar_data = c.dump_options()
    )

@app.route("/showchart3")
def effectscatter_base() -> EffectScatter:
    d = (
        EffectScatter()
            .add_xaxis(
            ['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
             '2014', '2015', '2016', '2017'])
            .add_yaxis("China", China)
            .add_yaxis("Angola", Angola)
            .add_yaxis("Ethiopia", Ethiopia)
            .add_yaxis("Zambia", Zambia)
            .set_global_opts(title_opts=opts.TitleOpts(title="四国人均GDP"))
    )
    return render_template(
        "showchart3.html",
        bar_data3=d.dump_options()
    )

if __name__ == '__main__':
    app.run(debug=True,port=8000)
