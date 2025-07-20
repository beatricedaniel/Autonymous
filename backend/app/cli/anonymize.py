# cli/anonymize.py
import os
import subprocess
import click

@click.command()
@click.option('--input', 'input_path', required=True, help='Path to DOCX file')
@click.option('--out-dir', required=True, help='Directory for outputs')
def anonymize(input_path, out_dir):
    """
    1) Convert DOCX → MD via Pandoc
    2) Detect & classify NER
    3) Write report.xlsx
    4) Redact MD & export PDF
    """
    click.echo(f"Processing {input_path} → {out_dir}")
    # TODO: implement:
    #    - subprocess.run(['pandoc', input_path, '-t', 'markdown', '-o', md_path])
    #    - NER pipeline…
    ...

if __name__ == '__main__':
    anonymize()
