class Question:
    def __init__(self, api_method: str, question_number: int, users: int) -> None:
        self.api_method = api_method
        self.question_number = question_number
        self.dict_user = [0] * users
        
    def get_q_base(self, request):
        if self.api_method == "GET" and self.question_number == 0:
            return render(request, 'q_base.html')

    def get_q1(self, request):
        if self.api_method == "GET" and self.question_number == 1:
            return render(request, 'q1.html')

    def get_q2(self, request):
        if self.api_method == "GET" and self.question_number == 2:
            if request.GET.get('adult') and request.GET.get('finished'):
                return render(request, 'q2.html')

    def get_q3(self, request):
        if self.api_method == "GET" and self.question_number == 3:
            return render(request, 'q3.html')

    def get_q3_selected(self, request, selected: int):
        if self.api_method == "GET" and self.question_number == 3 and selected:
            for i in range(0, len(selected)+1, 2):
                self.dict_user[int(selected[i])-1] = 1
            return render(request, 'q3.html')

    def get_q3_search(self, request, search: str):
        if self.api_method == "GET" and self.question_number == 3 and search:
            search_result = []
            for i in [i for i in range(len(novel)) if str(search) in novel['제목'][i]]:
                idx_dict = {
                    'index' : i,
                    'image' : novel.loc[i,'썸네일'], 
                    'title' : novel.loc[i,'제목'],
                    'author': novel.loc[i,'작가'],
                    'genre' : novel.loc[i,'장르']
                }
                search_result.append(idx_dict)
            return render(request, 'q3.html', {'search_result' : search_result})
