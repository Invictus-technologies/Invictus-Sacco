from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^loan_dev/', views.loan_dev, name='loan_dev'),
    url(r'^loan_biz/', views.loan_biz, name='loan_biz'),
    url(r'^salary_adv/', views.salary_adv, name='salary_adv'),
    url(r'^biz_fix/', views.biz_fix, name='biz_fix'),
    url(r'^timiza/', views.timiza, name='timiza'),
    url(r'^jipange/', views.jipange, name='jipange'),
    url(r'^open_acc/', views.open_acc, name='open_acc'),
    url(r'^statuary/', views.statuary, name='statuary'),
    url(r'^investment/', views.investment, name='investment'),
    url(r'^sacco_dep/', views.sacco_dep, name='sacco_dep'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^member_reg/', views.member_regi, name='member_reg'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^member_portal/', views.member_portal, name='member_portal'),
    url(r'^accounts/', views.accounts, name='accounts'),
    url(r'^help/', views.help, name='help'),
    url(r'^loans/', views.loans, name='loans'),
    url(r'^savings/', views.savings, name='savings'),
    url(r'^invictusadmin/', views.invictusadmin, name='invictusadmin'),
    url(r'^invictusmembers/', views.invictusmembers, name='invictusmembers'),
    url(r'^invictusapprovemembers/', views.invictusapprovemembers, name='invictusapprovemembers'),

    ]