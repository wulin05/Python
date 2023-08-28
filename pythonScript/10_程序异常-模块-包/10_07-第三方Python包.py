"""
包可以包含一堆的Python模块，而每个模块又内含许多的功能
所以：一个包，就是一堆同类型功能的集合体

非Python官方的第三方包：
1.科学计算中常用的：numpy包
2.数据分析中常用的：pandas包
3.大数据计算中常用的： pyspark、apache-flink包
4.图形可视化常用的：matplotlib、pyecharts
5.人工智能常用的：tensorFlow
6.等

既然第三方包,所有Python没有内置,所以需要安装它们才可以导入使用。

按照第三方包: pip
第三方包安装非常简单,只需要使用Python内置的 pip程序即可,即安装了Python解释器就有pip程序
格式如下：
   pip install 包名称  ---> 即可通过网络快速安装第三方包

如果在国内网速太慢,可以通过指定网址的方式,快速安装：
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
例如：
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

在PyCharm中安装：右下角去点击....
"""


