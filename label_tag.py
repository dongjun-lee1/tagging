import os

txt_list = []
dir_path = "D:/preprocessed"

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.txt' in file:
            file_path = os.path.join(root, file)
            txt_list.append(file_path)

#.txt 확장자 파일 찾는 코드. 공부해볼것

tag = {'다수':0, '교복':0, '장신구':0, '가방':0, '무늬':0, '소지품':0,
       '입장':0, '퇴장':0, '상호작용_물건':0, '계산':0, '의심행동':0,
       '직원행동':0, '복합행동':0, '섭취':0, '게시판':0, '가격확인':0, '상품':0}    #태그목록

for i in txt_list:
    f = open(i, 'r', encoding="UTF-8")

    line = f.readlines()

    for j in range(len(line)):
        for k in range(len(line[j])):
            if(line[j][k] == '#'):
                for p in range(k, len(line[j])):
                    if(line[j][p] == '\t' or p == len(line[j])-1):
                        string = line[j][k+1:p]
                        result1 = string.replace(' ','')
                        result = result1.replace('\n','')
                        try:
                            tag[result] += 1
                        except:
                            print(result)
                        if(result == '의심행동'):
                            print(i,j,line[j])
                        break
                        
    f.close()

print(tag)