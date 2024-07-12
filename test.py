import numpy as np

for i in range(10):
    file_path = r'<해당 코드 주소>.txt' % i
    try:
        with open(file_path, 'rt', encoding='utf-8') as f:
            line = f.read()
    except FileNotFoundError:
        print(f"파일 {file_path}을(를) 찾을 수 없습니다. 다음 파일로 넘어갑니다.")
        continue


    arr1 = []
    a = ""
    check = False
    arr2 = [] 
    j = 0

    while j < len(line):
        if line[j] == '\n':  
            if arr2:
                arr1.append(arr2)
                arr2 = []
        elif line[j] == '(':
            check = True
        elif line[j] == ')':
            check = False
            if a:
                if j + 2 < len(line) and line[j+1:j+3] == '/(':
                    arr3 = [a]
                    a = ""
                    j += 3
                    check = True
                    while j < len(line):
                        if line[j] == ')':
                            check = False
                            if a:
                                arr3.append(a)
                            a = ""
                            break
                        elif check:
                            a += line[j]
                        j += 1
                    arr2.append(arr3)
                else:
                    arr2.append([a, ""])          
            a = ""
        elif check:
            a += line[j]
        j += 1

    if arr2:
        arr1.append(arr2)

    arr_np = np.array(arr1, dtype=object)
    print(arr_np)

    cl_st = []
    fi_cl_st = []

    for a in range(len(arr_np)):
        for b in range(len(arr_np[a])):
            for c in range(len(arr_np[a][b])):
                arr_test = arr_np[a][b][c] 
                cl_st.append(arr_test)

    k = 0
    while k < len(cl_st) - 1:
        try:
            s = int(input(f'리스트 중 하나 선택하세요 첫번째 1 두번째 2\n {cl_st[k]} , {cl_st[k + 1]}: '))
            if s == 1: 
                fi_st = cl_st[k]
            elif s == 2:
                fi_st = cl_st[k + 1]
            else:
                print("잘못 입력하셨습니다.")
                fi_st = None
        except ValueError:
            print("숫자를 입력해주세요.")
            fi_st = None

        if fi_st is not None:
            print(f'선택된 값: {fi_st}')
            fi_cl_st.append(fi_st)
        else:
            print("선택된 값이 없습니다.")
        k += 2

    print(fi_cl_st)

    new_line = ""
    l = 0
    choice_index = 0
    while l < len(line):
        if line[l] == '(':
            m = l
            while m < len(line) and line[m] != ')':
                m += 1
            if m < len(line):
                if m + 2 < len(line) and line[m+1:m+3] == '/(':
                    if choice_index < len(fi_cl_st):
                        new_line += fi_cl_st[choice_index]
                        choice_index += 1
                    m += 3 
                    while m < len(line) and line[m] != ')':
                        m += 1
                    m += 1
                else:
                    if choice_index < len(fi_cl_st):
                        new_line += fi_cl_st[choice_index]
                        choice_index += 1
                    m += 1
            l = m
        else:
            new_line += line[l]
            l += 1

    print("최종 결과:")
    print(new_line)

    output_file_path = r'<저장할 위치 및 파일 이름>.txt' % i
    with open(output_file_path, "w", encoding='utf-8') as file:
        file.write(new_line)

