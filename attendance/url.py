from django.urls import path
from . import views

urlpatterns = [
    # admin paths
    path('', views.home , name='home'),
    path('index/', views.index , name='index'),
    path('login/',views.admin_login,name='login'),
    path('change_pw_admin/',views.change_pw_admin,name='change password'),
    path('manage_std/',views.manage_std,name='manage_student'),
    path('add_std/',views.add_std,name='add student'),
    path('add_std_multi/',views.add_std_multi,name='add student'),
    path('insert_std/',views.insert_std_sheet ,name='insert data'),
    path('edit_std/<int:id>',views.edit_std,name='edit student'),
    path('update_std/<int:id>',views.update_std,name='update student'),
    path('delete_std/<int:id>',views.delete_std,name='delete student'),
    
    path('manage_faculty/',views.manage_faculty,name='manage_faculty'),
    path('add_faculty/',views.add_faculty,name='add faculty'),
    path('edit_stf/<int:id>',views.edit_stf,name='edit faculty'),
    path('update_stf/<int:id>',views.update_stf,name='update faculty'),
    path('delete_faculty/<int:id>',views.delete_faculty,name='delete faculty'),
    path('add_faculty_multi/',views.add_stf_multi,name='add faculty multi'),
    path('insert_stf/',views.insert_stf_sheet ,name='insert data faculty'),

    path('manage_sub/',views.manage_sub,name='manage_subject'),
    path('add_sub/',views.add_sub ,name='add subject'),
    path('edit_sub/<int:id>',views.edit_sub,name='edit subject'),
    path('update_sub/<int:id>',views.update_sub,name='update subject'),
    path('delete_sub/<int:id>',views.delete_sub,name='delete subject'),

    path('manage_sem/',views.manage_sem,name='manage_semester'),
    path('add_sem/',views.add_sem ,name='add semester'),
    
    path('manage_att/',views.manage_att,name='manage_att'),
    path('add_att/',views.add_att ,name='add att'),
    path('insert/',views.insert_att_sheet ,name='insert data'),
    path('edit_att/<int:id>',views.edit_att,name='edit subject'),
    path('update_att/<int:id>',views.update_att,name='update subject'),
    path('delete_att/<int:id>',views.delete_att,name='delete attendance'),

    path('manage_complaint/',views.manage_complaint),
    path('reports/',views.reports),
    path('student_report/',views.student_report),
    path('faculty_report/',views.faculty_report),

    # student paths
    path('std_index/', views.std_index , name='stdindex'),
    path('std_login/',views.std_login,name='stdlogin'),
    path('std_profil/<int:id>',views.std_profile,name='student profile'),
    path('std_change_pw/',views.std_change_pw),
    path('s_forgot/',views.s_forgot),
    path('std_forgetpass/',views.std_forgetpass),
    path('std_resetpass/<str:em>',views.std_resetpass),
    path('std_index/complain/<int:id>',views.complain),
    path('std_index/complain/add_complaint/',views.add_complaint),
    path('std_index/view_att/<int:id>',views.view_att),

    # faculty paths
    path('stf_index/', views.stf_index , name='stfindex'),
    path('stf_login/',views.stf_login,name='stflogin'),
    path('stf_profil/<int:id>',views.stf_profil,name='staff profile'),
    path('stf_change_pw/',views.stf_change_pw),
    path('stf_index/manage_att_std/<int:id>',views.manage_att_std,name='attendance_subject_list'),
    path('stf_index/manage_att_std/mark_attendance/<int:id1>/<int:id2>',views.mark_attendance,name='attendance_list'),
    path('make_attendance/<int:semid>/<int:subid>',views.make_attendance,name='marking student attendance'),
    path('stf_index/my_lecs/<int:id>',views.my_lecs,name='faculty report'),
    path('stf_forgot/',views.stf_forgot),
    path('stf_forgetpass/',views.stf_forgetpass),
    path('stf_resetpass/<str:em>',views.stf_resetpass),
]