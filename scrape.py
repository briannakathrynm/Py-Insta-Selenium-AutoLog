import re
import time
import urllib


def recent_post_links(driver, username, post_count):
    """
    With the input of an account page, scrape posts

    Args:
    username: Instagram username
    post_count: Set as many or as few as you want

    Returns:
    A list with the unique url links for the most recent posts for the provided user
    """
    url = "https://www.instagram.com/" + username + "/"
    driver.get(url)
    print(url)
    post = 'https://www.instagram.com/p/'
    post_links = []
    print("Getting Links...")
    while len(post_links) < post_count:
        links = [a.get_attribute('href')
                 for a in driver.find_elements_by_tag_name("a")]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(scroll_down)
        time.sleep(10)
    else:
        driver.stop_client()
        return post_links[:post_count]


def find_mentions(comment):
    """
    Find mentions used in comments

    Args:
    comment: comments from specified Instagram post

    Returns:
    Mentions, if found in comment
    """
    print("Searching for Mentions...")
    mentions = re.findall('@[A-Za-z]+', comment)
    if (len(mentions) > 1) & (len(mentions) != 1):
        return mentions
    elif len(mentions) == 1:
        return mentions[0]
    else:
        return ""


def find_hashtags(comment):
    """
    Find hashtags used in comments

    Args:
    comment: comment from Instagram

    Returns:
    List or individual hashtags if found in comment
    """
    print("Searching for Hashtags...")
    hashtags = re.findall('#[A-Za-z]+', comment)
    if (len(hashtags) > 1) & (len(hashtags) != 1):
        return hashtags
    elif len(hashtags) == 1:
        return hashtags[0]
    else:
        return ""


def insta_details(driver, url):
    """
    Take a post url and return post details

    Args:
    Takes the URL used in login.py and the post links found in recent_post_links

    Returns:
    A list of dictionaries with details for each Instagram post, including link,
    post type, and like/view count, comments, hashtags, and mentions
    """
    driver.get(url)
    try:
        # Gets the like count for a photo
        likes = driver.find_element_by_xpath(
            """//*[@id="react-root"]/section/main/div/div/article/div[3]/section[2]/div/div/button""").text.split()[0]

        post_type = 'photo'
    except:
        # Gets the views for a video
        likes = driver.find_element_by_xpath(
            """//*[@id="react-root"]/section/main/div/div/article/div[3]/section[2]/div/span""").text.split()[0]
        post_type = 'video'
    age = driver.find_element_by_css_selector('a time').text
    print("Finding Comments...")
    comment = driver.find_element_by_xpath("""
    //*[@id="react-root"]/section/main/div/div/article/div[3]/div[1]""").text
    hashtags = find_hashtags(comment)
    mentions = find_mentions(comment)
    post_details = {'link': url, 'type': post_type, 'likes/views': likes,
                    'age': age, 'comment': comment, 'hashtags': hashtags,
                    'mentions': mentions}
    time.sleep(10)
    return post_details
