from django.shortcuts import render
from django.http import JsonResponse
from .models import Comic, AudioComic, Story

def comic_list(request):
    comics = Comic.objects.all()
    return JsonResponse({'comics': list(comics.values())})

def audio_comic_list(request):
    audio_comics = AudioComic.objects.all()
    return JsonResponse({'audio_comics': list(audio_comics.values())})

def story_list(request):
    stories = Story.objects.all()
    return JsonResponse({'stories': list(stories.values())})