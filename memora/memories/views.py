from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Memory

@login_required
def add_memory(request):
    if request.method == 'POST':
        Memory.objects.create(
            user=request.user,
            title=request.POST['title'],
            place=request.POST['place'],
            description=request.POST['description'],
            image=request.FILES['image'],
            is_public = 'is_public' in request.POST

        )
        return redirect('memory_list')


    return render(request, 'memories/add_memory.html')
@login_required
def memory_list(request):
    query = request.GET.get('q')

    if query:
        memories = Memory.objects.filter(
            user=request.user,
            place__icontains=query
        ).order_by('-created_at')
    else:
        memories = Memory.objects.filter(
            user=request.user
        ).order_by('-created_at')

    return render(
        request,
        'memories/memory_list.html',
        {
            'memories': memories,
            'query': query
        }
    )
def public_memories(request):
    query = request.GET.get('q')

    if query:
        memories = Memory.objects.filter(
            is_public=True,
            place__icontains=query
        ).order_by('-created_at')
    else:
        memories = Memory.objects.filter(
            is_public=True
        ).order_by('-created_at')

    return render(
        request,
        'memories/public_memories.html',
        {
            'memories': memories,
            'query': query
        }
    )


@login_required
def delete_memory(request, memory_id):
    memory = Memory.objects.get(id=memory_id, user=request.user)
    memory.delete()
    return redirect('memory_list')
