from django.urls import path


from core.homepage.views import IndexView

urlpatterns = [
    # homepage urls
    path('', IndexView.as_view(), name='index')
]