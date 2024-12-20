from django import template
from django.utils.timezone import now, is_aware, make_aware

register = template.Library()

@register.filter
def is_time(todo_obj):
    current_time = now()  
    
    if not is_aware(todo_obj.cron):
        todo_obj.cron = make_aware(todo_obj.cron)

    if todo_obj.cron > current_time and not todo_obj.status:
        time_difference = todo_obj.cron - current_time
        return time_difference.total_seconds() < 86400 
    else:
        return False
