import pypdf, tqdm, argparse, os


def resize_pdf_pages(input_filename, target_width, target_height, output_filename):

    # Convert target dimensions from inches to points
    target_width = target_width * 72
    target_height = target_height * 72

    # Open the input PDF file
    input_pdf = pypdf.PdfReader(open(input_filename, "rb"))

    # Create a new PDF file
    with pypdf.PdfWriter(open(output_filename, "wb")) as output_pdf:

        # Iterate through each page in the input PDF
        for page_num in tqdm.trange(
            len(input_pdf.pages),
            ascii="○◕●",
            desc="Resizing Progress",
            bar_format="{l_bar}{bar:18}| [Elapsed: {elapsed} ETA: {remaining}]",
            leave=False,
        ):

            page = input_pdf.pages[page_num]

            # Calculate the current page dimensions
            current_width = float(page.mediabox.width)
            current_height = float(page.mediabox.height)

            if current_width > current_height:
                o_tb = page.trimbox
                scale_by = target_width / current_width

                page.scale_by(scale_by)
                page.trimbox = o_tb
                temp_blank = pypdf._page.PageObject.create_blank_page(None, target_width, target_height)

                temp_blank.merge_page(page)
                tmh = temp_blank.mediabox.height
                pmh = page.mediabox.height

                temp_blank.add_transformation(pypdf.Transformation().translate(0, (tmh - pmh) / 2))
                page = temp_blank
            else:
                width_scale = target_width / current_width
                height_scale = target_height / current_height
                page.scale(float(width_scale), float(height_scale))

            output_pdf.add_page(page)


def get_args():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--help", action="help", default=argparse.SUPPRESS, help="Show this help message and exit")
    ap.add_argument("-w", type=float, help="The desired output width, in inches", metavar="HEIGHT”", default=8.5)
    ap.add_argument("-h", type=float, help="The desired output height, in inches", metavar="WIDTH”", default=11)
    ap.add_argument("input_path", help="The path to the input pdf", metavar="path/to/input.pdf")
    ap.add_argument("output_path", help="The path to the output pdf", metavar="path/to/output.pdf")

    parsed_args = ap.parse_args()
    args_dict = vars(parsed_args)

    assert os.path.exists(
        args_dict["input_path"]
    ), f"The input path \"{args_dict['input_path']}\" could not be found. Are you in the correct working directory?"
    assert os.path.exists(
        args_dict["output_path"]
    ), f"The output path \"{args_dict['output_path']}\" could not be found. Are you in the correct working directory?"

    return args_dict


if __name__ == "__main__":
    args = get_args()
    resize_pdf_pages(args["input_path"], args["w"], args["h"], args["output_path"])
