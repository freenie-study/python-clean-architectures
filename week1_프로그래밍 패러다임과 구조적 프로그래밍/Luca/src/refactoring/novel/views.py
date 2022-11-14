class NovelApi:
    def __init__(self, api_method: str) -> None:
        self.api_method = api_method
        self.cart_result = []
        
    def post_novel_list(self, request):
        if self.api_method == 'POST':
            rating = request.body('rating')
            novel_idx = request.body('novel_idx')
            idx_dict = {
                'index' : novel_idx,
                'image' : novel.loc[novel_idx,'썸네일'], 
                'title' : novel.loc[novel_idx,'제목'],
                'author': novel.loc[novel_idx,'작가'],
                'genre' : novel.loc[novel_idx,'장르'],
                'rating' : rating
            }
            self.cart_result.append(idx_dict)

        return redirect('q3')

    def get_novel_list(self, request):
        if self.api_method == 'GET':
            return render(request, 'novel_list.html', {'cart_result' : self.cart_result})

    def delete_novel(self, request):
        if self.api_method == 'DELETE':
            for i in range(len(self.cart_result)):
                if self.cart_result[i]['index'] == int(request.GET.get('novel_index_delete')):
                    del self.cart_result[i]
                    break
                
        return render(request, 'novel_list.html', {'cart_result' : self.cart_result})
    

