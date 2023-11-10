from django.contrib import admin
from .models.project import Project
from .models.skill import Skill
from .models.technology import Technology


class ProjectAdmin(admin.ModelAdmin):
    """
    add list of skill and technology to affect to projects
    """
    filter_horizontal = ('skill', 'technology')
    list_display = ('title', 'url_github')

class SkillAdmin(admin.ModelAdmin):
    """
    used to modify display of the skill table in the django admin console
    """
    list_display = ('name', 'description')

class TechnologyAdmin(admin.ModelAdmin):
    """
    used to modify display of the technology table in the django admin console
    """
    list_display = ('name','description',)

"""
tables to include in django administration page
"""
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Technology, TechnologyAdmin)
