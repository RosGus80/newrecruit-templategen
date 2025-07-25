#!/usr/bin/env python3

def main():
    import argparse
    import os
    from servogen.parse import render_html

    parser = argparse.ArgumentParser(
        prog='servogen',
        description='Tool for converting your New Recruit JSON rosters into readable '
                    'and navigable HTML pages – more elegant than New Recruit\'s own export! '
                    'Use -r flag to specify input JSON file. Use -o to specify output HTML file. '
                    'If no -o is provided, output will be saved next to input file with .html extension. '
                    'Use -c to enable collapsible sections.',
        usage='servogen -r roster.json [-o output.html] [--collapsible]'
    )

    parser.add_argument(
        '-r', '--render',
        metavar='INPUT',
        required=True,
        help='Path to the New Recruit JSON file to render into HTML.'
    )

    parser.add_argument(
        '-o', '--output',
        metavar='OUTPUT',
        help='Path to output HTML file. If selected, saved next to input with .html extension.'
    )

    parser.add_argument(
        '-c', '--collapsible',
        action='store_true',
        help='Enable collapsible sections for unit rules and abilities.'
    )

    args = parser.parse_args()

    input_path = args.render
    if args.output:
        output_path = args.output
    else:
        input_dir = os.path.dirname(input_path)
        input_basename = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(input_dir, input_basename + ".html")

    render_html(input_path, output_path, collapse=args.collapsible)


if __name__ == '__main__':
    main()
