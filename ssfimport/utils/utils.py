import pdb

from django.conf import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_srcset_str(url, webp=False, sizes=[1440, 1024, 960, 640, 500, 320]):
    protocol = 'https' if 'https://' in url else 'http'
    webp = 'webp/' if webp else ''
    srcset = []
    host = settings.CDN_BASE_URL

    if host in url:
        key = url.split(host)[1]
        for size in sizes:
            srcset.append(f"{protocol}://{host}/{webp}{size}x0{key} {size}w")

        if len(srcset) > 0:
            srcset_return = ", ".join(srcset)
        logger.info(srcset_return)

    return srcset_return


# <img src="small.jpg"
#      srcset="large.jpg 1024w, medium.jpg 640w, small.jpg 320w"
#      sizes="100vw"
#      alt="A rad wolf" />
#
def process_tlcode(tlcode):
    try:
        tlcode = tlcode.split('_')
        user_id = int(tlcode[0])
        user_id = int((user_id / 5432) ** (1. / 2.))

        campaign_id = int(tlcode[1])
        return user_id, campaign_id
    except:
        return 0, 0

def get_tlcode(user_id, campaign_id):
    code = user_id * user_id * 5432
    return f"{code}_{campaign_id}"

def append_tlcode(link, campaign_id, user_id):
    user_id = int(user_id)
    tlcode = get_tlcode(user_id, campaign_id)
    if '?' in link:
        link += f"&tlcode={tlcode}"
    else:
        link += f"?tlcode={tlcode}"

    return link

def get_json_from_request(request):
    output = {}
    keep_keys = ["REMOTE_HOST", "REQUEST_METHOD", "PATH_INFO", "QUERY_STRING", "REMOTE_ADDR", "HTTP_HOST",
                 "HTTP_USER_AGENT", "HTTP_REFERER", "HTTP_X_FORWARDED_FOR"]
    for key in keep_keys:
        output[key] = request.META.get(key, '')
    return output

def datetime_str(datetime, format="default"):

    if format == "rss":
        return datetime.strftime("%a, %e %b %Y %H:%M:%S +0000")

    return datetime.strftime("%m/%d/%Y, %H:%M:%S")


def get_utm_link(link, source=None, medium=None, campaign=None):

    sep = '?'
    if '?' in link:
        sep = '&'

    if source:
        link += f"{sep}utm_source={source}"
        sep = '&'

    if medium:
        link += f"{sep}utm_source={medium}"
        sep = '&'

    if campaign:
        link += f"{sep}utm_source={campaign}"
        sep = '&'

    return link


def get_srcset_str(url, webp=False, sizes=[1440, 1024, 960, 640, 500, 320]):
    protocol = 'https' if 'https://' in url else 'http'
    webp = 'webp/' if webp else ''
    srcset = []
    host = settings.CDN_BASE_URL
    srcset_return = url

    if host in url:
        key = url.split(host)[1]
        for size in sizes:
            srcset.append(f"{protocol}://{host}/{webp}{size}x0{key} {size}w")

        if len(srcset) > 0:
            srcset_return = ", ".join(srcset)
        # logger.info(srcset_return)
        return srcset_return

    host = settings.WP_CDN_URL.replace('https://', '')

    if host in url:
        key = url.split(host)[1]
        for size in sizes:
            srcset.append(f"{protocol}://{host}{webp}{size}x0/{key} {size}w")

        if len(srcset) > 0:
            srcset_return = ", ".join(srcset)
        # logger.info(srcset_return)
        return srcset_return

    return srcset_return

def get_square_image_func(url, size=1440):
    protocol = 'https' if 'https://' in url else 'http'
    host = settings.CDN_BASE_URL
    srcset_return = url

    if host in url:
        key = url.split(host)[1]
        return f"{protocol}://{host}/{size}x{size}{key}"

    host = settings.WP_CDN_URL.replace('https://', '')

    if host in url:
        key = url.split(host)[1]
        return f"{protocol}://{host}{size}x{size}/{key}"

    return url

def get_custom_image_func(url, size="1440x0"):
    protocol = 'https' if 'https://' in url else 'http'
    host = settings.CDN_BASE_URL
    srcset_return = url

    if host in url:
        key = url.split(host)[1]
        return f"{protocol}://{host}/{size}{key}"

    host = settings.WP_CDN_URL.replace('https://', '')

    if host in url:
        key = url.split(host)[1]
        return f"{protocol}://{host}{size}/{key}"

    return url

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))