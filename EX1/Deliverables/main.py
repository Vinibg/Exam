import yaml
import argparse
import sys
import os
from mailmerge import MailMerge

def setup_arg_parser():
    """Sets up and parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate documents from a YAML config and a Word template."
    )
    parser.add_argument(
        '-c', '--config',
        metavar='CONFIG_FILE',
        required=True,
        help='YAML configuration file to be read (required).'
    )
    parser.add_argument(
        '-t', '--template',
        metavar='TEMPLATE_FILE',
        required=True,
        help='MailMerge template file (.docx) (required).'
    )
    parser.add_argument(
        '-o', '--output',
        metavar='OUTPUT_DIR',
        default='.',
        help='Output directory to save generated files (defaults to current directory).'
    )
    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Enable debug mode for verbose output.'
    )
    return parser.parse_args()

def log_debug(message, is_debug_mode):
    if is_debug_mode:
        print(f"[DEBUG] {message}")

def load_yaml_config(filepath, is_debug_mode):
    log_debug(f"Attempting to load YAML from {filepath}", is_debug_mode)
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: The configuration file '{filepath}' was not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Could not parse the YAML file '{filepath}'.\n{e}")
        sys.exit(1)

def create_document(template_path, context, output_path, is_debug_mode):
    log_debug(f"Generating document: {output_path}", is_debug_mode)
    log_debug(f"Using context: {context}", is_debug_mode)
    try:
        doc = MailMerge(template_path)
        doc.merge(**context)
        doc.write(output_path)
        doc.close()
        return True
    except Exception as e:
        print(f"Error: Failed to create document '{output_path}'.\n{e}")
        return False

def main():
    args = setup_arg_parser()
    log_debug(f"Arguments parsed: {args}", args.debug)

    data = load_yaml_config(args.config, args.debug)
    if not data or 'bands' not in data:
        print("Error: YAML file is empty or does not contain a 'bands' key.")
        sys.exit(1)

    bands = data['bands']
    total_bands = len(bands)
    success_count = 0

    for band in bands:
        band_name = band.get('name', 'Untitled')
        log_debug(f"Processing entry for band: {band_name}", args.debug)

        musics = band.get('musics', [])
        context = {
            'BN': band.get('initials'),
            'Band': band_name,
            'Genre': band.get('genre'),
            'Members': band.get('members'),
            'About': band.get('about'),
            'Music1': musics[0].get('name') if len(musics) > 0 else None,
            'Album1': musics[0].get('album') if len(musics) > 0 else None,
            'Music2': musics[1].get('name') if len(musics) > 1 else None,
            'Album2': musics[1].get('album') if len(musics) > 1 else None,
            'Music3': musics[2].get('name') if len(musics) > 2 else None,
            'Album3': musics[2].get('album') if len(musics) > 2 else None,
        }

        filename = f"{band_name}.docx"
        output_path = os.path.join(args.output, filename)
        
        if create_document(args.template, context, output_path, args.debug):
            success_count += 1
    
    print(f"\nProcess finished. {success_count} of {total_bands} documents generated successfully.")

if __name__ == "__main__":
    main()
