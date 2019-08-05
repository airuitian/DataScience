# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QuotesScrapyPipeline(object):

    # process_item是必须要实现的方法
    def process_item(self, item, spider):
        # 使用dict转换item，然后插入数据库
        quote_info = dict(item)
        self.write_to_file(quote_info, 'quote_info')

        return item

    # 定义一个向文件里写的方法
    def write_to_file(self, quote_info, file_name):
    	# a 代表追加的写
        with open(file_name, 'a') as f:
        	# 字典中只有两个key, content和tags
            for values in quote_info.values():
            	# tags 的value是列表，如果是列表，则将列表转换为字符串
                if isinstance(values, list):
                	values = self.__convert_list_to_string(values)

                # 向文件中写单词
                # 需要注意的是这里，没有对标点符号的处理
                for word in values.split(' '):
                	f.write(word + '\n')
    # 将列表转换为字符串
    def __convert_list_to_string(self, values):

    	return ' '.join(values)


