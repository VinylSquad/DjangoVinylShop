from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

from django.conf.urls import handler404


urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', include('store.urls')),

    path('payment/', include('payment.urls')),
    
    path('cart/', include('cart.urls')),

    path('account/', include('account.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'store.views.error_404'