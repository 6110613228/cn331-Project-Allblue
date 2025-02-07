from recipes.views import add_comment
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
	path('view/menus/', views.menu_view, name = "menu"),
	path('addrecipe/', views.addrecipe_view, name = 'addrecipe'),
	path('view/recipe/<int:id>/', views.recipe_view, name='recipe_view'),
	path('view/recipe/voteup/<int:recipe_id>', views.voteUp_recipe ,name='voteup_recipe'),
	path('view/recipe/votedown/<int:recipe_id>', views.voteDown_recipe ,name='votedown_recipe'),
	path('addcomment/<int:recipe_id>', views.add_comment, name="addcomment"),
	path('view/myrecipe/<int:user_id>', views.view_my_recipes, name='myrecipe'),
	path('delete/<int:recipe_id>',views.deleteRecipe,name = 'delete'),
	path('view/menus/tag/<int:tag_id>', views.tag_show_recipes, name='tag'),
]
