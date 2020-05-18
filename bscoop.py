import tempfile
import webbrowser

class BeautifulScoop:

    def __init__(self):
        self.css = "<style></style>"
        self.base_url = ""

    def set_css(self, css, from_list = []):
        new_list = from_list or []
        new_list.append(css)
        print(['new list:', new_list])
        new_style = "".join([str(elem) for elem in new_list])
        self.css = new_style
        
    def set_base_url(self, base_url):
        self.base_url = f'<base href="{base_url}" target="_blank">'
        
    def display(self, elementOrString):
    
        tag = str(elementOrString)
            
        html = f'''
<!DOCTYPE html><html lang="en">
<head>
{self.base_url}
{self.css}
</head>
<body>
{tag}
</body></html>
'''

        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html',                                                        encoding='utf-8') as f:
            url = 'file://' + f.name
            f.write(html)
            
        webbrowser.open(url)

