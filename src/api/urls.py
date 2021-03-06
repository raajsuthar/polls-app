from django.urls import include, path
from rest_framework import routers
from  .views import UserViewSet, GroupViewSet,QuestionViewSet,ChoiceViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices' ,ChoiceViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]