# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.project.stacksd import views

urlpatterns = patterns(
    '',
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^get_d3_data/(?P<stack_id>[^/]+)/$',
        views.JSONView.as_view(), name='d3_data'),
    url(r'^formI/(?P<str>[^/]+)/$',views.InstanceFormView.as_view(), name='formI'),
    url(r'^formD/(?P<str>[^/]+)/$',views.DatabaseFormView.as_view(), name='formD'),
    url(r'^formLB/(?P<str>[^/]+)/$',views.LoadBalancerFormView.as_view(), name='formLB'),
    url(r'^create/(?P<id>\d+)/$',views.ResourcesView.as_view(), name='create'),
    url(r'^del/(?P<str>[^/]+)/$',views.RemoveNode.as_view(), name='del'),
)
