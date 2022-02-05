import time

from django.views.generic import TemplateView

from ssftemp.models import *


class PlanView(TemplateView):
    template_name = "plan.csv"

    def get(self, request, plan_id=0):

        context = self.get_context_data()
        subs = SubscribedUser.objects.filter(sub_plan_map_s__plan_id=plan_id, sub_plan_map_s__exp_date__gte=time.time())
        # id, username, email, first_name, last_name, nickname, display_name, joined, biographical_info, website
        # 1, reputeinfosystems, reputeinfosystems @ example.com, Repute, InfoSystems, reputeinfo, "Repute InfoSystems", "2016-08-01 16:08:01", " ", " "
        data = []
        i = 0
        for sub in subs:
            subscription = SubscribedUserPlanMapping.objects.filter(subscriber=sub).order_by('exp_date').last()
            data.append(
             [
                 i,
                 sub.username,
                 sub.email,
                 sub.fname,
                 sub.lname,
                 sub.username,
                 sub.username,
                 f"\"{datetime.utcfromtimestamp(subscription.exp_date).strftime('%Y-%m-%d %H:%M:%S')}\"",
                 '',
                 '',
                 sub.pwd
             ]
            )
            i += 1


        context['data'] = data


        return self.render_to_response(context)