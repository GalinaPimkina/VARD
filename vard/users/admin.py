from django.contrib import admin
from .models import User, File

admin.site.register(User)
admin.site.register(File)

# from django.contrib import admin
# from .models import Access, AccessType, Files, FilesType, Place, Dushboards, Charts, Feedback, Comments, ReadComments
#
#
# @admin.register(Access)
# class AccessAdmin(admin.ModelAdmin):
#     list_display = ['user_id__username', 'access_type_id__access_type', 'date_access_open', 'date_access_close']
#     search_fields = ['user_id__username', 'access_type_id__access_type']
#
#
# @admin.register(AccessType)
# class AccessTypeAdmin(admin.ModelAdmin):
#     list_display = ['access_type', ]
#     search_fields = ['access_type', ]
#
#
# @admin.register(Files)
# class FilesAdmin(admin.ModelAdmin):
#     list_display = ['name', 'type_id__files_type', 'place_id__type', 'user_id__username', 'date_creation', 'publish']
#     search_fields = ['name', 'type_id__files_type', 'place_id__type']
#
#
# @admin.register(FilesType)
# class FilesTypeAdmin(admin.ModelAdmin):
#     list_display = ['files_type', ]
#     search_fields = ['files_type', ]
#
#
# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ['type', ]
#     search_fields = ['type', ]
#
#
# @admin.register(Dushboards)
# class DushboardsAdmin(admin.ModelAdmin):
#     list_display = ['user_id__username', 'date_creation', 'date_change']
#     search_fields = ['user_id__username']
#
#
# @admin.register(Charts)
# class ChartsAdmin(admin.ModelAdmin):
#     list_display = ['user_id__username', 'date_creation', 'date_change']
#     search_fields = ['user_id__username']
#
#
# @admin.register(Feedback)
# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ['user_id__username', 'date_creation']
#     search_fields = ['user_id__username']
#
#
# @admin.register(Comments)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ['user_id__username', 'date_send', 'date_delivery']
#     search_fields = ['user_id__username', ]
#
#
# @admin.register(ReadComments)
# class ReadCommentsAdmin(admin.ModelAdmin):
#     list_display = ['user_id__username', 'date_reading']
#     search_fields = ['user_id__username', ]
