import os

def run_cmd(cmd):
    proc = os.popen(cmd)
    output = ''.join(proc.readlines())
    proc.close()
    return output

def get_support_styles():
    output = run_cmd('rougify help style')
    lines = output.split('\n')
    index = 0
    for line in lines:
        index += 1
        if line == 'available themes:':
            break
    styles = lines[index].strip().split(', ')
    return styles

def clear_history():
    if os.path.exists('dist'):
        run_cmd('rm -rf dist')

    os.mkdir('dist')

if __name__ == '__main__':
    clear_history()
    styles = get_support_styles()
    for style in styles:
        print(style)
        run_cmd('rougify style %s > dist/%s.css' % (style, style))
