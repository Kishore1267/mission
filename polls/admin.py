from django.contrib import admin
from .models import Receipes,StudentID,Student,Department,Subject,SubjectMarks


admin.site.register(Receipes)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(SubjectMarks,SubjectMarkAdmin)