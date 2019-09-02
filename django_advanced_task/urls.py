from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from stores.views import store_list
from inventories.views import inventory_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stores/', include('stores.urls', namespace='stores')),
    path('inventories/', include('inventories.urls', namespace='inventories')),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

