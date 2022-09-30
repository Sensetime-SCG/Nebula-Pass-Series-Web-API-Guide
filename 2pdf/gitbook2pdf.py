import sys
from gitbook2pdf import Gitbook2PDF


def print_help_info(self_name: str, param: str) -> bool:
    if param == "-h" or \
            param == "-H" or \
            param == "-help" or \
            param == "--help":
        print("Usage: {} [url]".format(self_name))
        return True
    return False

if __name__ == '__main__':

    default_url = "http://127.0.0.1:4000"

    if len(sys.argv) == 1:
        url = default_url
        print("Not specify url, will use default url: " + default_url)
    else:
        if print_help_info(sys.argv[0], sys.argv[1]):
            exit(0)
        url = sys.argv[1]
    Gitbook2PDF(url).run()
