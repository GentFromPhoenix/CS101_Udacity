def get_all_links(page): 
    links = [] 
    while True: 
        url, endpos = get_next_target(page)
        if url: 
            links.append(url) page = page[endpos:] 
        else: 
            break 
    return links

def crawl_web(seed): 
    tocrawl = [seed] 
    crawled = [] 
    index = {} # changed to dictionary
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled: 
            content = get_page(page) 
            add_page_to_index(index, page, content) 
            union(tocrawl, get_all_links(content)) 
            crawled.append(page) 
    return index 

def add_page_to_index(index, url, content): 
    words = content.split() 
    for word in words: 
        add_to_index(index, word, url) 

def add_to_index(index, keyword, url): 
    if keyword in index:  # remember 'index' is now a dictionary
        index[keyword].append(url)
    else:
        index[keyword] = [url] # This adds a new entry if keyword not in index
                               # keyword : url
    for entry in index: 
        if entry[0] == keyword: 
            entry[1].append(url) 
            return 
    # not found, add new keyword to index 
    index.append([keyword, [url]]) 

def lookup(index, keyword): 
    if keyword in index:
        return index[keyword]
    else:
        return None
   