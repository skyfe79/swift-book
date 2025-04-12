import os
import glob

def inject_custom_styles():
    # documentation 폴더 내의 모든 HTML 파일 찾기
    html_files = glob.glob('docs/documentation/the-swift-programming-language/**/*.html', recursive=True)
    
    # 추가할 CSS 내용
    custom_styles = """
    <style>
    @font-face {
        font-family: 'RIDIBatang';
        src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/RIDIBatang.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }

    :root {
        --font-family-system: 'RIDIBatang', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    body {
        line-height: 180%;
    }
    </style>
    """

    # 각 HTML 파일에 스타일 추가
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # </head> 태그 바로 앞에 스타일 삽입
        if '</head>' in content:
            content = content.replace('</head>', f'{custom_styles}</head>')
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == '__main__':
    inject_custom_styles() 