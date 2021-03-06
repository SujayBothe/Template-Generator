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

import logging

from django.utils.translation import ugettext_lazy as _

from horizon import messages
from horizon import tabs
from openstack_dashboard import api
from openstack_dashboard import policy

from openstack_dashboard.dashboards.project.stacksd \
    import api as project_api
#from openstack_dashboard.dashboards.project.stacks import mappings
#from openstack_dashboard.dashboards.project.stacks \
 #   import tables as project_tables


LOG = logging.getLogger(__name__)

class StackDesignerTab(tabs.Tab):
    name = _("Dsigner")
    slug = "designer"
    template_name = "project/stacksd/_designer.html"

    def get_context_data(self, request):
        context = {}
        #stack = self.tab_group.kwargs['stack']
        context['stack_id'] = "e75ea590-dcc0-4989-8550-87d206b21979"
        context['d3_data'] = project_api.d3_dataa(stack_id="e75ea590-dcc0-4989-8550-87d206b21979")
        return context
    #def get_context_data(self, request):
       # context = {}
        #stack = self.tab_group.kwargs['stack']
        #context['stack_id'] = stack.id
        #context['d3_data'] = project_api.d3_data(request, stack_id=stack.id)
        #return context

class TemplateTab(tabs.Tab):
    name = _("Templates")
    slug = "templates"
    template_name = "project/stacksd/_templates.html"
    preload = False

class StacksdTabs(tabs.TabGroup):
    slug = "stack_details"
    tabs = (StackDesignerTab, TemplateTab)
    sticky = True


