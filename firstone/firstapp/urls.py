
from django.urls import path
from .import views
urlpatterns = [
   path('',views.all,name="allfirst"),
   path('<int:chai_id>/',views.details,name="chaidetails"),
   path('chaistores/',views.chai_store,name='stores')
]