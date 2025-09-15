from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemahalls_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

cinemahalls_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("cinemahalls/", cinemahalls_list, name="cinemahall-list"),
    path("cinemahalls/<int:pk>/",
         cinemahalls_detail,
         name="cinemahall-detail"),
    path("", include(router.urls))

]

app_name = "cinema"
