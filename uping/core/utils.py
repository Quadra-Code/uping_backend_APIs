from .models import CategoriesTree
# Create your utils here.

def get_categories_tree_list(parents):
    data = []
    for parent in parents:
        obj = {}
        obj['id'] = parent.id
        obj['name'] = parent.name
        if parent.is_parent:
            obj['children'] = nested_loop(parent)
        data.append(obj)
    return data

def nested_loop(parent_obj):
    children_objs = []
    children = CategoriesTree.objects.filter(parent_fk=parent_obj.id).order_by('id')
    for child in children:
        obj = {
            'id':child.id,
            'name':child.name,
        }
        if child.is_parent:
            obj['children'] = nested_loop(child)
        children_objs.append(obj)
    return children_objs