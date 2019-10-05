from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.ShopUserListView.as_view(), name='index'),


    path('shopuser/create/', adminapp.shopuser_create,
         name='shopuser_create'),
    path('shopuser/update/<int:pk>)/', adminapp.shopuser_update,
         name='shopuser_update'),
    path('shopuser/delete/<int:pk>)/', adminapp.shopuser_delete,
         name='shopuser_delete'),


    path('productcategory/list/', adminapp.productcategory_list,
         name='productcategory_list'),
    path('productcategory/create/', adminapp.ProductCategoryCreateView.as_view(),
         name='productcategory_create'),
    path('productcategory/update/<int:pk>)/', adminapp.ProductCategoryUpdateView.as_view(),
         name='productcategory_update'),
    path('productcategory/delete/<int:pk>)/', adminapp.ProductCategoryDeleteView.as_view(),
         name='productcategory_delete'),
    path('productcategory/products/<int:pk>)/', adminapp.productcategory_products,
         name='productcategory_products'),


    path('product/create/<int:pk>)/', adminapp.product_create,
         name='product_create'),
    path('product/update/<int:pk>)/', adminapp.product_update,
         name='product_update'),
    path('product/delete/<int:pk>)/', adminapp.product_delete,
         name='product_delete'),
    path('product/read/<int:pk>)/', adminapp.ProductDetailView.as_view(),
         name='product_read'),

]
