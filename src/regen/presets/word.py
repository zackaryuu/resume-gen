import os
import click
from regen.utils import build_input_md
    
captures = ["output.docx"]

def run(profile, data):
    build_input_md(data)
    click.echo("Input file created: input.md")
    os.system(
        f'pandoc input.md -o output.docx '
        f'-f markdown -t docx '
        f'--reference-doc="{os.path.join(profile, "template.dotx")}"'
    )
    click.echo("Output file created: output.docx") 