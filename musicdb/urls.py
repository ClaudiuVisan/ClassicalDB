from django.urls import path
from musicdb import views


urlpatterns = [
    path('', views.index, name='index'),
    path('composers/', views.view_composers, name='composers'),
    path('compositions/', views.view_compositions, name='compositions'),
    path('catalogues/', views.view_catalogues, name='catalogues'),

    path('composition/<int:id>', views.view_composer_compositions,
         name='composer_compositions'),
    path('catalogue/<int:id>', views.view_composer_catalogues,
         name='composer_catalogues'),

    path('composers/composer-add/', views.add_composer, name='add_composer'),
    path('composers/composer-delete/<int:id>', views.delete_composer,
         name='delete_composer'),
    path('composers/composer-edit/<int:id>', views.update_composer,
         name='update_composer'),

    path('compositions/composition-add/', views.add_composition,
         name='add_composition'),
    path('compositions/composition-delete/<int:id>', views.delete_composition,
         name='delete_composition'),
    path('compositions/composition-edit/<int:id>', views.update_composition,
         name='update_composition'),

    path('catalogues/catalogue-add/', views.add_catalogue,
         name='add_catalogue'),
    path('catalogues/catalogue-delete/<int:id>', views.delete_catalogue,
         name='delete_catalogue'),
    path('catalogues/catalogue-edit/<int:id>', views.update_catalogue,
         name='update_catalogue'),
]
