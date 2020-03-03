import requests
import json
import ast

#지역별 상수
CONST_SEOUL= 1100000000
CONST_BUSAN= 2600000000
CONST_DAEGU= 2700000000
CONST_INCHEON= 2800000000
CONST_GWANGJU= 2900000000
CONST_DAEJEON= 3000000000
CONST_ULSAN= 3100000000
CONST_SEJONG= 3600000000
CONST_GYUNGGI= 4100000000
CONST_GANGWON= 4200000000
CONST_CHUNGBUK= 4300000000
CONST_CHUNGNAM= 4400000000
CONST_JEONBUK= 4500000000
CONST_JEONNAM= 4600000000
CONST_GYUNGBUK= 4700000000
CONST_GYUNGNAM= 4800000000
CONST_JEJU= 5000000000 

region_list = [CONST_SEOUL,CONST_BUSAN,CONST_DAEGU,CONST_INCHEON,CONST_GWANGJU,
            CONST_DAEJEON,CONST_ULSAN,CONST_SEJONG,CONST_GYUNGGI,CONST_GANGWON,
            CONST_CHUNGBUK,CONST_CHUNGNAM,CONST_JEONBUK,CONST_JEONNAM,CONST_GYUNGBUK,
            CONST_GYUNGNAM,CONST_JEJU]

#region_list = [CONST_CHUNGNAM,CONST_DAEGU];

def ret_regionName(regionCode):
        global region_list
        if regionCode == region_list[0]: return "SEOUL"
        elif regionCode == region_list[1]: return "BUSAN"
        elif regionCode == region_list[2]: return "DAEGU"
        elif regionCode == region_list[3]: return "INCHEON"
        elif regionCode == region_list[4]: return "GWANGJU"
        elif regionCode == region_list[5]: return "DAEJEON"
        elif regionCode == region_list[6]: return "ULSAN"
        elif regionCode == region_list[7]: return "SEJONG"
        elif regionCode == region_list[8]: return "GYEONGGI"
        elif regionCode == region_list[9]: return "GANGWON"
        elif regionCode == region_list[10]: return "CHUNGBUK"
        elif regionCode == region_list[11]: return "CHUNGNAM"
        elif regionCode == region_list[12]: return "JEONBUK"
        elif regionCode == region_list[13]: return "JEONNAM"
        elif regionCode == region_list[14]: return "GYEONGBUK"
        elif regionCode == region_list[15]: return "GYEONGNAM"
        elif regionCode == region_list[16]: return "JEJU"
        else: return "SEOUL"

f = open('school-code.json', mode='wt', encoding='utf-8')

def get_code():
    global region_list
    ret = "{"
    for j in region_list:
        ret+="'"+ret_regionName(j)+"':"
        result = {'elementary': {}, 'middle': {}, 'high': {}, 'special': {}}

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }

        data = {
            'HG_CD': '',
            'SEARCH_KIND': '',
            'HG_JONGRYU_GB': '',
            'GS_HANGMOK_CD': '',
            'GS_HANGMOK_NM': '',
            'GU_GUN_CODE': '',
            'SIDO_CODE': j,
            'GUGUN_CODE': '',
            'SRC_HG_NM': ''
        }

        response = json.loads(requests.post('https://www.schoolinfo.go.kr/ei/ss/Pneiss_a01_l0.do',
                                            headers=headers, data=data).text)

        for i in range(2, 6):
            sch = response['schoolList0'+str(i)]
            if sch:
                for c in range(0, len(sch)):
                    code = sch[c]['SCHUL_CODE']
                    name = sch[c]['SCHUL_NM']
                    if i==2: result['elementary'][name] = code
                    elif i==3: result['middle'][name] = code
                    elif i==4: result['high'][name] = code
                    else: result['special'][name] = code
        ret+=str(result)+",\n"
    ret=ret[:-1]+"}"
    return ret
    
# get_code('당신의 학교 이름')
f.write(json.dumps(ast.literal_eval(get_code()),ensure_ascii=False))
f.write('\n')
#print(get_code(''))
f.close()