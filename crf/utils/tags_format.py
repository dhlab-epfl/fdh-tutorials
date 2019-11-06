def iob2_to_io(tags):
    out = []
    for tag in tags:
        out.append(tag.replace('B', 'I'))
    return out

def iob_to_io(tags):
    out = []
    for tag in tags:
        out.append(tag.replace('B', 'I'))
    return out

def iob_to_iob2(tags):
    out = []
    for i, tag in enumerate(tags):
        if tag[0] == 'I':
            if i + 1 < len(tags) and tags[i + 1][0] == 'I':
                out.append(tag)
            else:
                out.append('B' + tag[1:])
        else:
            out.append(tag)
    return out

def iob2_to_iob(tags):
    out = []
    for i, tag in enumerate(tags):
        if tag[0] == 'B':
            if i + 1 < len(tags) and tags[i + 1][0] == 'I':
                out.append(tag)
            else:
                out.append('I' + tag[1:])
        else:
            out.append(tag)
    return out


def biluo_to_iob2(tags):
    out = []
    for tag in tags:
        if tag[0] == 'U':
            out.append('B' + tag[1:])
        elif tag[0] == 'L':
            out.append('I' + tag[1:])
        else:
            out.append(tag)
    return out

def iob2_to_biluo(tags):
    out = []
    for i, tag in enumerate(tags):
        if tag == 'O':
            out.append(tag)
        elif tag[0] == 'B':
            if i + 1 < len(tags) and tags[i + 1][0] == "I":
                out.append(tag)
            else:
                out.append('U' + tag[1:])
        else:
            if i + 1 < len(tags) and tags[i + 1][0] == 'I':
                out.append(tag)
            else:
                out.append('L' + tag[1:])
    return out

def biluo_to_bioes(tag):
    out = []
    for tag in tags:
        if tag[0] == 'U':
            out.append('S' + tag[1:])
        elif tag[0] == 'L':
            out.append('E' + tag[1:])
        else:
            out.append(tag)
    return out

def bioes_to_biluo(tag):
    out = []
    for tag in tags:
        if tag[0] == 'S':
            out.append('U' + tag[1:])
        elif tag[0] == 'E':
            out.append('L' + tag[1:])
        else:
            out.append(tag)
    return out

def iob_to_biluo(tags):
    return iob2_to_biluo(iob_to_iob2(tags))

def biluo_to_iob(tags):
    return iob_to_iob2(biluo_to_iob2(tags))