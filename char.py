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
        sentence_text = sentence["sentText"].strip().strip('"')
        char_vector += sentence_text
        #print(sentence_text)
    char_vector = de_duplication(char_vector)
    print(char_vector)
    
