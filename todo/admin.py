from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from todo.models import TODO


@admin.register(TODO)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'details', 'user', 'favorite', 'pub_date']

    readonly_fields = ('user', 'pub_date',)

    list_filter = ('user', ('pub_date', DateFieldListFilter))

    search_fields = ('title', 'id',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user = request.user

        super().save_model(request, obj, form, change)
