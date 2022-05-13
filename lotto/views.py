from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all() # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    # 브라우저로부터 넘어온 request를 그대로 template('default.html')에게 전달
    # {} 에는 추가로 함께 전달하려는 object들을 dict로 넣어줄 수 있음
    return render(request, 'lotto/default.html', {"lottos":lottos})

def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST) # 채워진 양식

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate() # <- self.save()

            return redirect('index')

        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_test)
        # row.generate() # self.save()

        # print('\n\n\n===========================\n\n\n')
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print('\n\n\n===========================\n\n\n')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

    # print(request.POST['csrfmiddlewaretoken'])
    # -> wEwyS248wYqzma1wpsXO7WNX7ITtjWatYBzPwTMhItwEUKPF4QetwaE3uDWHGW5j

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
    return render(request, "lotto/detail.html", {"lotto": lotto})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")
