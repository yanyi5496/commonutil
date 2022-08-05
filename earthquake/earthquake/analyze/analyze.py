import json
import os

import folium
import jieba
from folium.plugins import HeatMap
from pyecharts.charts import Bar
from wordcloud import WordCloud


def draw_heat_map(data, result_path, file_name):
    heat_map_counter = {}
    for i in data:
        longitude = float('%.1f' % float(i.get('longitude')))
        latitude = float('%.1f' % float(i.get('latitude')))
        name = str(latitude) + '-' + str(longitude)
        if name in heat_map_counter:
            heat_map_counter[name][2] = heat_map_counter[name][2] + 1
        else:
            heat_map_counter[name] = [latitude, longitude, 1]
    result = [[j[0], j[1], j[2]] for i, j in heat_map_counter.items()]
    map_ = folium.Map(location=[35, 110], zoom_start=5)
    HeatMap(result).add_to(map_)
    map_.save(os.path.join(result_path, file_name + '.html'))


def draw_year_bar(title, data, result_path):
    counter = {}
    for each in data:
        o_time = each.get('o_time').split(' ')[0].split('-')[0]
        if o_time in counter:
            counter[o_time] += 1
        else:
            counter[o_time] = 1
    counter = dict(sorted(counter.items(), key=lambda item: item[0]))

    bar = Bar()
    attrs = [i for i, j in counter.items()]
    values = [j for i, j in counter.items()]
    bar.add_xaxis(attrs)
    bar.add_yaxis('111', values)
    bar.render(os.path.join(result_path, '%s.html' % title))


'''统计词频'''


def statistics(texts, stopwords):
    words_dict = {}
    for text in texts:
        temp = jieba.cut(text)
        for t in temp:
            if t in stopwords or t == 'unknown':
                continue
            if t in words_dict.keys():
                words_dict[t] += 1
            else:
                words_dict[t] = 1
    return words_dict


def draw_word_cloud(words, title, result_path):
    wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920, height=1080,
                   margin=5)
    wc.generate_from_frequencies(words)
    wc.to_file(os.path.join(result_path, title + '.png'))


def main():
    data_source_path = '../../data.json'
    result_path = './result'
    if not os.path.exists(result_path):
        os.mkdir(result_path)

    data = json.load(open(data_source_path, 'r', encoding='utf-8'))

    # 热力图
    draw_heat_map(data, result_path, 'heatmap')

    # 柱状图

    draw_year_bar(title='每年地震发生频次统计', data=data, result_path=result_path)

    # 词云
    stopwords = open('stopwords.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
    texts = [each.get('location') for each in data]
    words_dict = statistics(texts, stopwords)
    draw_word_cloud(words_dict, '地震地点名词云', result_path=result_path)


if __name__ == '__main__':
    main()
