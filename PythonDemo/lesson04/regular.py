# import re
# shazi='djadadhalsdkasdjpythonsdjsdjs;dfs;fsdfsfdsf'
# zhuzi='python'
# shaizi=re.compile(zhuzi)
# taojin=re.search(shaizi,shazi)
# print(taojin.group(0))
#
# p3=re.compile(p2)
# taojin=re.search(p3,p1)
# print(taojin.group(0))



import re
p1='fsfsdfsxdax2533450@sina.pq.ail.amza.comsdsdsdsdfdsf'
p2='2533450@sina\.pq\.ail\.amza\.com'
key=r"http://www.nsfbuhwe.com and https://www.auhfusna.com"#
p1=r"https*://"#看那个星号
pattern1=re.compile(p1)
print(pattern1.findall(key))

'''
。*？  findall
+ 无线匹配多次（加号写在哪边就匹配多次），如ab+  abbbb
* 匹配0次，或者多次
.表示任何一个字符（任意匹配，无线循环）
'''

import re
key='<htMl>aaa</html> <xml>aavccc</xml>'
p1=r"<[HhTtXx][Mm][Ll]>.+?</[HhTtXx][Mm][Ll]>"
pattern=re.compile(p1)
print(pattern.findall(key))


import re
key=r"lalala<hTml>hello</Html>heiheihei"
p1=r"[Hh][Tt][Mm][Ll].+?</[Hh][Tt][Mm][Ll]>"
pattern=re.compile(p1)
print(pattern.findall(key))


import re
key=r"chuxiuhong@hit.edu.cn"
p1=r"@(.+?\.)"
#p1=r"@.+?"
pattern=re.compile(p1)
print(pattern.findall(key))

import re
key=r"saas and sas and saaas"
p1=r"sa{1,2}s"
pattern=re.compile(p1)
print(pattern.findall(key))


import re
key=r"jjhee jhhhee jheeeeeee"
p1=r"j{1,2}h{1,3}e{1,7}"
pattern=re.compile(p1)
print(pattern.findall(key))


''''
?<= 前缀 ./?  ？=后缀  

'''