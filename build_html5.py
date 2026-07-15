import json
REC=json.load(open('records5.json'))
TPL=open('template_body.html').read()
body=TPL.replace('__REC__', json.dumps(REC, ensure_ascii=False))
open('입시결과_학교_전형_학과별.html','w').write(body)
print('written chars', len(body))
