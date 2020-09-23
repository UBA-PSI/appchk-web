#!/usr/bin/env python3

import common_lib as mylib
import lib_html as HTML
import index_categories  # enum_all_categories


def process(per_page=60):
    print('generating html: category-index ...')
    base = mylib.path_out('category')
    parent = 'All Categories'
    arr = []
    for cid, cat, apps in sorted(index_categories.enum_all_categories(),
                                 key=lambda x: x[1].lower()):
        arr.append((cid, cat))
        pre = HTML.h2(HTML.a_path([(parent, '../')], cat))
        _, a = HTML.write_app_pages(mylib.path_add(base, cid), apps, cat,
                                    per_page, pre=pre)
        print('  {} ({})'.format(cat, a))

    src = ''.join([HTML.a(n, '{}/'.format(cid)) for cid, n in arr])
    HTML.write(base, '''
<h2>{}</h2>
<div class="tags large center">
  {}
</div>'''.format(parent, src), parent)
    print('')


if __name__ == '__main__':
    process()
