from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    # 1. 브라우저에서 요청
    # 2. 요청이 runserver로 실행중인 서버에 도착
    # 3. runserver는 요청을 Django code로 전달
    # 4. Django code중 config.urls모듈이 해당 요청을 받음
    # 5. config.urls 모듈은 받은 요청의 URL과 일치하는 blog.urls모듈로 전달
    # 6. blog.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 열결된 함수(view)를 실행
    # 8. 함수의 실행함 결과(리턴값)을 브라우저로 다시 전달

    # Http 프로토토콜로 텍스트 데이터 응답을 반환
    # return HttpResponse('<html><body><h1>Post list</h1><p>post 목록을 보여줄 예정입니다.</p></body></html>')

    # posts = Post.objects.order_by('-created_date')
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # 위 return 코드와 같은 내용
    # return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    """
    localhost:8000/detail/ 로 온 요청을
    'blog/post_detail.html'을 render한 결과를 리턴
    :param request:
    :return:
    """
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)


def post_edit(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.title = request.POST['title']
        post.content = request.POST['content']
        if post.title and post.content:

            post.save()
            return redirect('post-detail', pk=post.pk)
        context['form_error'] = '제목과 내용을 입력해주세요.'
    return render(request, 'blog/post_add_edit.html', context)


def post_add(request):
    context = {}
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        # title이나 content가 비어있으면 아래까지 내려가서 오류 메시지 출력
        if title and content:
            # return HttpResponse(f'{title}: {content}') # 인자는 하나여야함
            post = Post.objects.create(
                author=request.user,
                title=title,
                content=content,
            )
            return redirect('post-detail', pk=post.pk)
            # return HttpResponse(f'{post.author}<br> {post.pk}<br> {post.title}<br> {post.content}')

            # render를 사용할 경우
            # context = {
            #     'post': post
            # }
            # return render(request, 'blog/post_detail.html', context)
        context['form_error'] = '제목과 내용을 입력해주세요.'
    return render(request, 'blog/post_add_edit.html', context)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        if request.user == post.author:
            post.delete()
            return redirect('post-list')
        return redirect('post-detail', pk=post.pk)
