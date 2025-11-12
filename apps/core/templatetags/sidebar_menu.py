from django import template

register = template.Library()

@register.simple_tag
def create_menu(user):
    menu_items = [
        {'label': 'Pembukuan', 'url': 'ledger:ledger_index', 'icon': 'fas fa-tachometer-alt'},
        {'label': 'Post Media', 'url': 'post_media:post_media_home', 'icon': 'fas fa-share-alt'},
        {'label': 'Leads', 'url': 'leads:lead_list', 'icon': 'fas fa-list'},
        {'label': 'Ideas', 'url': 'lean:idea_list', 'icon': 'fas fa-lightbulb'},
    ]

    # Tambah menu admin kalau superuser atau owner
    if user.is_superuser or user.groups.filter(name='Owner').exists():
        menu_items.append({'label': 'Admin', 'url': 'admin:index', 'icon': 'fas fa-cog'})

    return menu_items


@register.filter
def is_owner(user):
    return user.groups.filter(name='Owner').exists()


@register.filter
def is_employee(user):
    return hasattr(user, 'is_employee') and user.is_employee()


@register.filter
def is_active(current_url, match):
    """Tandai menu aktif di template"""
    return 'active' if match in current_url else ''
