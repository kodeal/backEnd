from django.shortcuts import render

import openai

# OpenAI API 키, 항상 비워놓고 push하기
openai.api_key = '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'
openai.Engine.list()


# main page
def index(request):
    return render(request, 'home.html')


# qna
def qna_answer(request):
    return render(request, 'common/qna_answer.html')


# qna action
def qna_main(request):
    if request.method == 'POST':
        user_code = request.POST['code_area']  # 코드 영역
        user_text = request.POST['text_area']  # 질문 영역
        # codex 변환 과정
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=user_text,
            temperature=0,
            max_tokens=128,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\"\"\""],
        )
        return render(request, 'common/qna_answer.html', {'response': response})
    else:
        return render(request, 'common/qna_main.html')


# common page
def login_main(request):
    return render(request, 'common/login_main.html')

