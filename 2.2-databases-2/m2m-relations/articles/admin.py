from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        cnt = 0
        for form in self.forms:
            print(type(form.cleaned_data),form.cleaned_data)
            if form.cleaned_data.get('is_main'):
                cnt+=1
        if cnt != 1:
                raise ValidationError('Несколько основных или отсутствует вообще !!')
        return super().clean()  # вызываем базовый код переопределяемого метода

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass




