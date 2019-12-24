import jieba
import json

def de_duplication(str):
    dedup_str = ''
    for char in str:
        if not char in dedup_str:
            dedup_str += char
    return dedup_str

with open('data/new/dev.txt', 'rt', encoding='utf-8') as fin:
    char_vector=""
    for line in fin:
        line = line.strip()
        if not line:
            continue;
        sentence = json.loads(line)
	
        relation_seg_list = [] 
        for relation_mention in sentence["relationMentions"]:
            tmp1 = jieba.cut(relation_mention["em1Text"], cut_all=False)
            tmp2 = jieba.cut(relation_mention["em2Text"], cut_all=False)
            relation_seg_list.append('{"em1Text":"'+" ".join(tmp1)+'", '+'"em2Text":"'+" ".join(tmp2)+'", '+'"label":"'+relation_mention["label"]+'"}')
        relation_seg_all = '"relationMentions":['+",".join(relation_seg_list)+']'

        sentence_text = sentence["sentText"].strip().strip('"')
        seg_list = jieba.cut(sentence_text, cut_all=False)
        sentence_text_all = '"sentText":"' + " ".join(seg_list) + '"'
    

        entity_seg_list = [] 
        for entity_mention in sentence["entityMentions"]:
            tmp = jieba.cut(entity_mention["text"], cut_all=False)
            entity_mention["text"] = " ".join(tmp)
            entity_mention = str(entity_mention)
            entity_seg_list.append(entity_mention)
        #print(entity_seg_list)
        entity_seg_all = '"entityMentions":['+",".join(entity_seg_list)+']'

        print('{'+relation_seg_all+','+sentence_text_all+','+entity_seg_all+'}')
