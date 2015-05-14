from django import template, conf

register = template.Library()

@register.simple_tag
def raw_include(path):
    import os.path

    for template_dir in conf.settings.TEMPLATE_DIRS:
        filepath = '%s/%s' % (template_dir, path)
        if os.path.isfile(filepath):
            break

    fp = open(filepath, 'r')
    output = fp.read()
    fp.close()
    return output