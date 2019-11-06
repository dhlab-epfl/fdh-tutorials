import matplotlib
import random
import pandas as pd

random.seed(2)

def gen_colors(n):
    ret = []
    if n < 12:
        cmap = matplotlib.cm.get_cmap('Set3')
        for i in range(cmap.N):
            rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
            ret.append(matplotlib.colors.rgb2hex(rgb))
        return ret
    r = int(random.random() * 256)
    g = int(random.random() * 256)
    b = int(random.random() * 256)
    step = 256 / n
    for i in range(n):
        r += step
        g += step
        b += step
        r = int(r) % 256
        g = int(g) % 256
        b = int(b) % 256
        ret.append('#%02x%02x%02x' % (r,g,b)) 
    return ret

def export_to_excel(df_annots, path, tags, colors = None):
    df_annots = df_annots.copy()
    if 'tag' not in df_annots:
        df_annots['tag'] = ''
    
    columns = df_annots.reset_index().columns.values.tolist()
    text_col_idx = columns.index('text')
    token_col_idx = columns.index('token')
    tag_col_idx = columns.index('tag')
    
    classes = set([t.split('-')[1] for t in tags if t != 'O'])
    if not colors:
        colors = gen_colors(len(classes))
    class2color = dict(zip(classes, colors))
    
    with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
        df_annots.to_excel(writer, sheet_name='Sheet1')
        worksheet = writer.sheets['Sheet1']
        workbook = writer.book
        
        for tag in tags:
            if tag == 'O':
                continue
            curr_format = workbook.add_format()
            class_ = tag.split('-')[1]
            curr_format.set_bg_color(class2color[class_])
            worksheet.conditional_format(1,tag_col_idx,len(df_annots),tag_col_idx,{
                'type': 'text',
                'criteria': 'containing',
                'value': tag,
                'format': curr_format
            })
        wrap_format = workbook.add_format()
        wrap_format.set_text_wrap()
        worksheet.set_column(text_col_idx,text_col_idx, 40, wrap_format)
        worksheet.set_column(token_col_idx,token_col_idx, 20)
        
        worksheet.data_validation(1,tag_col_idx,len(df_annots),tag_col_idx, {
            'validate': 'list',
            'source': tags
        })