from django.conf.urls import include, url
from lost_and_found.views.sign_up import member_signup
from lost_and_found.views.log_in import member_login
from lost_and_found.views.update_user_info import update_user_info
from lost_and_found.views.get_user_info import get_user_info
from lost_and_found.views.check import  check
from lost_and_found.views.get_user_uploads import get_user_uploads
from lost_and_found.views.get_uploads import get_uploads
from lost_and_found.views.member_info import member_info
urlpatterns = [
    url(r'^signup/$', member_signup, name="signup"),
    url(r'^login/$', member_login, name="login"),
    url(r'^profile/$', get_user_info, name='user_info'),
    url(r'^member/(?P<username>\w+)/profile/update/$', update_user_info, name='profile_update'),
    url(r'^check/(?P<username>\w+)/(?P<item_name>\w+)/(?P<item_category>\w+)/upload/', check, name="check"),
    url(r'^(?P<username>\w+)/uploads/$',get_user_uploads,name='user_uploads'),
    url(r'^uploads/$',get_uploads,name='uploads'),
    url(r'^member/profile/info/$',member_info,name='member_info')
]