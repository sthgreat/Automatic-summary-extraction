# author: 千山漫雪空
# time: 2018.8.2
# encoding:utf-8

''' ===========180度旋转矩阵=========='''
def fz(a):
    return a[::-1]

def FZ(mat):
    return np.array(fz(list(map(fz, mat))))
'''=============我是分割线=============='''


def process_txt(content_path, dic):
    '''
    预处理处理文本内容
    :param content_path: 文本路径（文本需utf-8编码）
    :return: 返回一个列表[['今天','下雨'],['明天','天气','怎样'],['这','真的','是,'太棒了,]]
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
            dic[count] = s
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


def similary_compute_old(word_li1, word_li2):
    '''
    :param word_li1: ['今天','下雨']
    :param word_li2: ['明天','天气','怎样']
    :return:
    '''
    child = 0
    for i in word_li1:
        if i in word_li2:
            child += 1.0
    mom = math.log(len(word_li1)) + math.log(len(word_li2))
    similary = (child + 0.1)/mom
    return similary

def similary_compute_vec(word_li1, word_li2):
    pass


def value_matrix(li):
    '''
    计算句子与句子之间的权值，返回一个权值矩阵
    :param li: [['今天','下雨'],['明天','天气','怎样'],['这','真的','是,'太棒了,]]
    :return:
    '''
    matrix = np.zeros([len(li), len(li)])
    for i in range(len(li)):
        for k in range(len(li)):
            if k > i:
                matrix[i][k] = similary_compute_old(li[i], li[k])
                matrix[k][i] = similary_compute_old(li[i], li[k])
    # m_r = FZ(matrix)
    # m_last = m_r + matrix
    return matrix


def textrank(matrix, n, dic_2, para=0.8):  # 更改权重字典dic_2，lenth为li的长度，也为matrix的行（宽）长度
    dic_linshi = {}
    sum_li = list(matrix.sum(axis=1))  # 相似度按行相加的结果列表

    for i in range(len(matrix)):
        dic_linshi[i] = 1  # 初始化权重
    count = 0
    while count < n:
        for i in range(len(matrix)):
            s = 0
            for k in range(len(matrix)):
                if i != k:
                    s += (matrix[k][i]/sum_li[k])*dic_linshi[k]
            dic_2[i] = 1-para+para*s

        dic_linshi = dic_2.copy()  # 将dic_2的值传给dic
        count += 1
        # print('\r现在的进度是：{:.2f}%'.format(100*count/n))

if __name__ == '__main__':
    jieba.load_userdict(r'E:\nlp\分词\自定义词典.txt')
    ncount = 0

    dic = {}  # 序号+句子
    dic_2 = {}  # 序号+句子权重

    n = 3
    li = process_txt(r'E:\nlp\Word_process\文章摘要提取\test_3.txt', dic)
    matrix = value_matrix(li)
    textrank(matrix, 500, dic_2)

    sort_d = dict(sorted(dic_2.items(), key=lambda d: d[1], reverse=True))

    ccc = 0
    list_num = []
    for i in sort_d:  # 序号+排序好的句子权重（从大到小）
        if ccc>3:
            break
        list_num.append(i)
        ccc += 1

    list_num.sort()
    for num in list_num:
        print(dic[num])

    print(dic)
    print(sort_d)

