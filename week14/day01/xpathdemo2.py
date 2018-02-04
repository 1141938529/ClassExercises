from lxml import etree

page_text = '''
<html>
<title> This is Title </title>
<body>
	<h1> This is h1 </h1>
	<div> This is fisrt div </div>
	<div id="divid">
		<img src="1111.png"/>
		<span id="sp1"> desc 1111.png </span>

		<img src="2222.png"/>
		<span id="sp2"> desc 2222.png </span>

		<p>
			<a href="http://www.xxxxx.com/"> link-of-xxxxxx </a>
		</p>

		<a href="http://www.yyyyyyy.com/"> link-of-yyyyyyyyy </a>
		<br/>
		<a href="http://www.zzzzzzz.com/"> link-of-zzzzzzzzz </a>

	</div>

	<p class="p_classname"> This is p with class name </p>

	<div class="div_classname"> This is div with class name </div>

</body>
</html>
'''
html = etree.HTML(page_text)

# 所有拥有id属性的 div 元素集合列表
# mlist = html.xpath('//div[@id]')
# print(mlist)

# 所有 class 属性为 div_classname 的 div 元素集合列表
# mlist = html.xpath('//div[@class="div_classname"]')
mlist = html.xpath("//div[@class='div_classname']")
# 所有属性 非空 的 div 元素集合列表
mlist = html.xpath('//div[@*]')
# 所有属性为 空 的 div 元素集合列表
mlist = html.xpath('//div[not(@*)]')
# 第一层 div 元素列表，注意下标不是 0，而且类型依然是 列表
mlist = html.xpath("//div[1]/text()")
# 最后一个 div 元素，类型列表
mlist = html.xpath('//div[last()]/text()')
# 倒数第2个 div 元素，类型列表
mlist = html.xpath('//div[last()-1]')
# 位置为最前面 2 个的div元素
mlist = html.xpath('//div[position() < 3]')
# 所有 标签a 的 href 属性值，列表
mlist = html.xpath('//a/@href')
# 第 2 个 div 标签下一层所有 a 的 href 属性值
# 注意 p 中的 a 没拿到
mlist = html.xpath('//div[2]/a/@href')
# 第 2 个 div 标签以下以下所有层面 a 的 href 属性值
mlist = html.xpath('//div[2]//a/@href')
# 第 2 个 div 标签下第1个 span 的 id 属性值
mlist = html.xpath('//div[2]/span[1]/@id')
# 查找 div 和 p 的集合
mlist = html.xpath('//div | //p')
# 除了最后一个 div 以外的所有 div
mlist = html.xpath('//div[position()<last()]/text()')
print(mlist)
