#coding:utf-8
import sys
import random
#query [title] wiki_title [ref] ref_title ref_content [SPLIT] ... [SPLIT] target_text

def rand_ref(q):
    rand_title = '标题' * random.randint(1, 8)
    ref = '内容'*random.randint(10,256)
    return q+'[title]'+rand_title+'[ref]'+ref

def build_random_data(n=100):
    dataset = []
    for i in range(n):
        query = '查询'*random.randint(1,5)
        rand_count = random.randint(1,5)
        source = []
        while len(source)<rand_count:
            source.append(rand_ref(query))

        dataset.append('[SPLIT]'.join(source)+'[SPLIT]'+'[摘要]'*random.randint(1,128))
    return dataset

train_writer = open('train_data.txt','a+',encoding='utf-8')
dev_writer = open('dev_data.txt','a+',encoding='utf-8')

train_data= build_random_data()
dev_data = build_random_data(10)

for line in train_data:
    train_writer.write(line+'\n')
train_writer.close()

for line in dev_data:
    dev_writer.write(line+'\n')
dev_writer.close()


