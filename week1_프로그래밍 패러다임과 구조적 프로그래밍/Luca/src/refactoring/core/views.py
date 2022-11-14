def get_main_page(request):
    return render(request, 'main.html')

def get_loading_page(request):
    return render(request, 'loading.html')

def get_result_page(request):
    user = makeUserDF()
    review_new, novel_new = filtering()

    cb_recmm = CB(user, novel_new)
    cf_recmm = CF(user, review_new, novel_new)
    recmm_idx = cb_recmm + cf_recmm

    recmm_result = [] # 프론트에서 접근 가능한 형태로 변환
    for i in recmm_idx:
        idx_dict = {
            'index' : i,
            'image' : novel.loc[i,'썸네일'], 
            'title' : novel.loc[i,'제목'],
            'author': novel.loc[i,'작가'],
            'genre' : novel.loc[i,'장르'],
            'url' : novel.loc[i, '링크']
        }
        recmm_result.append(idx_dict)
    return render(request, 'result.html', {'recmm_result' : recmm_result})