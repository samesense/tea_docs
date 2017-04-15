import os

files = [x.split('.')[0]
         for x in os.listdir('../../md/')]

rule md_to_html:
    input:  '../../md/{afile}.md'
    output: '../../html/{afile}.html'
    shell:  'pandoc -t html {input} > {output}'

rule all:
    input: expand('../../html/{afile}.html', afile=files)
