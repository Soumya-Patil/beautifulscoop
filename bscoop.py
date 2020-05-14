import tempfile
import webbrowser

class BeautifulScoop:

    def __init__(self):
        self.css = "<style></style>"

    def set_css(self, css):
        self.css = css
        
    def display(self, elementOrString):
    
        tag = str(elementOrString)
            
        html = f'''
<!DOCTYPE html><html lang="en">
<head>
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

