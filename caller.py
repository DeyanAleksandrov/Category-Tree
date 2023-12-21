import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SecondCategoryTree.settings")
django.setup()

from SecondCategoryTree.categories.models import Category


def find_longest_path():
    categories = Category.objects.all()

    visited = set()
    longest_path = []

    def dfs(cur_category, path):
        nonlocal visited, longest_path

        if cur_category not in visited:

            visited.add(cur_category)
            path.append(cur_category)

            sub_categories = cur_category.sub_categories.all()

            if sub_categories:

                for sub_category in sub_categories:
                    dfs(sub_category, path[:])

            if len(path) > len(longest_path):
                longest_path = path

    for cur_category in categories:
        dfs(cur_category, [])

    return longest_path


longest_path = find_longest_path()

print("Longest Path")
for category in longest_path:
    print(category)

print()


def find_islands():
    categories = Category.objects.all()
    visited = set()
    islands = []

    def dfs(cur_category, island):
        nonlocal visited

        if cur_category not in visited:
            visited.add(cur_category)
            island.add(cur_category)

            sub_categories = cur_category.sub_categories.all()

            if sub_categories:
                for sub_category in sub_categories:
                    dfs(sub_category, island)

    for category in categories:
        if category not in visited:
            rabbit_island = set()
            dfs(category, rabbit_island)
            islands.append(rabbit_island)

    return islands


rabbit_islands = find_islands()

print('Rabbit Islands')
for index, island in enumerate(rabbit_islands, start=1):
    print(f'Island {index}')
    for category in island:
        print(category)
    print('____________')
