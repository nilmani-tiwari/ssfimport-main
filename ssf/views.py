from django.db.models.expressions import F
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
# from .models import Post
from ssf.models import *

class BlogListView(ListView):
    model =  project_details
    context_object_name = 'project_details'
    template_name = 'base1.html'
    count_hit = True

    

   


class BaseDetailView(HitCountDetailView):
    model =  project_details
    template_name = 'base1.html'
    context_object_name = 'project_details'
    #slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(BaseDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts':  project_details.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


def base2(request): 
    p_data=project_details.objects.filter(active=True).values().first()
    BlogPost.objects.filter(id=1).update(hit_count=F('hit_count')+1)
    


    return render(request,'base1.html' , p_data)
