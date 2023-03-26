from django.contrib.auth.models import User 
from django.contrib import admin
from django.apps import AppConfig
from . models import *

# Register your models here.


# Here we try the inline classes to handle course - lesson relatioship
## This needs to be before the class CourseAdmin

class LessonInline(admin.StackedInline): 
    model = Lesson
    extra = 5


# We create a ModelAdmin class to add the field names we
# want to appear in case we do not want all fields to appear

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    # This is added for the course - lesson inline relationship
    inlines = [LessonInline]

# You need to update previous course registration
# to include CourseAdmin -- with no customization, use only 
# admin.site.register(Course)

admin.site.register(Course, CourseAdmin)

# Customize Instructor as well
class InstructorAdmin(admin.ModelAdmin):
    
    ##readonly_fields = ['user']    # to make a field read-only
    fields = ['user', 'full_time']

    ##readonly_fields = ['user', 'full_time'] To make a field read-only


admin.site.register(Instructor, InstructorAdmin)


## code snippet for changing the displayed fields based on the user
#class MyModelAdmin(admin.ModelAdmin):
#    list_display = ('A', 'B', 'C',)
#
#    def changelist_view(self, request, extra_context=None):
#        if not request.user.is_superuser:
#            self.list_display = ('B', 'C',)
#        return super(MyModelAdmin, self).changelist_view(request, extra_context)
