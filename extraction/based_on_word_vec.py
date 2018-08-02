# author: 千山漫雪空
# time: 2018.7.25
# encoding:utf-8

# ---------------------------------------
           摘要提取（向量实现）
# ---------------------------------------
def get_distance(list_vec, list_word):
    A = 0
    B = 0
    AB = 0
    for i in range(len(list_word)):
        A = A + list_vec[i] * list_vec[i]
        B = B + list_word[i] * list_word[i]
        AB = AB + list_word[i] * list_vec[i]
    distance = AB / (A ** 0.5 * B ** 0.5)
    return distance

def deal_sentence(str, dic):  # 输入句子str，返回累加的句子向量
    sum_li = np.zeros(300)
    li = ','.join(jieba.cut(str)).split(',')
    for i in li:
        if i in dic:
            sum_li += np.array(dic[i])
    return(sum_li)

def compare(value, dic_4):  # 输入value,dic字典，dic_4字典 /输出句子序号
    dic = dict(zip(dic_4.values(), dic_4.keys()))
    return(dic[value])

dic = {}  # 序号+句子
dict_2 = {}  # 序号+句子向量
dict_3 = {}  # 词+词向量
text_vec = np.zeros(300)
count = 1

with open(r'E:\nlp\Word_process\文章摘要提取\test_3.txt', 'r', encoding='utf-8') as f:
    content = f.read().replace(' ', '').replace('\n', '')
    content_1 = content.split('。')

with open(r'E:\nlp\Word_process\Data\sgns.sogou.word', 'r', encoding='utf-8') as f:  # word中数据写入
    for element in f:
        element_list = element.split(' ')
        word_name = element_list[0]
        del element_list[len(element_list) - 1]
        del element_list[0]
        if len(element_list) == 0:
            continue
        else:
            dict_3[word_name] = list(map(eval, element_list))  # 数据写入结束
    print('词+词向量字典构建完毕')

for i in content_1:  # 随循环构建dic，dict_2
    dic[count] = i  # 构建字典：序号+句子
    dict_2[count] = deal_sentence(i, dict_3)  # 构建字典：序号+句子向量
    count += 1

for key in dict_2:  # 求表达全文的向量
    text_vec += dict_2[key]

text_vec = text_vec/(len(dict_2))

distence_li = []
dic_4 = {}  # 序号+与文本向量的cos值
for key in dict_2:
    value = get_distance(list_vec=dict_2[key], list_word=text_vec)
    dic_4[key] = value
    distence_li.append(value)

distence_li.sort()
distence_li.reverse()
print(distence_li)

for i in range(1,4):
    print(dic[compare(distence_li[i], dic_4)])
    with open(r'E:\nlp\Word_process\文章摘要提取\test_3_向量.txt', 'a+', encoding='utf-8') as f:
        f.write(dic[compare(distence_li[i], dic_4)])
