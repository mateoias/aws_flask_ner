'''
function to find the first matching character from the Cedict dictionary and add the pinyin.
doesn't take into account multi tone words. inefficient, but OK for the sozr of the task

'''
def add_pinyin(predictions):
    # prepare Cedict (Chinese dictionary) parser
    from cedict_utils.cedict import CedictParser
    parser = CedictParser()
    parser.read_file("cedict_1_0_ts_utf-8_mdbg.txt")
    entries = parser.parse()
    search_term = predictions
    pinyin = ""
    pinyin_data = []
    #loop through dictionary and get pin yin for eaxch character
    for term in search_term:
        for i in range(len(entries)):
            if term in entries[i].traditional:
                characters = entries[i].traditional
                position = characters.index(term)
                pinyin_string = entries[i].pinyin
                pinyin_list = pinyin_string.split()
                pinyin = pinyin_list[int(position)]
                pinyin_data.append(pinyin)
                pinyin = ""
                break
        search_term.replace(term, '')
    return pinyin_data
 # for e in entries:
    # print(e) 
    # 龟缩 (龜縮) - gui1 suo1
    # 龟背竹 (龜背竹) - gui1 bei4 zhu2
    # 龟船 (龜船) - gui1 chuan2
    # ..
    # entries[200].simplified
    # '敦'
    # entries[200].traditional
    # '㪟'
    # entries[200].pinyin
    # 'dun1'
    # entries[200].raw_line
    # '㪟 敦 [dun1] /variant of 敦[dun1]/'
    # entries[200].meanings
    # ['variant of 敦[dun1]']
