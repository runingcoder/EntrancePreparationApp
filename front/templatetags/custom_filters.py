from django import template

register = template.Library()

@register.filter
def sort_results(results):
    valued_dates = []
    unknown_dates = []

    for result in results:
        if result.date_attempted:
            valued_dates.append(result)
        else:
            unknown_dates.append(result)

    return valued_dates + unknown_dates
