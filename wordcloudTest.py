import pymysql
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy import ndimage

connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='',
    db='scrapytest',
    charset='utf8',
    use_unicode=True
)
cursor = connect.cursor()
cursor.execute(
                "select text from comment"
                )
data=cursor.fetchall()
connect.close()
cursor.close()

image=ndimage.imread('shu.jpg')  # 解析该图片

wc=WordCloud(
     mode='RGBA',#设置透明底色
     background_color=None,
     mask=image, #词云形状设置为背景图像
     max_words=500,#显示的词的最大个数
     font_path="C:\\Windows\\Fonts\\simfang.ttf",#设置字体，否则中文可能会出现乱码
     scale=5,#扩大三倍
     collocations=False, #去除重复词
     random_state=10   #配色数
 )

 #生成词云
image_colors = ImageColorGenerator(image)# 基于背景颜色设置字体色彩
wc.generate(data.__str__())#根据文本生成词云


plt.imshow(wc)#显示词云图
plt.axis("off")#关闭坐标轴
plt.show()#显示窗口
wc.to_file('test.png')# 保存图片