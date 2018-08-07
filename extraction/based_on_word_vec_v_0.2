# author: 千山漫雪空
# time: 2018.8.7
# encoding:utf-8

# ---------------------------------------
#           摘要提取（向量实现）
# ---------------------------------------

def get_distance(np_sentence_vec, np_article_vec):
    A = 0
    B = 0
    AB = 0
    for i in range(len(np_article_vec)):
        A = np.sum(np_sentence_vec*np_sentence_vec)
        B = np.sum(np_article_vec*np_article_vec)
        AB = np.sum(np_article_vec*np_sentence_vec)
    distance = AB / (A ** 0.5 * B ** 0.5)
    return distance


def process_txt(content_path):
    '''
    预处理文本内容
    :param content_path: 文本路径（文本需utf-8编码）
    :return: 返回一个列表[['今天','下雨'],['明天','天气','怎样'],['这','真的','是,'太棒了']]
    '''
    return_li = []
    with open(r'E:\nlp\分词\停用词表_1.txt', 'r', encoding='utf-8') as f1:  # 停用词表导入
        stopword_li = f1.read().split('\n')
        stopword_li.append('啊')

    with open(content_path, 'r', encoding='utf-8') as f:
        content = f.read().replace(' ', '').replace('\n', '').replace('、', '').replace('%', '')
        sentence_li = content.split('。')  # 分句
        count = 0

        for s in sentence_li:  # 构建字典：序号+句子
            dic_1[count] = s
            count += 1

        for element in sentence_li:
            li = []
            word_str = ','.join(jieba.cut(element))  # 分词
            process_li = word_str.split(',')
            for word in process_li:
                if word not in stopword_li:
                    li.append(word)
            return_li.append(li)
            # print(process_li)
            # return_li.append(process_li)

    return return_li


def compute_sentence_vec(sentence_li):  # 计算句子向量，构建字典：序号+句子向量
    with open(r'E:\nlp\语料\文本摘要提取\词向量字典.txt', 'rb') as f:
        dic_word_vec = pickle.load(f)
    print('词向量字典加载完毕')

    count = 0
    for sentence in sentence_li:
        sentence_vec = np.zeros(300, )
        for word in sentence:
            if word in dic_word_vec:
                sentence_vec += dic_word_vec[word]
            else:
                sentence_vec += 0

        dic_2[count] = sentence_vec/len(sentence)
        count += 1


def compute_article_vec():  # 计算全文的向量
    article_vec = np.zeros(300, )
    for sentence in dic_2:
        article_vec += dic_2[sentence]
    return_vec = article_vec/len(dic_2)
    return return_vec


def sigle_process():
    article_vec = compute_article_vec()

    for num in dic_2:
        dic_3[num] = get_distance(dic_2[num], article_vec)

    sorted(dic_3.items(), key=lambda x: x[1], reverse=True)

    count = 0
    for num in dic_3:
        if count > 2:
            break
        print(dic_1[num])
        count += 1


if __name__ == '__main__':
    dic_1 = {}  # 字典：序号+句子
    dic_2 = {}  # 字典：序号+句子向量
    dic_3 = {}  # 字典：序号+句子与文章的相似度
    path = r'E:\nlp\Word_process\文章摘要提取\test_3.txt'
    li = process_txt(path)
    compute_sentence_vec(li)
    sigle_process()
