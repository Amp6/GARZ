from typing import Dict
from django import template

register = template.Library()


@register.inclusion_tag('webpack.html', takes_context=False)
def lazy_render_bundle(bundle: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    return {'bundle': bundle}
