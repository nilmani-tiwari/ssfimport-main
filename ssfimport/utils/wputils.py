import requests
from bs4 import BeautifulSoup, Comment
import logging
from wp.models import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def wp_content_processor(content, post_id=0, wp_id=False):
    # return content
    soup = BeautifulSoup(content, 'html.parser')

    if wp_id:
        _TG = f"[CONTENT PROCESSOR] [WP: {post_id}]"
    else:
        _TG = f"[CONTENT PROCESSOR] [BlogPost: {post_id}]"

    # Images
    try:
        images_blocks = soup.findAll("div", {"class": "wp-block-image"})
        images_blocks += soup.findAll("figure", {"class": "wp-block-image"})
        for image_block in images_blocks:
            images = image_block.find_all('img')
            for image in images:
                try:
                    image_post_id = image.get('class')[0].replace('wp-image-', '')
                    image_obj = WpAs3CfItems.objects.using('wp').get(source_id=image_post_id)
                    image_url = 'https://' + image_obj.bucket + '/' + image_obj.path
                    image['src'] = image_url
                    logger.info(f"{_TG} Image processing successful.")
                except:
                    logger.error(f"{_TG} Cannot process image: {image}")
    except:
        logger.error(f"{_TG} Something went wrong with processing image tags.")


    # Reusable Blocks
    try:
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            if 'wp:block' in comment:
                logger.info("Found WP Block: {}".format(comment))
                try:
                    block_id = int(comment.split('{"ref":')[1].split('}')[0])
                    block_html = WpPosts.objects.using('wp').filter(id=block_id).first().post_content
                    comment.replace_with(BeautifulSoup(block_html, 'html.parser'))
                except:
                    # print(1)
                    logger.error(f"{_TG} Invalid block: {comment}")
    except:
        logger.error(f"{_TG} Reusable Block Failed")
    # Buttons

    try:
        buttons = soup.find_all('a', class_='wp-block-button__link')
        for button in buttons:
            button['class'] = button.get('class', []) +['btn', 'btn-primary']
    except:
        logger.error(f"{_TG} Button Class Change Failed")

    # External Links
    try:
        links = soup.find_all('a')
        for link in links:
            if 'tickle.life' not in link.get('href', ''):
                link['target'] = '_blank'

        figures = soup.find_all('figure')
        logger.info("Found {} figures".format(len(list(figures))))
    except:
        logger.error(f"{_TG} Failed to add _blank to target for link")

    # Spotify
    # print("*" * 100)
    try:
        spotify_embeds = soup.find_all('figure', class_='is-provider-spotify')
        for embed in spotify_embeds:
            spotURL = embed.find('div')
            if spotURL:
                spotURL = spotURL.get_text().strip()
                if 'open.spotify' in spotURL:
                    r = requests.get("https://open.spotify.com/oembed?url={}".format(spotURL))
                    if r.status_code == 200:
                        frame_html = r.json().get('html')
                        frame = BeautifulSoup(frame_html, 'html.parser').find('iframe')
                        embed.string = ""
                        embed.append(frame)
                        # print(frame)
    except:
        logger.error(f"{_TG} Spotify Replace Failed")

    try:
        for figure in figures:
            if 'is-type-video' in figure.attrs.get('class', []):
                logger.info("Found figure_type=video")

                if 'is-provider-youtube' in figure.attrs.get('class', []):
                    logger.info("Found figure_type=video figure_provider=youtube")
                    innerDiv = figure.find('div')
                    if innerDiv:

                        ytURL = innerDiv.get_text()
                        logger.info("Found YouTubeURL={}".format(ytURL))

                        if '//youtu.be' in ytURL:
                            ytURL = ytURL.split('//youtu.be')[1].split('/')[1]
                        else:
                            ytURL = ytURL.split('?v=')[1].split('\r')[0].split('\n')[0].split('&')[0]
                        logger.info("Found Processed YouTubeURL={}".format(ytURL))

                        embed = soup.new_tag('iframe', width='100%', height='450px', src="https://www.youtube.com/embed/{}".format(ytURL),
                                     frameborder="0",
                                     allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture=",
                                     allowfullscreen='allowfullscreen')
                        innerDiv.parent.insert(0, embed)
                        innerDiv.decompose()
    except:
        logger.error(f"{_TG} YouTube Failed")
    return str(soup)