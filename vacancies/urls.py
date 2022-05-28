"""GB_concept URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from cvs.views import CVList, CVCreate, CVUpdate, CVDelete, CVDistribute
from news.views import NewsCreate, NewsUpdate, NewsDelete, NewsModerateList
from vacancies.views import VacancyList, VacancyCreate, VacancyUpdate, VacancyDelete, VacancyDistribute

app_name = 'vacancy'

urlpatterns = [
    path('all/', VacancyList.as_view(), name='vacancy_list'),
    path('create/', VacancyCreate.as_view(), name='create_vacancy'),
    path('update/<int:pk>/', VacancyUpdate.as_view(), name='update_vacancy'),
    path('delete/<int:pk>/', VacancyDelete.as_view(), name='delete_vacancy'),
    path('distribute/<int:pk>/', VacancyDistribute.as_view(), name='distribute_vacancy'),

]
